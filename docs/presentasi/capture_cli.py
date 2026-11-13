"""
Perekam cuplikan terminal Stokku Desktop (Fase 1)
PIC: YUKEN VELINO (15260767 / @Curzyori)

Menjalankan progress_p7/main_p7.py di dalam pseudo terminal (pty) sehingga
keluaran yang ditangkap identik dengan sesi interaktif asli, termasuk input
yang diketik pengguna. Hasilnya dirender menjadi PNG bergaya terminal.

Jalankan dari root proyek Stokku-Desktop:
    python docs/presentasi/capture_cli.py

Keluaran:
    docs/assets/cli_menu.png
    docs/assets/cli_tabel.png
    docs/assets/cli_anti_minus.png
    docs/assets/cli_uji.png
"""

import os
import pty
import select
import subprocess
import sys
import time

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS = os.path.join(ROOT, "docs", "assets")
MAIN = os.path.join("progress_p7", "main_p7.py")

FONT_REGULAR = os.path.expanduser(
    "~/.local/share/fonts/JetBrainsMono/JetBrainsMono-Regular.ttf"
)
FONT_BOLD = os.path.expanduser(
    "~/.local/share/fonts/JetBrainsMono/JetBrainsMono-Bold.ttf"
)

BG = (15, 23, 42)
FG = (226, 232, 240)
FG_DIM = (148, 163, 184)
FG_PROMPT = (45, 212, 191)
FG_OK = (52, 211, 153)
FG_WARN = (251, 191, 36)
FG_ERR = (251, 113, 133)

FONT_SIZE = 19
LINE_HEIGHT = 26
PAD_X = 26
PAD_Y = 20
CHROME_H = 36
MAX_COLS = 104

PROMPT = "$ python progress_p7/main_p7.py"


def run_cli(inputs, settle=0.22):
    """Menjalankan CLI di dalam pty dan mengembalikan transkrip asli."""
    master, slave = pty.openpty()
    env = dict(os.environ, TERM="dumb", COLUMNS=str(MAX_COLS), LINES="40")
    proc = subprocess.Popen(
        [sys.executable, MAIN],
        cwd=ROOT,
        stdin=slave,
        stdout=slave,
        stderr=slave,
        env=env,
        close_fds=True,
    )
    os.close(slave)

    chunks = []

    def drain(timeout):
        end = time.time() + timeout
        while time.time() < end:
            ready, _, _ = select.select([master], [], [], 0.05)
            if not ready:
                continue
            try:
                data = os.read(master, 65536)
            except OSError:
                return False
            if not data:
                return False
            chunks.append(data)
        return True

    drain(settle)
    for item in inputs:
        os.write(master, (item + "\n").encode())
        drain(settle)

    # Tunggu sampai proses selesai
    deadline = time.time() + 8
    while proc.poll() is None and time.time() < deadline:
        if not drain(0.1):
            break
    drain(0.2)

    try:
        os.close(master)
    except OSError:
        pass
    proc.wait(timeout=5)

    raw = b"".join(chunks).decode("utf-8", errors="replace")
    raw = raw.replace("\r\n", "\n").replace("\r", "")
    return raw.split("\n")


def wrap(text, width=MAX_COLS):
    """Membungkus baris panjang tanpa memotong kata bila memungkinkan."""
    if len(text) <= width:
        return [text]
    out, current = [], ""
    for word in text.split(" "):
        candidate = word if not current else current + " " + word
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word if len(word) <= width else word[:width]
    if current:
        out.append(current)
    return out


def color_for(line):
    stripped = line.strip()
    if stripped.startswith("[Berhasil]") or "LULUS" in stripped:
        return FG_OK
    if stripped.startswith("[Peringatan]") or stripped.startswith("[Batal]"):
        return FG_ERR
    if stripped.startswith("[INFO]"):
        return FG_WARN
    if set(stripped) <= {"=", "-", "+", "|", " "} and stripped:
        return FG_DIM
    return FG


