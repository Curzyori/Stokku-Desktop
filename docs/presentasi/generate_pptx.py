import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette (Antislop / Professional Corporate UBSI)
    C_BG = RGBColor(248, 250, 252)        # #F8FAFC Slate 50
    C_WHITE = RGBColor(255, 255, 255)
    C_NAVY = RGBColor(15, 23, 42)          # #0F172A Slate 900
    C_SLATE = RGBColor(51, 65, 85)         # #334155 Slate 700
    C_MUTED = RGBColor(100, 116, 139)      # #64748B Slate 500
    C_TEAL = RGBColor(13, 148, 136)        # #0D9488 Teal 600
    C_TEAL_DARK = RGBColor(15, 118, 110)   # #0F766E Teal 700
    C_CARD_BG = RGBColor(255, 255, 255)
    C_CARD_BORDER = RGBColor(226, 232, 240)# #E2E8F0
    C_RED = RGBColor(190, 18, 60)          # #BE123C Rose 700
    C_GREEN = RGBColor(4, 120, 87)         # #047857 Emerald 700
    C_LIGHT_TEAL = RGBColor(240, 253, 250) # Teal 50
    C_LIGHT_RED = RGBColor(255, 241, 242)  # Rose 50

    def add_background(slide, color=C_BG):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text=None):
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.3))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0)
        tf.vertical_anchor = MSO_ANCHOR.TOP

        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_TEAL
        p_tag.space_after = Pt(4)

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Trebuchet MS"
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY
        p_title.space_after = Pt(4)

        if subtitle_text:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = "Calibri"
            p_sub.font.size = Pt(13)
            p_sub.font.color.rgb = C_SLATE

    def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        card.text_frame.vertical_anchor = MSO_ANCHOR.TOP
        return card

    # =========================================================================
    # SLIDE 1: JUDUL & IDENTITAS AKADEMIK
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1, C_WHITE)

    # Accent decorative top bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_TEAL
    bar.line.fill.background()

    # Left Container (Hero Info)
    left_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(7.5), Inches(5.0))
    tf1 = left_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = Inches(0)

    p_badge = tf1.paragraphs[0]
    p_badge.text = "EVALUASI PROGRES PROYEK PERTEMUAN 8 (UTS)"
    p_badge.font.name = "Arial"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = C_TEAL
    p_badge.space_after = Pt(12)

    p_title = tf1.add_paragraph()
    p_title.text = "STOKKU DESKTOP"
    p_title.font.name = "Trebuchet MS"
    p_title.font.size = Pt(40)
    p_title.font.bold = True
    p_title.font.color.rgb = C_NAVY
    p_title.space_after = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Aplikasi Manajemen Persediaan & Pencatatan Mutasi Stok Gudang UMKM Berbasis Python (Offline-First)"
    p_sub.font.name = "Calibri"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = C_SLATE
    p_sub.space_after = Pt(36)

    p_meta = tf1.add_paragraph()
    p_meta.text = "Mata Kuliah   : Dasar Pemrograman (Kode: 894)\nKelas / Prodi : 15.1C.30 / Teknik Informatika\nInstitusi        : Universitas Bina Sarana Informatika (UBSI)\nDosen            : Ali Mustopa, M.Kom (Kode Dosen: AOP)"
    p_meta.font.name = "Consolas"
    p_meta.font.size = Pt(12.5)
    p_meta.font.color.rgb = C_SLATE

    # Right Container (Team Members Card)
    card_right = add_card(s1, Inches(8.8), Inches(1.3), Inches(3.7), Inches(5.0), bg_color=C_BG, border_color=C_CARD_BORDER)
    tf_team = card_right.text_frame
    tf_team.word_wrap = True
    tf_team.margin_left = tf_team.margin_right = Inches(0.3)
    tf_team.margin_top = Inches(0.4)

    p_th = tf_team.paragraphs[0]
    p_th.text = "KELOMPOK 4"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(14)
    p_th.font.bold = True
    p_th.font.color.rgb = C_NAVY
    p_th.space_after = Pt(16)

    members = [
        ("Yuken Velino", "15260767", "Lead Developer & Backend Logic"),
        ("Mahardika Athaillah", "15260673", "Frontend UI CLI & Presentasi"),
        ("Renkyna Aftania N.", "15260847", "Data Analytics Pandas & Makalah")
    ]
    for name, nim, role in members:
        p_m = tf_team.add_paragraph()
        p_m.text = f"{name}"
        p_m.font.name = "Trebuchet MS"
        p_m.font.size = Pt(12.5)
        p_m.font.bold = True
        p_m.font.color.rgb = C_NAVY

        p_r = tf_team.add_paragraph()
        p_r.text = f"NIM: {nim} • {role}"
        p_r.font.name = "Calibri"
        p_r.font.size = Pt(11)
        p_r.font.color.rgb = C_MUTED
        p_r.space_after = Pt(14)

    # =========================================================================
    # SLIDE 2: LATAR BELAKANG & MASALAH RIIL UMKM
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "Latar Belakang & Analisis Masalah", "Tantangan Pencatatan Persediaan Barang di Toko UMKM",
               "Sistem manual menimbulkan inefisiensi pencatatan stok fisik, rawan selisih, dan ketidakpastian modal.")

    # 4 Issue Cards
    issues = [
        ("1. Ketidakpastian Sisa Fisik",
         "Pemilik toko tidak mengetahui jumlah barang terkini tanpa menghitung ulang fisik (stock opname) yang menyita waktu operasional."),
        ("2. Keterlambatan Pengadaan",
         "Ketiadaan batas ambang minimum membuat pengadaan ulang (restock) terlambat, sehingga potensi transaksi penjualan hilang."),
        ("3. Kebocoran & Selisih Stok",
         "Barang rusak, kedaluwarsa, atau pemakaian internal sering tidak tercatat rapi, mengakibatkan pembukuan tidak cocok dengan saldo fisik."),
        ("4. Kesulitan Menghitung Modal",
         "Sulit menghitung total nilai uang yang mengendap pada stok gudang secara tepat tanpa adanya rekapitulasi nilai modal.")
    ]

    card_w = Inches(2.7)
    card_h = Inches(3.2)
    top_pos = Inches(2.0)
    gap = Inches(0.3)

    for i, (title, desc) in enumerate(issues):
        x = Inches(0.8) + i * (card_w + gap)
        c = add_card(s2, x, top_pos, card_w, card_h)
        tf_c = c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_right = Inches(0.25)
        tf_c.margin_top = Inches(0.3)

        p1 = tf_c.paragraphs[0]
        p1.text = title
        p1.font.name = "Trebuchet MS"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY
        p1.space_after = Pt(10)

        p2 = tf_c.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = C_SLATE

    # Solution Banner at Bottom
    sol_card = add_card(s2, Inches(0.8), Inches(5.6), Inches(11.733), Inches(1.3), bg_color=C_LIGHT_TEAL, border_color=C_TEAL)
    tf_sol = sol_card.text_frame
    tf_sol.word_wrap = True
    tf_sol.margin_left = tf_sol.margin_right = Inches(0.3)
    tf_sol.margin_top = Inches(0.2)

    p_st = tf_sol.paragraphs[0]
    p_st.text = "SOLUSI: STOKKU DESKTOP (OFFLINE-FIRST & ZERO EXTERNAL DEPENDENCY)"
    p_st.font.name = "Arial"
    p_st.font.size = Pt(11.5)
    p_st.font.bold = True
    p_st.font.color.rgb = C_TEAL_DARK
    p_st.space_after = Pt(4)

    p_sd = tf_sol.add_paragraph()
    p_sd.text = "Aplikasi lokal mandiri berbasis Python murni untuk mengelola data master, mutasi restock, transaksi pengeluaran barang dengan validasi anti-stok minus, serta deteksi stok kritis dan perhitungan total aset modal gudang secara instan."
    p_sd.font.name = "Calibri"
    p_sd.font.size = Pt(11)
    p_sd.font.color.rgb = C_NAVY

    # =========================================================================
    # SLIDE 3: PEMETAAN SILABUS UBSI (P01 - P07)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "Kesesuaian Kurikulum Akademik", "Pemetaan Materi Silabus UBSI (Pertemuan 1 s.d. 7)",
               "Setiap fitur pada Fase 1 dibangun murni membuktikan penguasaan materi praktikum sebelum UTS.")

    # Table of Syllabus mapping
    rows = 8
    cols = 4
    table_shape = s3.shapes.add_table(rows, cols, Inches(0.8), Inches(2.0), Inches(11.733), Inches(4.8))
    table = table_shape.table

    table.columns[0].width = Inches(1.2)
    table.columns[1].width = Inches(3.2)
    table.columns[2].width = Inches(5.1)
    table.columns[3].width = Inches(2.233)

    headers = ["Pertemuan", "Materi Silabus UBSI", "Implementasi Nyata pada Stokku Desktop", "Berkas Kode"]
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
        if j in [0, 3]:
            p.alignment = PP_ALIGN.CENTER

    syllabus_data = [
        ("P01", "Tools, Best Practice & PEP 8", "Struktur modul rapi, indentasi 4 spasi konsisten, penamaan variabel jelas", "Seluruh Berkas"),
        ("P02", "Sintaks, Variabel & Tipe Data", "Data barang: str (kode, nama), int (stok, rupiah), bool (status aktivasi)", "data_store.py"),
        ("P03", "String, Format & Operator", "Format Rupiah (Rp {:,.0f}), manipulasi string, operator mutasi (+=, -=, *)", "engine_stok.py"),
        ("P04", "Percabangan (if...elif...else)", "Validasi mutlak anti-stok minus (keluar <= stok) & cek status stok kritis", "validasi.py"),
        ("P05", "Perulangan (while True & for)", "Siklus menu interaktif (while True), iterasi pembacaan data tabel (for)", "main_p7.py"),
        ("P06", "Struktur Data List & Tuple", "List of dicts untuk master barang, list of tuples untuk log riwayat mutasi", "data_store.py"),
        ("P07", "Matrix & Library Pandas", "Representasi data tabular 2D dan konversi inventaris ke pandas.DataFrame", "laporan_pandas.py")
    ]

    for i, row in enumerate(syllabus_data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if i % 2 == 0 else C_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Consolas" if j in [0, 3] else "Calibri"
            p.font.size = Pt(10)
            p.font.color.rgb = C_NAVY if j == 0 else C_SLATE
            if j in [0, 3]:
                p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 4: ARSITEKTUR FILE MODULAR & ALUR MUTASI
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "Arsitektur & Logika Sistem", "Pemisahan Modul Terisolasi & Validasi Mutasi Stok",
               "Arsitektur dirancang modular tanpa tabrakan file antaranggota tim dengan validasi anti-stok minus.")

    # Left Card: Module Structure
    c_arch = add_card(s4, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8))
    tf_arch = c_arch.text_frame
    tf_arch.word_wrap = True
    tf_arch.margin_left = tf_arch.margin_right = Inches(0.3)
    tf_arch.margin_top = Inches(0.3)

    p = tf_arch.paragraphs[0]
    p.text = "STRUKTUR MODUL TERISOLASI (FASE 1)"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_TEAL_DARK
    p.space_after = Pt(12)

    modules_info = [
        ("progress_p7/data_store.py", "Yuken Velino", "Koleksi data in-memory (list of dicts) dan saldo awal."),
        ("progress_p7/validasi.py", "Yuken Velino", "Filter validasi input angka bulat positif dan kode unik."),
        ("progress_p7/engine_stok.py", "Yuken Velino", "Logika mutasi masuk/keluar, rumus aset, penanda kritis."),
        ("progress_p7/display_cli.py", "Mahardika Athaillah", "Format tabel ASCII terminal, lebar kolom proporsional."),
        ("progress_p7/main_p7.py", "Yuken Velino", "Integrator siklus menu interaktif aplikasi CLI.")
    ]

    for fname, author, desc in modules_info:
        p1 = tf_arch.add_paragraph()
        p1.text = f"• {fname}"
        p1.font.name = "Consolas"
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY

        p2 = tf_arch.add_paragraph()
        p2.text = f"  PIC: {author} — {desc}"
        p2.font.name = "Calibri"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_SLATE
        p2.space_after = Pt(6)

    # Right Card: Mutation Logic & Anti-Minus Guard
    c_logic = add_card(s4, Inches(6.8), Inches(2.0), Inches(5.733), Inches(4.8))
    tf_l = c_logic.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = Inches(0.3)
    tf_l.margin_top = Inches(0.3)

    p = tf_l.paragraphs[0]
    p.text = "LOGIKA MUTASI & ATURAN ANTI-STOK MINUS"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(12)

    logic_steps = [
        ("1. Transaksi Restock (Barang Masuk)",
         "Kuantitas masuk harus bilangan bulat positif (> 0). Sistem mengeksekusi penugasan akumulator: stok = stok + kuantitas, kemudian mencatat riwayat ke log_mutasi."),
        ("2. Evaluasi Mutasi Barang Keluar (P04)",
         "Sebelum stok dikurangi, sistem membandingkan kuantitas permintaan dengan stok fisik saat ini:"),
        ("   Kondisi A: kuantitas_keluar > stok_tersedia",
         "   [DITOLAK KERAS] Sistem membatalkan transaksi seketika. Saldo fisik tidak berubah, mengembalikan pesan peringatan: Stok tidak mencukupi."),
        ("   Kondisi B: kuantitas_keluar <= stok_tersedia",
         "   [TRANSAKSI SAH] Sistem mengeksekusi pengurangan: stok = stok - kuantitas, dan membuat baris catatan mutasi KELUAR lengkap dengan alasan.")
    ]

    for title, desc in logic_steps:
        p1 = tf_l.add_paragraph()
        p1.text = title
        p1.font.name = "Trebuchet MS" if "Kondisi" not in title else "Consolas"
        p1.font.size = Pt(11)
        p1.font.bold = True
        if "Kondisi A" in title:
            p1.font.color.rgb = C_RED
        elif "Kondisi B" in title:
            p1.font.color.rgb = C_GREEN
        else:
            p1.font.color.rgb = C_NAVY

        p2 = tf_l.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = C_SLATE
        p2.space_after = Pt(8)

    # =========================================================================
    # SLIDE 5: HASIL PENGUJIAN OTOMATIS (7 KASUS UJI)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Verifikasi & Pengujian Kualitas", "Hasil Pengujian Otomatis (7 Kasus Uji - 100% Lulus)",
               "Verifikasi menyeluruh menggunakan test_skenario.py membuktikan seluruh fungsi bisnis berjalan tanpa galat.")

    # Table of Test Cases
    rows = 8
    cols = 5
    t5_shape = s5.shapes.add_table(rows, cols, Inches(0.8), Inches(2.0), Inches(11.733), Inches(4.8))
    t5 = t5_shape.table

    t5.columns[0].width = Inches(1.0)
    t5.columns[1].width = Inches(2.8)
    t5.columns[2].width = Inches(4.333)
    t5.columns[3].width = Inches(2.2)
    t5.columns[4].width = Inches(1.4)

    t5_headers = ["ID Uji", "Skenario Pengujian", "Aksi & Parameter Pengujian", "Ekspektasi Sistem", "Status"]
    for j, h in enumerate(t5_headers):
        cell = t5.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Trebuchet MS"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE
        if j in [0, 4]:
            p.alignment = PP_ALIGN.CENTER

    tests_data = [
        ("TC-01", "Inisialisasi Data Awal", "Memeriksa list of dicts data barang awal", "4 produk terdata, saldo fisik valid", "100% PASS"),
        ("TC-02", "Pendaftaran Barang Baru", "Input kode ATK03 (Penghapus Pensil)", "Berhasil ditambahkan ke daftar", "100% PASS"),
        ("TC-03", "Pencegahan Kode Duplikat", "Mencoba input kode lama (KRT01)", "Ditolak: Kode barang sudah ada", "100% PASS"),
        ("TC-04", "Transaksi Barang Masuk", "Restock ATK02 sebanyak 15 dus", "Stok fisik bertambah dari 5 -> 20", "100% PASS"),
        ("TC-05", "Validasi Anti-Stok Minus", "Mencoba keluar 50 rim KRT01 (stok 30)", "Dibatalkan: Stok tidak mencukupi", "100% PASS"),
        ("TC-06", "Transaksi Keluar Sah", "Pengeluaran normal 5 pak ATK01", "Stok fisik berkurang dari 20 -> 15", "100% PASS"),
        ("TC-07", "Pemantauan Status Kritis", "Deteksi produk dengan stok <= min_stok", "Status [STOK KRITIS] aktif tepat", "100% PASS")
    ]

    for i, row in enumerate(tests_data):
        for j, val in enumerate(row):
            cell = t5.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if i % 2 == 0 else C_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Consolas" if j in [0, 4] else "Calibri"
            p.font.size = Pt(10)
            if j == 4:
                p.font.bold = True
                p.font.color.rgb = C_GREEN
                p.alignment = PP_ALIGN.CENTER
            else:
                p.font.color.rgb = C_NAVY if j == 0 else C_SLATE
                if j == 0:
                    p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 6: FORMULA MATEMATIS & PEMANTAUAN ASET MODAL
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "Kalkulasi Bisnis & Akuntansi Dasar", "Formula Perhitungan Aset Modal & Ambang Batas Stok",
               "Sistem secara otomatis menghitung nilai modal terikat dan memberikan indikator peringatan dini.")

    # 3 Column Cards
    col_w = Inches(3.7)
    col_h = Inches(4.8)
    top_pos = Inches(2.0)
    gap = Inches(0.3)

    # Card 1: Nilai Aset per Produk
    c1 = add_card(s6, Inches(0.8), top_pos, col_w, col_h)
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "1. NILAI ASET PER PRODUK"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(10)

    p_f = tf.add_paragraph()
    p_f.text = "Aset_i = Stok_i × Harga_Beli_i"
    p_f.font.name = "Consolas"
    p_f.font.size = Pt(12)
    p_f.font.bold = True
    p_f.font.color.rgb = C_TEAL_DARK
    p_f.space_after = Pt(10)

    p_d = tf.add_paragraph()
    p_d.text = "Mencerminkan nilai uang modal usaha yang sedang tertanam pada setiap jenis barang fisik di gudang.\n\nContoh Riil:\n• KRT01: 30 rim × Rp 45.000\n  = Rp 1.350.000\n• ATK02: 20 dus × Rp 24.000\n  = Rp 480.000"
    p_d.font.name = "Calibri"
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = C_SLATE

    # Card 2: Total Aset Gudang
    c2 = add_card(s6, Inches(4.8), top_pos, col_w, col_h)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = Inches(0.3)
    tf2.margin_top = Inches(0.3)
    p = tf2.paragraphs[0]
    p.text = "2. TOTAL ESTIMASI ASET"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(10)

    p_f2 = tf2.add_paragraph()
    p_f2.text = "Total_Aset = Σ (Stok_i × Harga_Beli_i)"
    p_f2.font.name = "Consolas"
    p_f2.font.size = Pt(12)
    p_f2.font.bold = True
    p_f2.font.color.rgb = C_TEAL_DARK
    p_f2.space_after = Pt(10)

    p_d2 = tf2.add_paragraph()
    p_d2.text = "Menggunakan teknik akumulator pada perulangan for untuk menghitung total keseluruhan aset modal gudang.\n\nRingkasan Saldo Awal:\n• Total Produk : 4 SKU\n• Total Fisik   : 350 Unit\n• Total Aset    : Rp 2.800.000\n\nDihitung otomatis tanpa keterlambatan data."
    p_d2.font.name = "Calibri"
    p_d2.font.size = Pt(11)
    p_d2.font.color.rgb = C_SLATE

    # Card 3: Ambang Batas Kritis
    c3 = add_card(s6, Inches(8.8), top_pos, col_w, col_h)
    tf3 = c3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_right = Inches(0.3)
    tf3.margin_top = Inches(0.3)
    p = tf3.paragraphs[0]
    p.text = "3. AMBANG BATAS KRITIS"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(10)

    p_f3 = tf3.add_paragraph()
    p_f3.text = "Stok <= Min_Stok -> [KRITIS]\nStok >  Min_Stok -> [AMAN]"
    p_f3.font.name = "Consolas"
    p_f3.font.size = Pt(11)
    p_f3.font.bold = True
    p_f3.font.color.rgb = C_RED
    p_f3.space_after = Pt(10)

    p_d3 = tf3.add_paragraph()
    p_d3.text = "Peringatan dini otomatis untuk mencegah kelangkaan barang:\n\n• Jika stok fisik menyentuh atau berada di bawah batas minimum (min_stok), sistem memberi tag visual [STOK KRITIS].\n• Membantu operator segera membuat order pengadaan ulang sebelum barang habis total."
    p_d3.font.name = "Calibri"
    p_d3.font.size = Pt(11)
    p_d3.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 7: ROADMAP VERSI 2.0 (MENUJU FINAL UAS P09 - P16)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Rencana Pengembangan Lanjutan", "Roadmap Versi 2.0 (Menuju Final Project UAS)",
               "Transformasi dari mesin logika terminal menjadi aplikasi desktop modern dengan GUI dan basis data permanen.")

    steps = [
        ("P09: Fungsi Modular", "Restrukturisasi kode menjadi subrutin terisolasi (def) dengan parameter formal, default argument, dan return value bersih."),
        ("P10: Modul & SQLite3", "Pemisahan multi-file modular, migrasi penyimpanan ke basis data relasional SQLite3 permanen (stok_gudang.db), dan proteksi try-except."),
        ("P11-P12: Desktop GUI", "Pembangunan antarmuka grafis native menggunakan Tkinter dan ttk.Treeview lengkap dengan dashboard metrik dan form dialog modal."),
        ("P13-P16: Makalah & Demo", "Penyusunan naskah makalah akademik format resmi UBSI, slide presentasi final, dan demonstrasi live di ruang lab komputer.")
    ]

    card_w = Inches(2.7)
    card_h = Inches(4.8)
    top_pos = Inches(2.0)
    gap = Inches(0.3)

    for i, (stitle, sdesc) in enumerate(steps):
        x = Inches(0.8) + i * (card_w + gap)
        c = add_card(s7, x, top_pos, card_w, card_h)
        tf_s = c.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = Inches(0.25)
        tf_s.margin_top = Inches(0.35)

        p_num = tf_s.paragraphs[0]
        p_num.text = f"TAHAP 0{i+1}"
        p_num.font.name = "Arial"
        p_num.font.size = Pt(11)
        p_num.font.bold = True
        p_num.font.color.rgb = C_TEAL
        p_num.space_after = Pt(8)

        p1 = tf_s.add_paragraph()
        p1.text = stitle
        p1.font.name = "Trebuchet MS"
        p1.font.size = Pt(13.5)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY
        p1.space_after = Pt(12)

        p2 = tf_s.add_paragraph()
        p2.text = sdesc
        p2.font.name = "Calibri"
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 8: KESIMPULAN & PEMBAGIAN PERAN
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Penutup & Distribusi Kerja", "Kesimpulan Kesiapan Proyek & Pembagian Tanggung Jawab",
               "Seluruh komponen inti Fase 1 telah tuntas 100% dan teruji siap menghadapi evaluasi dosen.")

    # Left Card: Summary Points
    c_sum = add_card(s8, Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8))
    tf_sum = c_sum.text_frame
    tf_sum.word_wrap = True
    tf_sum.margin_left = tf_sum.margin_right = Inches(0.3)
    tf_sum.margin_top = Inches(0.3)

    p = tf_sum.paragraphs[0]
    p.text = "KESIMPULAN PROGRES FASE 1"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(12)

    conclusions = [
        "1. Kepatuhan Penuh Silabus: Seluruh konsep logika P01 s.d. P07 terimplementasi secara nyata tanpa loncatan materi.",
        "2. Validasi Teruji 100%: Sebanyak 7 skenario uji coba otomatis lulus tanpa galat, membuktikan keandalan anti-stok minus.",
        "3. Zero External Dependency: Program berjalan di Python standar tanpa dependensi library pihak ketiga yang merepotkan saat demo.",
        "4. Kesiapan Evaluasi Dosen: Berkas tanya-jawab teknis (DOSEN-ASK.txt) telah disusun untuk mengantisipasi pertanyaan kurikulum."
    ]
    for c_text in conclusions:
        p_c = tf_sum.add_paragraph()
        p_c.text = c_text
        p_c.font.name = "Calibri"
        p_c.font.size = Pt(11)
        p_c.font.color.rgb = C_SLATE
        p_c.space_after = Pt(10)

    # Right Card: Role Matrix & Q&A
    c_qa = add_card(s8, Inches(6.8), Inches(2.0), Inches(5.733), Inches(4.8), bg_color=C_WHITE)
    tf_qa = c_qa.text_frame
    tf_qa.word_wrap = True
    tf_qa.margin_left = tf_qa.margin_right = Inches(0.3)
    tf_qa.margin_top = Inches(0.3)

    p = tf_qa.paragraphs[0]
    p.text = "MATRIKS TANGGUNG JAWAB ANGGOTA TIM"
    p.font.name = "Trebuchet MS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(12)

    roles = [
        ("Yuken Velino (@Curzyori)", "Backend Logic, Validasi Anti-Minus, Test Runner, Integrator Menu"),
        ("Mahardika Athaillah (@dikah4300)", "Frontend UI CLI, Formatting Tabel ASCII, Desain Presentasi"),
        ("Renkyna Aftania Nasution", "Reporting Tabular Pandas (P07), Penyusunan Naskah Makalah UBSI")
    ]
    for r_name, r_desc in roles:
        p1 = tf_qa.add_paragraph()
        p1.text = f"• {r_name}"
        p1.font.name = "Trebuchet MS"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY

        p2 = tf_qa.add_paragraph()
        p2.text = f"  Tanggung Jawab: {r_desc}"
        p2.font.name = "Calibri"
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = C_SLATE
        p2.space_after = Pt(8)

    p_qa = tf_qa.add_paragraph()
    p_qa.text = "SESI DISKUSI & TANYA JAWAB DIBUKA"
    p_qa.font.name = "Trebuchet MS"
    p_qa.font.size = Pt(12)
    p_qa.font.bold = True
    p_qa.font.color.rgb = C_TEAL_DARK
    p_qa.space_after = Pt(4)

    p_thx = tf_qa.add_paragraph()
    p_thx.text = "Terima kasih kepada Dosen Pengampu Ali Mustopa, M.Kom atas bimbingan dan arahan akademiknya."
    p_thx.font.name = "Calibri"
    p_thx.font.size = Pt(10.5)
    p_thx.font.color.rgb = C_MUTED

    # Ensure output dir exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    out_file = "/home/curzy/workspace/UBSI/Dasar-Pemograman/P1/Stokku-Desktop/docs/presentasi/STOKKU_DESKTOP_PROGRES_P7.pptx"
    create_deck(out_file)
