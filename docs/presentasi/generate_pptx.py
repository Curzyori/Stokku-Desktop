"""
Pembangkit Deck Presentasi Stokku Desktop (Evaluasi UTS Pertemuan 8)
PIC: YUKEN VELINO (15260767 / @Curzyori) - Kelompok 4 Dasar Pemrograman 15.1C.30

Jalankan dari root proyek Stokku-Desktop:
    python docs/presentasi/generate_pptx.py

Prasyarat gambar (dibuat oleh skrip pendamping):
    python docs/presentasi/capture_cli.py      -> docs/assets/cli_*.png
    python docs/presentasi/build_diagrams.py   -> docs/assets/diagrams/*.png

Susunan slide:
 1. Layar kosong (putih)
 2. Judul materi dan identitas akademik
 3. Latar belakang dan masalah
 4. Diagram arsitektur sistem
 5. Flowchart alur program utama
 6. Flowchart validasi anti stok minus
 7. Tampilan output program (menu dan daftar stok)
 8. Tampilan output program (anti stok minus dan pengujian)
 9. Pemetaan silabus P01-P07
10. Hasil 7 kasus uji
11. Formula aset modal dan ambang kritis
12. Dokumentasi kegiatan
13. Roadmap versi 2.0
14. Kesimpulan dan pembagian peran
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

C_BG = RGBColor(248, 250, 252)
C_WHITE = RGBColor(255, 255, 255)
C_NAVY = RGBColor(15, 23, 42)
C_SLATE = RGBColor(51, 65, 85)
C_MUTED = RGBColor(71, 85, 105)
C_TEAL = RGBColor(13, 148, 136)
C_TEAL_DARK = RGBColor(15, 118, 110)
C_CARD_BG = RGBColor(255, 255, 255)
C_CARD_BORDER = RGBColor(226, 232, 240)
C_RED = RGBColor(190, 18, 60)
C_GREEN = RGBColor(4, 120, 87)
C_LIGHT_TEAL = RGBColor(240, 253, 250)

SLIDE_W = 13.333
SLIDE_H = 7.5

DATA_AWAL_RINGKAS = [
    ("ATK01", "Buku Tulis Kiky 38 Lembar", 15, 3500),
    ("ATK02", "Pulpen Faster C600 Hitam", 4, 2500),
    ("KRT01", "Kertas HVS Sinar Dunia A4 75gr", 10, 42000),
]
TOTAL_SKU = len(DATA_AWAL_RINGKAS)
TOTAL_UNIT = sum(s for _, _, s, _ in DATA_AWAL_RINGKAS)
TOTAL_MODAL = sum(s * h for _, _, s, h in DATA_AWAL_RINGKAS)

HASIL_UJI = [
    ("TC-01", "Inisialisasi data master dan saldo awal",
     "3 produk bawaan dan 3 entri log awal dimuat",
     "3 SKU, 3 log, saldo awal terbaca"),
    ("TC-02", "Tambah barang valid dan proteksi duplikat",
     "Tambah ATK03 (20 Pcs), lalu input ulang atk01",
     "ATK03 tersimpan, kode kembar ditolak"),
    ("TC-03", "Transaksi barang masuk (restock)",
     "Restock ATK01 sebanyak 10 Pcs",
     "Stok 15 menjadi 25, log MASUK tercatat"),
    ("TC-04", "Transaksi barang keluar normal",
     "Keluarkan ATK01 sebanyak 5 Pcs",
     "Stok 25 menjadi 20, log KELUAR tercatat"),
    ("TC-05", "Validasi anti stok minus",
     "Keluarkan ATK02 sebanyak 10 Pcs (stok 4)",
     "Ditolak, stok tetap 4, log tidak bertambah"),
    ("TC-06", "Deteksi status kritis",
     "ATK02 stok 4 min 5, KRT01 keluar 8 dari 10",
     "ATK02 KRITIS, KRT01 AMAN menjadi KRITIS"),
    ("TC-07", "Akurasi total unit dan nilai modal",
     "Hitung sum stok dan sum stok x harga beli",
     "46 unit, modal Rp 194.000, cocok manual"),
]

SILABUS = [
    ("P01", "Tools, Best Practice dan PEP 8",
     "Struktur modul rapi, indentasi 4 spasi, penamaan variabel jelas", "Seluruh berkas"),
    ("P02", "Sintaks, Variabel dan Tipe Data",
     "str untuk kode dan nama, int untuk stok dan harga, bool PANDAS_TERSEDIA sebagai penanda ketersediaan pandas",
     "data_store.py, laporan_pandas.py"),
    ("P03", "String, Format dan Operator",
     "strip, upper, isdigit, format Rupiah, operator += dan -=",
     "validasi.py, display_cli.py"),
    ("P04", "Percabangan if elif else",
     "Validasi keluar tidak melebihi stok, penentuan status kritis", "validasi.py"),
    ("P05", "Perulangan while dan for",
     "while True untuk menu, for untuk tabel dan akumulasi aset", "main_p7.py"),
    ("P06", "Struktur Data List dan Tuple",
     "list of dict untuk master barang, list of tuple untuk log mutasi", "data_store.py"),
    ("P07", "Matriks dan Library Pandas",
     "DataFrame 12 kolom, groupby kategori, statistik deskriptif", "laporan_pandas.py"),
]

DOKUMENTASI = [
    ("docs/assets/P1_2026-11-13.jpg",
     "Sesi 1: Pengembangan Mesin Inti",
     "Yuken Velino dan Mahardika Athaillah",
     "Modul backend, validasi anti stok minus, dan tabel terminal"),
    ("docs/assets/P2_2026-11-13.jpg",
     "Sesi 2: Integrasi Modul, Deck Presentasi, dan Draf Makalah",
     "Yuken Velino, Mahardika Athaillah, dan Renkyna Aftania Nasution",
     "Integrasi modul Pandas, deck presentasi, dan draf makalah"),
]

CATATAN_PEMBICARA = {
    1: ("Semua", [
        "Slide ini sengaja dibiarkan putih kosong.",
        "Dipakai sebagai jeda saat kelompok naik ke depan kelas.",
        "Bila laptop lambat, sebutkan judul proyek secara lisan.",
    ]),
    2: ("Yuken Velino", [
        "Buka dengan salam dan perkenalkan diri sebagai ketua kelompok.",
        "Perkenalkan kedua anggota lain beserta perannya.",
        "Sebutkan mata kuliah, kelas, dan nama dosen pengampu.",
        "Satu kalimat inti: aplikasi mencatat persediaan dan mutasi stok gudang UMKM.",
    ]),
    3: ("Mahardika Athaillah", [
        "Jelaskan empat masalah pencatatan manual secara berurutan.",
        "Tekankan masalah keempat: nilai modal yang tertanam tidak diketahui.",
        "Tutup dengan kartu solusi: Stokku Desktop berjalan luring.",
    ]),
    4: ("Yuken Velino", [
        "Tunjuk main_p7.py sebagai satu-satunya titik masuk.",
        "Sebutkan enam modul yang dipanggil dari sana.",
        "Tegaskan tiap modul terpisah agar tidak bentrok saat digabung.",
    ]),
    5: ("Yuken Velino", [
        "Jelaskan perulangan while True dan percabangan if elif else.",
        "Tegaskan input tidak valid tidak menghentikan program.",
        "Sebutkan pilihan 0 dipakai untuk keluar.",
    ]),
    6: ("Yuken Velino", [
        "Ini aturan inti proyek: stok tidak boleh minus.",
        "Telusuri alur sampai kotak jumlah lebih besar dari stok.",
        "Tegaskan jalur ditolak: stok utuh dan log tidak bertambah.",
        "Sebutkan fungsi validasi_stok_keluar sebagai penjaga.",
    ]),
    7: ("Mahardika Athaillah", [
        "Perlihatkan menu operasional yang tampil setelah program dijalankan.",
        "Sebutkan delapan pilihan dan fungsinya masing-masing.",
        "Tunjuk kolom kanan sebagai poin yang perlu ditekankan.",
    ]),
    8: ("Mahardika Athaillah", [
        "Tunjuk baris ATK02 dengan status KRITIS.",
        "Jelaskan arti KRITIS: stok kurang dari atau sama dengan batas minimum.",
        "Sebutkan kolom harga disembunyikan agar huruf terbaca.",
    ]),
    9: ("Mahardika Athaillah", [
        "Tunjukkan penolakan transaksi 50 Rim saat stok 10 Rim.",
        "Tunjukkan transaksi 4 Rim yang diterima beserta sisa stok.",
        "Tegaskan pesan penolakan memakai satuan yang sama dengan tabel.",
    ]),
    10: ("Renkyna Aftania Nasution", [
        "Petakan tiap pertemuan P01 sampai P07 ke berkas kode yang nyata.",
        "Tekankan tidak ada materi yang dilompati.",
        "Sebutkan P07 dipegang modul laporan_pandas.",
    ]),
    11: ("Renkyna Aftania Nasution", [
        "Bacakan tujuh kasus uji secara ringkas.",
        "Tegaskan TC-05 sebagai bukti proteksi anti stok minus.",
        "Sebutkan tambahan 15 unit test di folder tests.",
        "Sebutkan hasil dicatat ke draf makalah.",
    ]),
    12: ("Renkyna Aftania Nasution", [
        "Jelaskan rumus nilai aset per produk dan total aset gudang.",
        "Bacakan angka saldo awal: tiga SKU, 29 unit, Rp 482.500.",
        "Jelaskan ambang batas kritis: stok kurang dari atau sama dengan min_stok.",
    ]),
    13: ("Renkyna Aftania Nasution", [
        "Sebutkan dua sesi kerja dan siapa saja yang hadir di masing-masing sesi.",
        "Sesi 1 mengerjakan mesin inti dan antarmuka terminal.",
        "Sesi 2 mengerjakan integrasi modul Pandas, deck presentasi, dan draf makalah.",
    ]),
    14: ("Mahardika Athaillah", [
        "Jelaskan rencana P09 sampai P16 menuju UAS.",
        "Sebutkan migrasi ke SQLite dan antarmuka Tkinter pada P10 sampai P12.",
        "Sebutkan makalah final dan demonstrasi laboratorium pada P13 sampai P16.",
    ]),
    15: ("Yuken Velino", [
        "Bacakan empat poin kesimpulan.",
        "Sebutkan matriks tanggung jawab tiap anggota.",
        "Tutup dengan terima kasih lalu buka sesi tanya jawab.",
        "Bila ditanya bukti, tunjukkan repositori publik dan jalankan skrip uji.",
    ]),
}


def _textbox(slide, left, top, width, height):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0)
    tf.vertical_anchor = MSO_ANCHOR.TOP
    return tf


def _para(tf, text, font, size, color, bold=False, after=0, first=False, align=None):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.text = text
    p.font.name = font
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    if after:
        p.space_after = Pt(after)
    if align is not None:
        p.alignment = align
    return p


def fit_picture(slide, path, left, top, max_w, max_h):
    """Menempatkan gambar dengan rasio asli di dalam kotak, rata tengah."""
    if not os.path.isfile(path):
        tf = _textbox(slide, left, top, max_w, Inches(0.6))
        _para(tf, f"Gambar belum dibuat: {os.path.relpath(path)}",
              "Consolas", 11, C_RED, first=True)
        return None

    with Image.open(path) as im:
        ratio = im.size[0] / im.size[1]

    box_ratio = max_w / max_h
    if ratio >= box_ratio:
        width = max_w
        height = int(max_w / ratio)
    else:
        height = max_h
        width = int(max_h * ratio)

    left += int((max_w - width) / 2)
    top += int((max_h - height) / 2)
    picture = slide.shapes.add_picture(path, left, top, width=width, height=height)
    return picture, int(height), int(width)


def create_deck(output_path, root=None):
    root = root or os.getcwd()
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    blank = prs.slide_layouts[6]

    def background(slide, color=C_BG):
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(SLIDE_W), Inches(SLIDE_H)
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def header(slide, tag_text, title_text, subtitle=None):
        tf = _textbox(slide, Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.2))
        _para(tf, tag_text.upper(), "Arial", 11, C_TEAL_DARK, bold=True, after=4, first=True)
        _para(tf, title_text, "Trebuchet MS", 24, C_NAVY, bold=True, after=4)
        if subtitle:
            _para(tf, subtitle, "Calibri", 13, C_SLATE)

    def card(slide, left, top, width, height,
             bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
        shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shp.fill.solid()
        shp.fill.fore_color.rgb = bg_color
        if border_color:
            shp.line.color.rgb = border_color
            shp.line.width = Pt(1)
        else:
            shp.line.fill.background()
        shp.text_frame.vertical_anchor = MSO_ANCHOR.TOP
        return shp

    def table_header(table, headers, center_cols):
        for j, h in enumerate(headers):
            cell = table.cell(0, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_NAVY
            p = cell.text_frame.paragraphs[0]
            p.text = h
            p.font.name = "Trebuchet MS"
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = C_WHITE
            if j in center_cols:
                p.alignment = PP_ALIGN.CENTER

    def diagram_slide(tag, title, subtitle, image_name, caption, poin=()):
        slide = prs.slides.add_slide(blank)
        background(slide)
        header(slide, tag, title, subtitle)
        card(slide, Inches(0.8), Inches(1.85), Inches(11.733), Inches(4.75),
             bg_color=C_WHITE)
        hasil = fit_picture(
            slide,
            os.path.join(root, "docs", "assets", "diagrams", image_name),
            Inches(0.95), Inches(1.95), Inches(11.43), Inches(3.3),
        )
        if hasil:
            _, tinggi, _ = hasil
            y_poin = Inches(1.95) + tinggi + Inches(0.22)
            tf = _textbox(slide, Inches(1.2), y_poin, Inches(11.0), Inches(1.2))
            for i, baris in enumerate(poin):
                _para(tf, "\u2022 " + baris, "Calibri", 12, C_SLATE,
                      after=5, first=(i == 0))
        tf = _textbox(slide, Inches(0.8), Inches(6.72), Inches(11.733), Inches(0.5))
        _para(tf, caption, "Calibri", 10.5, C_MUTED, first=True)
        return slide

    def output_slide(tag, title, subtitle, items, caption):
        slide = prs.slides.add_slide(blank)
        background(slide)
        header(slide, tag, title, subtitle)
        for spec in items:
            left, top, w, h = spec["box"]
            card(slide, left, top, w, h, bg_color=C_WHITE)
            fit_picture(slide, os.path.join(root, spec["path"]),
                        left + Inches(0.12), top + Inches(0.12),
                        w - Inches(0.24), h - Inches(0.24))
            if spec.get("label"):
                tf = _textbox(slide, left, top + h + Inches(0.05), w, Inches(0.3))
                _para(tf, spec["label"], "Calibri", 9.5, C_MUTED, first=True)
        tf = _textbox(slide, Inches(0.8), Inches(6.95), Inches(11.733), Inches(0.4))
        _para(tf, caption, "Calibri", 10.5, C_MUTED, first=True)
        return slide

    # ------------------------------------------------------------------
    # 1. LAYAR KOSONG
    # ------------------------------------------------------------------
    background(prs.slides.add_slide(blank), C_WHITE)

    # ------------------------------------------------------------------
    # 2. JUDUL DAN IDENTITAS
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s, C_WHITE)
    bar = s.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(SLIDE_W), Inches(0.15)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_TEAL
    bar.line.fill.background()

    tf = _textbox(s, Inches(1.0), Inches(1.3), Inches(7.5), Inches(5.0))
    _para(tf, "EVALUASI PROGRES PROYEK PERTEMUAN 8 (UTS)",
          "Arial", 11, C_TEAL, bold=True, after=12, first=True)
    _para(tf, "STOKKU DESKTOP", "Trebuchet MS", 40, C_NAVY, bold=True, after=8)
    _para(tf,
          "Aplikasi Manajemen Persediaan dan Pencatatan Mutasi Stok "
          "Gudang UMKM Berbasis Python (Offline-First)",
          "Calibri", 16, C_SLATE, after=36)
    _para(tf,
          "Mata Kuliah   : Dasar Pemrograman (Kode: 894)\n"
          "Kelas / Prodi : 15.1C.30 / Teknik Informatika\n"
          "Institusi     : Universitas Bina Sarana Informatika (UBSI)\n"
          "Dosen         : Ali Mustopa, M.Kom (Kode Dosen: AOP)",
          "Consolas", 12.5, C_SLATE)

    tf_team = card(s, Inches(8.8), Inches(1.3), Inches(3.7), Inches(5.0),
                   bg_color=C_BG, border_color=C_CARD_BORDER).text_frame
    tf_team.word_wrap = True
    tf_team.margin_left = tf_team.margin_right = Inches(0.3)
    tf_team.margin_top = Inches(0.4)
    _para(tf_team, "KELOMPOK 4", "Arial", 14, C_NAVY, bold=True, after=16, first=True)
    for nama, nim, peran in [
        ("Yuken Velino", "15260767", "Backend Logic dan Test Runner"),
        ("Mahardika Athaillah", "15260673", "Antarmuka CLI dan Presentasi"),
        ("Renkyna Aftania N.", "15260847", "Analitik Pandas dan Makalah"),
    ]:
        _para(tf_team, nama, "Trebuchet MS", 12.5, C_NAVY, bold=True)
        _para(tf_team, f"NIM {nim}", "Calibri", 11, C_MUTED)
        _para(tf_team, peran, "Calibri", 11.5, C_SLATE, after=14)

    # ------------------------------------------------------------------
    # 3. LATAR BELAKANG
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Latar Belakang dan Analisis Masalah",
           "Tantangan Pencatatan Persediaan Barang di Toko UMKM",
           "Pencatatan manual menimbulkan inefisiensi, rawan selisih, "
           "dan ketidakpastian nilai modal.")

    card_w, card_h, gap = Inches(2.7), Inches(3.05), Inches(0.3)
    for i, (judul, isi) in enumerate([
        ("1. Sisa Fisik Tidak Pasti",
         "Pemilik toko tidak mengetahui jumlah barang terkini tanpa menghitung "
         "ulang fisik (stock opname) yang menyita waktu operasional."),
        ("2. Pengadaan Terlambat",
         "Ketiadaan ambang batas minimum membuat restock terlambat, sehingga "
         "potensi transaksi penjualan hilang."),
        ("3. Selisih Stok",
         "Barang rusak, kedaluwarsa, atau pemakaian internal sering tidak tercatat, "
         "sehingga pembukuan tidak cocok dengan saldo fisik."),
        ("4. Modal Tidak Terhitung",
         "Sulit menghitung total nilai uang yang mengendap pada stok gudang "
         "tanpa rekapitulasi nilai modal."),
    ]):
        tf = card(s, Inches(0.8) + i * (card_w + gap), Inches(1.95),
                  card_w, card_h).text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.3)
        _para(tf, judul, "Trebuchet MS", 13, C_NAVY, bold=True, after=10, first=True)
        _para(tf, isi, "Calibri", 11.5, C_SLATE)

    tf_sol = card(s, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.35),
                  bg_color=C_LIGHT_TEAL, border_color=C_TEAL).text_frame
    tf_sol.word_wrap = True
    tf_sol.margin_left = tf_sol.margin_right = Inches(0.3)
    tf_sol.margin_top = Inches(0.2)
    _para(tf_sol, "SOLUSI: STOKKU DESKTOP (OFFLINE-FIRST)",
          "Arial", 11.5, C_TEAL_DARK, bold=True, after=4, first=True)
    _para(tf_sol,
          "Aplikasi lokal mandiri berbasis Python untuk mengelola data master, "
          "mutasi restock, transaksi keluar dengan validasi anti stok minus, "
          "deteksi stok kritis, dan perhitungan total aset modal gudang.",
          "Calibri", 11, C_NAVY)

    # ------------------------------------------------------------------
    # 4. DIAGRAM ARSITEKTUR
    # ------------------------------------------------------------------
    diagram_slide(
        "Diagram Sistem", "Arsitektur Modul dan Alur Ketergantungan",
        "Enam modul terisolasi di progress_p7 dengan satu titik masuk main_p7.py.",
        "slide-04-arsitektur.png",
        "Gambar 1. Diagram arsitektur ringkas: satu titik masuk dan enam modul.",
        poin=[
            "main_p7.py hanya mengimpor dan memanggil, tidak menyimpan data.",
            "engine_stok memanggil validasi sebelum mengubah angka stok.",
            "Setiap berkas punya satu pemilik agar tidak bentrok saat digabung.",
        ],
    )

    # ------------------------------------------------------------------
    # 5. FLOWCHART ALUR PROGRAM
    # ------------------------------------------------------------------
    diagram_slide(
        "Flowchart", "Alur Program Utama (Menu 0 sampai 7)",
        "Perulangan while True dengan percabangan if elif else untuk delapan pilihan.",
        "slide-05-alur-utama.png",
        "Gambar 2. Flowchart siklus menu dan percabangan validasi pilihan.",
        poin=[
            "Percabangan memakai if elif else sesuai materi Pertemuan 4.",
            "Input di luar 0 sampai 7 kembali ke menu tanpa keluar program.",
            "Perulangan berhenti hanya pada pilihan 0.",
        ],
    )

    # ------------------------------------------------------------------
    # 6. FLOWCHART ANTI STOK MINUS
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Flowchart", "Alur Validasi Anti Stok Minus",
           "Aturan inti: transaksi keluar dibatalkan bila kuantitas melebihi "
           "stok fisik.")
    card(s, Inches(0.8), Inches(1.8), Inches(11.733), Inches(2.45),
         bg_color=C_WHITE)
    fit_picture(
        s,
        os.path.join(root, "docs", "assets", "diagrams", "slide-06-anti-minus.png"),
        Inches(0.95), Inches(1.9), Inches(11.43), Inches(2.25),
    )
    tf = _textbox(s, Inches(0.8), Inches(4.28), Inches(11.733), Inches(0.3))
    _para(tf, "Gambar 3. Flowchart validasi mutasi barang keluar.",
          "Calibri", 10.5, C_MUTED, first=True)

    tf_reject = card(s, Inches(0.8), Inches(4.75), Inches(5.733), Inches(1.95),
                     bg_color=RGBColor(255, 241, 242),
                     border_color=C_RED).text_frame
    tf_reject.word_wrap = True
    tf_reject.margin_left = tf_reject.margin_right = Inches(0.28)
    tf_reject.margin_top = Inches(0.22)
    _para(tf_reject, "JALUR DITOLAK (jumlah lebih besar dari stok)",
          "Trebuchet MS", 12, C_RED, bold=True, after=8, first=True)
    _para(tf_reject,
          "Fungsi validasi_stok_keluar() mengembalikan False sebelum operasi "
          "pengurangan dijalankan. Stok fisik tetap, dan log_mutasi tidak "
          "bertambah satu baris pun.",
          "Calibri", 11, C_SLATE)

    tf_accept = card(s, Inches(6.8), Inches(4.75), Inches(5.733), Inches(1.95),
                     bg_color=C_LIGHT_TEAL,
                     border_color=C_GREEN).text_frame
    tf_accept.word_wrap = True
    tf_accept.margin_left = tf_accept.margin_right = Inches(0.28)
    tf_accept.margin_top = Inches(0.22)
    _para(tf_accept, "JALUR DITERIMA (jumlah tidak melebihi stok)",
          "Trebuchet MS", 12, C_GREEN, bold=True, after=8, first=True)
    _para(tf_accept,
          "Sistem menjalankan stok = stok dikurangi jumlah, lalu mencatat "
          "tuple mutasi KELUAR berisi stok sebelum dan sesudah.",
          "Calibri", 11, C_SLATE)

    # ------------------------------------------------------------------
    # 7. TAMPILAN OUTPUT: MENU
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Bukti Eksekusi", "Tampilan Output: Menu Operasional",
           "Keluaran asli python progress_p7/main_p7.py tanpa banner, "
           "diperbesar agar terbaca dari baris belakang.")
    card(s, Inches(0.8), Inches(1.9), Inches(11.733), Inches(4.62),
         bg_color=C_WHITE)
    fit_picture(
        s, os.path.join(root, "docs", "assets", "cli_menu_only.png"),
        Inches(1.2), Inches(1.98), Inches(6.9), Inches(4.46),
    )
    tf = _textbox(s, Inches(8.4), Inches(2.2), Inches(3.9), Inches(3.9))
    _para(tf, "YANG PERLU DITUNJUK", "Arial", 11, C_TEAL_DARK, bold=True,
          after=10, first=True)
    for poin in [
        "Delapan pilihan menu, dari lihat stok sampai uji otomatis.",
        "Menu 0 dipakai untuk keluar dengan rapi.",
        "Input selain 0 sampai 7 ditolak tanpa menghentikan program.",
        "Perulangan while True menjaga menu tetap tampil.",
    ]:
        _para(tf, "\u2022 " + poin, "Calibri", 12, C_SLATE, after=9)

    # ------------------------------------------------------------------
    # 8. TAMPILAN OUTPUT: DAFTAR STOK
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Bukti Eksekusi", "Tampilan Output: Daftar Stok dan Status Kritis",
           "Empat kolom terpenting dari Menu 1, diperbesar agar angka dan "
           "penanda status terbaca.")
    card(s, Inches(0.8), Inches(1.9), Inches(11.733), Inches(4.5),
         bg_color=C_WHITE)
    fit_picture(
        s, os.path.join(root, "docs", "assets", "cli_tabel_ringkas.png"),
        Inches(0.95), Inches(2.0), Inches(11.43), Inches(4.3),
    )
    tf = _textbox(s, Inches(0.8), Inches(6.5), Inches(11.733), Inches(0.5))
    _para(tf, "Kolom Kategori, Satuan, Harga Beli, dan Harga Jual disembunyikan "
              "pada slide ini agar teks terbaca. Versi lengkap ada di README.",
          "Calibri", 11, C_MUTED, first=True)

    # ------------------------------------------------------------------
    # 9. TAMPILAN OUTPUT: ANTI STOK MINUS
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Bukti Eksekusi", "Tampilan Output: Anti Stok Minus",
           "Satu transaksi ditolak karena melebihi stok, satu transaksi "
           "diterima karena masih dalam batas.")
    card(s, Inches(0.8), Inches(1.9), Inches(11.733), Inches(4.5),
         bg_color=C_WHITE)
    fit_picture(
        s, os.path.join(root, "docs", "assets", "cli_anti_minus.png"),
        Inches(0.95), Inches(2.0), Inches(11.43), Inches(4.38),
    )
    tf = _textbox(s, Inches(0.8), Inches(6.5), Inches(11.733), Inches(0.5))
    _para(tf, "Perhatikan satuan pada pesan penolakan sudah konsisten: "
              "Rim, bukan unit.", "Calibri", 11, C_MUTED, first=True)

    # ------------------------------------------------------------------
    # 10. SILABUS
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Kesesuaian Kurikulum Akademik",
           "Pemetaan Materi Silabus UBSI (Pertemuan 1 sampai 7)",
           "Setiap fitur Fase 1 dibangun murni untuk membuktikan "
           "penguasaan materi praktikum sebelum UTS.")

    tbl = s.shapes.add_table(
        8, 4, Inches(0.8), Inches(1.95), Inches(11.733), Inches(4.75)
    ).table
    tbl.columns[0].width = Inches(1.2)
    tbl.columns[1].width = Inches(3.2)
    tbl.columns[2].width = Inches(5.1)
    tbl.columns[3].width = Inches(2.233)
    table_header(tbl, ["Pertemuan", "Materi Silabus UBSI",
                       "Implementasi Nyata pada Stokku Desktop", "Berkas Kode"],
                 center_cols={0, 3})
    for i, row in enumerate(SILABUS):
        for j, val in enumerate(row):
            cell = tbl.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if i % 2 == 0 else C_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Consolas" if j in (0, 3) else "Calibri"
            p.font.size = Pt(10)
            p.font.color.rgb = C_NAVY if j == 0 else C_SLATE
            if j in (0, 3):
                p.alignment = PP_ALIGN.CENTER

    # ------------------------------------------------------------------
    # 11. HASIL UJI
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Verifikasi dan Pengujian Kualitas",
           "Hasil Pengujian Otomatis (7 Kasus Uji, 100 Persen Lulus)",
           "Dijalankan lewat progress_p7/test_skenario.py tanpa input manual, "
           "ditambah 15 unit test di folder tests.")

    tbl6 = s.shapes.add_table(
        8, 5, Inches(0.8), Inches(1.95), Inches(11.733), Inches(4.75)
    ).table
    tbl6.columns[0].width = Inches(0.95)
    tbl6.columns[1].width = Inches(3.1)
    tbl6.columns[2].width = Inches(3.5)
    tbl6.columns[3].width = Inches(3.4)
    tbl6.columns[4].width = Inches(0.783)
    table_header(tbl6, ["ID", "Skenario", "Aksi dan Parameter",
                        "Hasil Aktual", "Status"], center_cols={0, 4})
    for i, row in enumerate(HASIL_UJI):
        for j, val in enumerate(row + ("LULUS",)):
            cell = tbl6.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if i % 2 == 0 else C_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Consolas" if j in (0, 4) else "Calibri"
            p.font.size = Pt(10.5)
            if j == 4:
                p.font.bold = True
                p.font.color.rgb = C_GREEN
                p.alignment = PP_ALIGN.CENTER
            else:
                p.font.color.rgb = C_NAVY if j == 0 else C_SLATE
                if j == 0:
                    p.alignment = PP_ALIGN.CENTER

    # ------------------------------------------------------------------
    # 12. FORMULA ASET
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Kalkulasi Bisnis dan Akuntansi Dasar",
           "Formula Perhitungan Aset Modal dan Ambang Batas Stok",
           "Sistem menghitung nilai modal terikat dan memberi indikator "
           "peringatan dini secara otomatis.")

    col_w, col_h, gap = Inches(3.7), Inches(4.9), Inches(0.3)
    top = Inches(1.95)

    tf1 = card(s, Inches(0.8), top, col_w, col_h).text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.3)
    tf1.margin_top = Inches(0.3)
    _para(tf1, "1. NILAI ASET PER PRODUK", "Trebuchet MS", 12, C_NAVY, bold=True,
          after=10, first=True)
    _para(tf1, "Aset_i = Stok_i x Harga_Beli_i", "Consolas", 12, C_TEAL_DARK,
          bold=True, after=10)
    contoh = "\n".join(
        f"{kode}: {stok} x Rp {harga:,} = Rp {stok * harga:,}".replace(",", ".")
        for kode, _, stok, harga in DATA_AWAL_RINGKAS
    )
    _para(tf1,
          "Nilai uang modal usaha yang tertanam pada setiap jenis barang "
          f"fisik di gudang.\n\nData bawaan:\n{contoh}",
          "Calibri", 12, C_SLATE)

    tf2 = card(s, Inches(4.8), top, col_w, col_h).text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = Inches(0.3)
    tf2.margin_top = Inches(0.3)
    _para(tf2, "2. TOTAL ESTIMASI ASET", "Trebuchet MS", 12, C_NAVY, bold=True,
          after=10, first=True)
    _para(tf2, "Total_Aset = \u03a3 (Stok_i x Harga_Beli_i)", "Consolas", 11.5,
          C_TEAL_DARK, bold=True, after=10)
    ringkas = (
        "Teknik akumulator pada perulangan for menghitung total keseluruhan "
        f"aset modal gudang.\n\nSaldo awal:\nTotal produk : {TOTAL_SKU} SKU\n"
        f"Total fisik  : {TOTAL_UNIT} unit\n"
        f"Total aset   : Rp {TOTAL_MODAL:,}".replace(",", ".")
        + "\n\nDihitung otomatis tanpa keterlambatan data."
    )
    _para(tf2, ringkas, "Calibri", 12, C_SLATE)

    tf3 = card(s, Inches(8.8), top, col_w, col_h).text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_right = Inches(0.3)
    tf3.margin_top = Inches(0.3)
    _para(tf3, "3. AMBANG BATAS KRITIS", "Trebuchet MS", 12, C_NAVY, bold=True,
          after=10, first=True)
    _para(tf3, "Stok <= Min_Stok  ->  KRITIS\nStok >  Min_Stok  ->  AMAN",
          "Consolas", 11, C_RED, bold=True, after=10)
    _para(tf3,
          "Peringatan dini otomatis untuk mencegah kelangkaan barang:\n\n"
          "Jika stok fisik menyentuh atau berada di bawah batas minimum, sistem "
          "memberi tag visual KRITIS.\n\nOperator dapat segera membuat pesanan "
          "pengadaan ulang sebelum barang habis total.",
          "Calibri", 12, C_SLATE)

    # ------------------------------------------------------------------
    # 13. DOKUMENTASI
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Dokumentasi Pengerjaan",
           "Bukti Sesi Kerja dan Kolaborasi Tim",
           "Dua sesi kerja terdokumentasi, dari pengembangan mesin inti "
           "hingga integrasi modul, penyusunan deck, dan draf makalah.")

    foto_w = Inches(5.667)
    foto_h = Inches(5.0)
    top_foto = Inches(1.95)

    for i, (path, judul, orang, keterangan) in enumerate(DOKUMENTASI):
        left = Inches(0.8) + i * (foto_w + Inches(0.4))
        card(s, left, top_foto, foto_w, foto_h)
        fit_picture(s, os.path.join(root, path),
                    left + Inches(0.22), top_foto + Inches(0.22),
                    foto_w - Inches(0.44), Inches(3.85))
        tf = _textbox(s, left + Inches(0.25), top_foto + Inches(4.15),
                      foto_w - Inches(0.5), Inches(0.75))
        _para(tf, judul, "Trebuchet MS", 12, C_NAVY, bold=True, after=2, first=True)
        _para(tf, orang, "Calibri", 10.5, C_TEAL_DARK, bold=True, after=2)
        _para(tf, keterangan, "Calibri", 10, C_MUTED)

    # ------------------------------------------------------------------
    # 14. ROADMAP
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Rencana Pengembangan Lanjutan",
           "Roadmap Versi 2.0 (Menuju Final Project UAS)",
           "Dari mesin logika terminal menjadi aplikasi desktop dengan "
           "antarmuka grafis dan basis data permanen.")

    rw, rh, rgap = Inches(2.7), Inches(4.9), Inches(0.3)
    for i, (tag, judul, isi) in enumerate([
        ("TAHAP 01", "P09: Fungsi Modular",
         "Restrukturisasi kode menjadi subrutin terisolasi dengan parameter, "
         "nilai bawaan, dan return bersih."),
        ("TAHAP 02", "P10: Modul dan SQLite",
         "Pemisahan multi berkas, migrasi penyimpanan ke SQLite3 permanen "
         "(stok_gudang.db), dan proteksi try except."),
        ("TAHAP 03", "P11-P12: Desktop GUI",
         "Antarmuka grafis native Tkinter dan ttk.Treeview dengan kartu "
         "ringkasan serta form dialog."),
        ("TAHAP 04", "P13-P16: Makalah dan Demo",
         "Naskah makalah format resmi UBSI, slide final, dan demonstrasi "
         "langsung di laboratorium komputer."),
    ]):
        tf = card(s, Inches(0.8) + i * (rw + rgap), Inches(1.95),
                  rw, rh).text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.35)
        _para(tf, tag, "Arial", 11, C_TEAL, bold=True, after=8, first=True)
        _para(tf, judul, "Trebuchet MS", 13.5, C_NAVY, bold=True, after=12)
        _para(tf, isi, "Calibri", 12.5, C_SLATE)

    # ------------------------------------------------------------------
    # 15. KESIMPULAN
    # ------------------------------------------------------------------
    s = prs.slides.add_slide(blank)
    background(s)
    header(s, "Penutup dan Distribusi Kerja",
           "Kesimpulan Kesiapan Proyek dan Pembagian Tanggung Jawab",
           "Seluruh komponen inti Fase 1 tuntas dan teruji, "
           "siap menghadapi evaluasi dosen.")

    tf_sum = card(s, Inches(0.8), Inches(1.95), Inches(5.6), Inches(4.9)).text_frame
    tf_sum.word_wrap = True
    tf_sum.margin_left = tf_sum.margin_right = Inches(0.3)
    tf_sum.margin_top = Inches(0.3)
    _para(tf_sum, "KESIMPULAN PROGRES FASE 1", "Trebuchet MS", 12, C_NAVY,
          bold=True, after=12, first=True)
    for teks in [
        "1. Kepatuhan Silabus: konsep logika P01 sampai P07 terimplementasi "
        "secara nyata tanpa loncatan materi.",
        "2. Validasi Teruji: 7 skenario uji otomatis dan 15 unit test lulus "
        "tanpa galat, membuktikan keandalan anti stok minus.",
        "3. Dependensi Minimal: hanya pandas untuk Menu 6 analisis tabular; "
        "menu lain berjalan dengan pustaka bawaan Python.",
        "4. Berkas Terbuka: 7 skenario uji, 15 unit test, dan draf makalah "
        "tersedia di repositori publik GitHub.",
    ]:
        _para(tf_sum, teks, "Calibri", 12, C_SLATE, after=12)

    tf_qa = card(s, Inches(6.8), Inches(1.95), Inches(5.733), Inches(4.9),
                 bg_color=C_WHITE).text_frame
    tf_qa.word_wrap = True
    tf_qa.margin_left = tf_qa.margin_right = Inches(0.3)
    tf_qa.margin_top = Inches(0.3)
    _para(tf_qa, "MATRIKS TANGGUNG JAWAB ANGGOTA TIM", "Trebuchet MS", 12,
          C_NAVY, bold=True, after=12, first=True)
    for nama, tugas in [
        ("Yuken Velino (@Curzyori)",
         "Backend logic, validasi anti minus, test runner, integrator menu"),
        ("Mahardika Athaillah (@dikah4300)",
         "Antarmuka CLI, format tabel terminal, desain presentasi"),
        ("Renkyna Aftania Nasution (@renkynatania-dotcom)",
         "Pelaporan tabular Pandas P07, naskah makalah UBSI"),
    ]:
        _para(tf_qa, nama, "Trebuchet MS", 11, C_NAVY, bold=True)
        _para(tf_qa, f"Tanggung jawab: {tugas}", "Calibri", 11.5, C_SLATE, after=10)

    _para(tf_qa, "SESI DISKUSI DAN TANYA JAWAB DIBUKA", "Trebuchet MS", 12,
          C_TEAL_DARK, bold=True, after=4)
    _para(tf_qa,
          "Terima kasih kepada Dosen Pengampu Ali Mustopa, M.Kom atas "
          "bimbingan dan arahan akademiknya.",
          "Calibri", 10.5, C_MUTED)

    # ------------------------------------------------------------------
    # NOMOR SLIDE (mulai slide 2)
    # ------------------------------------------------------------------
    total = len(prs.slides)
    for nomor in range(2, total + 1):
        slide = prs.slides[nomor - 1]
        tf_no = _textbox(slide, Inches(11.9), Inches(7.02), Inches(1.13), Inches(0.32))
        _para(tf_no, f"{nomor} / {total}", "Calibri", 10.5, C_MUTED,
              first=True, align=PP_ALIGN.RIGHT)

    # ------------------------------------------------------------------
    # CATATAN PEMBICARA (PIC dan poin kunci per slide)
    # ------------------------------------------------------------------
    for nomor, (pic, poin) in CATATAN_PEMBICARA.items():
        if nomor - 1 >= len(prs.slides):
            continue
        tf_notes = prs.slides[nomor - 1].notes_slide.notes_text_frame
        tf_notes.text = f"PIC: {pic}"
        for baris in poin:
            para = tf_notes.add_paragraph()
            para.text = f"- {baris}"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"Presentation saved to: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out_file = os.path.join(
        root, "docs", "presentasi", "STOKKU_DESKTOP_PROGRES_P7.pptx"
    )
    create_deck(out_file, root)