def render(lines, out_path, title, wrap_cols=MAX_COLS, target_width=1560):
    body = []
    for ln in lines:
        body.extend(wrap(ln, wrap_cols) if wrap_cols else [ln])

    size = FONT_SIZE
    while True:
        font = ImageFont.truetype(FONT_REGULAR, size)
        font_bold = ImageFont.truetype(FONT_BOLD, size)
        font_chrome = ImageFont.truetype(FONT_BOLD, 14)
        widest = max([font.getbbox(PROMPT)[2]] + [font.getbbox(ln)[2] for ln in body])
        if widest + PAD_X * 2 <= target_width or size <= 11:
            break
        size -= 1

    line_h = max(LINE_HEIGHT, size + 7)
    width = widest + PAD_X * 2
    height = CHROME_H + PAD_Y * 2 + line_h * (len(body) + 1)

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, width, CHROME_H], fill=(30, 41, 59))
    for i, col in enumerate([(248, 113, 113), (251, 191, 36), (52, 211, 153)]):
        cx = 18 + i * 20
        draw.ellipse([cx - 5, CHROME_H // 2 - 5, cx + 5, CHROME_H // 2 + 5], fill=col)
    tw = font_chrome.getbbox(title)[2]
    draw.text(((width - tw) // 2, CHROME_H // 2 - 9), title,
              font=font_chrome, fill=FG_DIM)

    y = CHROME_H + PAD_Y
    draw.text((PAD_X, y), PROMPT, font=font_bold, fill=FG_PROMPT)
    y += line_h
    for ln in body:
        if ln.strip():
            draw.text((PAD_X, y), ln, font=font, fill=color_for(ln))
        y += line_h

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, optimize=True)
    print(f"saved {os.path.relpath(out_path, ROOT)} ({img.shape if hasattr(img, 'shape') else img.size})")


def slice_between(lines, start_pred, stop_pred, include_stop=True):
    start = next((i for i, ln in enumerate(lines) if start_pred(ln)), None)
    if start is None:
        return []
    for i in range(start + 1, len(lines)):
        if stop_pred(lines[i]):
            return lines[start:i + (1 if include_stop else 0)]
    return lines[start:]


def main():
    # 1. Banner dan menu utama
    menu = run_cli([])
    render(
        slice_between(
            menu,
            lambda ln: "STOKKU DESKTOP" in ln,
            lambda ln: ln.strip().startswith("Pilih menu"),
        ),
        os.path.join(ASSETS, "cli_menu.png"),
        "Stokku Desktop: menu utama",
    )

    # 2. Tabel persediaan (Menu 1)
    tabel = run_cli(["1"])
    blok = []
    inside = False
    for ln in tabel:
        st = ln.strip()
        is_row = st.startswith("|") or (st.startswith("+") and set(st) <= {"+", "-"})
        if is_row:
            inside = True
            blok.append(ln)
        elif inside:
            break
    render(blok, os.path.join(ASSETS, "cli_tabel.png"),
           "Stokku Desktop: Menu 1 daftar stok", wrap_cols=None)

    # 3. Mutasi keluar: satu ditolak, satu berhasil
    keluar = run_cli(
        ["4", "KRT01", "50", "Coba melebihi stok", "4", "KRT01", "4", "Penjualan toko"]
    )
    keep = [
        ln for ln in keluar
        if ln.strip().startswith(("---", "Masukkan", "Produk Terpilih",
                                  "[Batal]", "[Berhasil]"))
    ]
    render(keep, os.path.join(ASSETS, "cli_anti_minus.png"),
           "Stokku Desktop: Menu 4 anti stok minus")

    # 4. Hasil pengujian otomatis (Menu 7)
    uji = run_cli(["7"])
    ringkas = [
        ln for ln in uji
        if ln.strip().startswith(("[TC-", "HASIL AKHIR", "KESIMPULAN", " PENGUJIAN", "Status:"))
        or ln.strip().startswith("=" * 20)
    ]
    render(ringkas, os.path.join(ASSETS, "cli_uji.png"),
           "Stokku Desktop: Menu 7 pengujian otomatis")


if __name__ == "__main__":
    main()
