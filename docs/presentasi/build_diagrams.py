"""
Pembangkit diagram dari blok mermaid di README.md
PIC: YUKEN VELINO (15260767 / @Curzyori)

Sumber tunggal diagram adalah blok ```mermaid di README.md. Skrip ini:
  1. mengekstrak setiap blok mermaid menjadi berkas docs/diagrams/*.mmd
  2. merender setiap .mmd menjadi PNG di docs/assets/diagrams/*.png
  3. mengganti blok mermaid di README dengan referensi gambar PNG

Prasyarat: mermaid-cli (mmdc) dan Chromium/Brave.

Pemakaian dari root proyek Stokku-Desktop:
    python docs/presentasi/build_diagrams.py            # ekstrak + render + tulis README
    python docs/presentasi/build_diagrams.py --no-readme  # hanya ekstrak + render

Variabel lingkungan opsional:
    MMDC          perintah mermaid-cli, default "npx mmdc"
    PUPPETEER_CFG berkas konfigurasi puppeteer
    CHROME_BIN    path Chromium/Brave
"""

import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README = os.path.join(ROOT, "README.md")
MMD_DIR = os.path.join(ROOT, "docs", "diagrams")
PNG_DIR = os.path.join(ROOT, "docs", "assets", "diagrams")

SLUGS = [
    "01-arsitektur-sistem",
    "02-alur-program-utama",
    "03-menu-1-daftar-stok",
    "04-menu-2-tambah-barang",
    "05-menu-3-barang-masuk",
    "06-menu-4-barang-keluar",
    "07-menu-5-riwayat-mutasi",
    "08-menu-6-laporan-pandas",
    "09-menu-7-uji-otomatis",
    "10-menu-0-keluar",
]


def extract_blocks(lines):
    """Mengembalikan daftar (judul_heading, indeks_awal, indeks_akhir, isi)."""
    heading = ""
    blocks = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#"):
            heading = lines[i].lstrip("# ").strip()
        if lines[i].strip() == "```mermaid":
            j = i + 1
            body = []
            while j < len(lines) and lines[j].strip() != "```":
                body.append(lines[j])
                j += 1
            blocks.append((heading, i, j, "\n".join(body)))
            i = j
        i += 1
    return blocks


def write_mmd(slug, body):
    os.makedirs(MMD_DIR, exist_ok=True)
    path = os.path.join(MMD_DIR, f"{slug}.mmd")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body.rstrip() + "\n")
    return path


def ensure_puppeteer_conf():
    conf = os.environ.get("PUPPETEER_CFG")
    if conf and os.path.isfile(conf):
        return conf
    chrome = os.environ.get("CHROME_BIN")
    if not chrome:
        for candidate in ("/usr/bin/brave", "/usr/bin/chromium",
                          "/usr/bin/google-chrome", "/usr/bin/chromium-browser"):
            if os.path.isfile(candidate):
                chrome = candidate
                break
    os.makedirs(MMD_DIR, exist_ok=True)
    conf_path = os.path.join(MMD_DIR, "puppeteer.json")
    with open(conf_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "executablePath": chrome,
                "headless": True,
                "args": ["--no-sandbox", "--disable-setuid-sandbox",
                         "--disable-dev-shm-usage"],
            },
            f,
            indent=2,
        )
    return conf_path


def render(mmd_path, png_path, conf, scale=2):
    os.makedirs(os.path.dirname(png_path), exist_ok=True)
    cmd = (os.environ.get("MMDC", "npx mmdc")).split() + [
        "-i", mmd_path,
        "-o", png_path,
        "-p", conf,
        "-b", "white",
        "-s", str(scale),
    ]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"  GAGAL {os.path.basename(png_path)}")
        print(proc.stderr.strip()[-600:])
        return False
    print(f"  ok {os.path.relpath(png_path, ROOT)}")
    return True


def rewrite_readme(lines, blocks, slugs):
    """Mengganti blok mermaid dengan referensi gambar PNG."""
    out = list(lines)
    for (heading, start, end, _body), slug in sorted(
        zip(blocks, slugs), key=lambda pair: pair[0][1], reverse=True
    ):
        alt = heading.replace("|", "/")
        img = f"![Diagram: {alt}](docs/assets/diagrams/{slug}.png)"
        out[start:end + 1] = [img]
    with open(README, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return len(blocks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-readme", action="store_true",
                    help="jangan ubah README, hanya ekstrak dan render")
    ap.add_argument("--scale", type=int, default=2)
    args = ap.parse_args()

    with open(README, encoding="utf-8") as f:
        lines = f.read().split("\n")

    blocks = extract_blocks(lines)
    if not blocks:
        print("Tidak ada blok mermaid di README.md")
        return 1
    if len(blocks) > len(SLUGS):
        print(f"Blok mermaid {len(blocks)} melebihi daftar slug {len(SLUGS)}")
        return 1

    slugs = SLUGS[: len(blocks)]
    conf = ensure_puppeteer_conf()

    failed = 0
    for (heading, _s, _e, body), slug in zip(blocks, slugs):
        mmd = write_mmd(slug, body)
        if not render(mmd, os.path.join(PNG_DIR, f"{slug}.png"), conf, args.scale):
            failed += 1

    print(f"\n{len(blocks) - failed} dari {len(blocks)} diagram berhasil dirender")

    if not args.no_readme and failed == 0:
        n = rewrite_readme(lines, blocks, slugs)
        print(f"{n} blok mermaid di README.md diganti referensi gambar PNG")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
