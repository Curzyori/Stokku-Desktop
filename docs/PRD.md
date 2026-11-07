# PRODUCT REQUIREMENT DOCUMENT (PRD)
# STOKKU DESKTOP: SISTEM MANAJEMEN STOK GUDANG UMKM

- **Nama Produk:** Stokku Desktop
- **Subjudul:** *Aplikasi Manajemen Persediaan & Mutasi Stok Gudang UMKM Berbasis Python*
- **Versi Produk:** 1.0 (Rilis Tahap 1 - UTS) / 2.0 (Rilis Tahap 2 - UAS)
- **Status Dokumen:** Final Approved
- **Tanggal:** 29 Oktober 2026
- **Mata Kuliah:** Dasar Pemrograman (Kode: 894) — 4 SKS
- **Program Studi / Kelas:** Teknik Informatika / 15.1C.30
- **Institusi:** Universitas Bina Sarana Informatika (UBSI)
- **Dosen Pengampu:** Ali Mustopa, M.Kom (Kode Dosen: AOP)
- **Identitas Tim Pengembang (Kelompok 4):**
  1. **15260767 — YUKEN VELINO** (Project Lead, Backend Logic, Database & Data Validation)
  2. **15260673 — MAHARDIKA ATHAILLAH** (Frontend UI Layout & Presentation Designer)
  3. **15260847 — RENKYNA AFTANIA NASUTION** (Reporting Module, Data Analytics Pandas & Academic Documentation)
  4. **15260722 — PRISILA HUTAJULU** *(Status: Anggota Sementara / Tentatif — Test Runner & Notulen)*

---

## 1. Ringkasan Eksekutif & Latar Belakang

Sebagian besar pelaku Usaha Mikro, Kecil, dan Menengah (UMKM), seperti toko kelontong, toko alat tulis kantor (ATK), dan distributor barang rumahan, masih mencatat arus persediaan barang secara manual di buku tulis. Kebiasaan ini sering memicu selisih stok fisik, keterlambatan pengadaan ulang (*restock*) ketika barang habis, serta ketidakjelasan estimasi total nilai modal yang tertanam di dalam persediaan gudang.

**Stokku Desktop** dikembangkan sebagai aplikasi desktop lokal mandiri (*offline-first*) yang ringan, cepat, dan mudah dioperasikan. Aplikasi ini dibuat khusus untuk memenuhi seluruh capaian pembelajaran silabus praktikum **Dasar Pemrograman (Python - 894)** di Universitas Bina Sarana Informatika dari Pertemuan 1 hingga Pertemuan 16.

Aplikasi ini menggunakan pustaka standar bahasa Python secara murni (*zero external dependency*), sehingga dijamin dapat dijalankan langsung di komputer praktikum kampus maupun laptop dosen penguji tanpa kendala instalasi paket tambahan.

---

## 2. Tujuan & Batasan Lingkup Proyek

### A. Tujuan Proyek (Goals)
1. **Sentralisasi Data Persediaan:** Mencatat master barang, mutasi barang masuk, dan mutasi barang keluar dalam satu sistem terpadu.
2. **Integritas Anti-Stok Minus:** Menerapkan validasi mutlak agar kuantitas stok barang tidak pernah bernilai negatif dalam situasi apa pun.
3. **Peringatan Dini Stok Kritis (*Low-Stock Alert*):** Mendeteksi dan memberi tanda visual otomatis apabila persediaan barang menyentuh atau berada di bawah ambang batas minimum (`stok <= min_stok`).
4. **Audit Mutasi Kronologis:** Mencatat setiap riwayat keluar-masuk barang lengkap dengan waktu, kuantitas perubahan, sisa stok, dan alasan transaksi.
5. **Kalkulasi Nilai Aset Otomatis:** Menghitung total fisik persediaan dan total estimasi modal aset gudang secara otomatis ($\sum \text{stok} \times \text{harga beli}$).
6. **Portabilitas Penuh:** Dapat langsung dijalankan di sistem operasi Windows, Linux, maupun macOS yang memiliki Python tanpa dependensi rumit.

### B. Batasan Lingkup (Non-Goals)
Fitur-fitur berikut secara sengaja tidak dimasukkan ke dalam ruang lingkup aplikasi demi menjaga fokus pada kompetensi kurikulum dan batas waktu akademik:
1. Tidak memerlukan koneksi internet, sinkronisasi cloud, atau multi-user online.
2. Tidak mencakup sistem kasir POS multi-keranjang, pembayaran digital QRIS/kartu, maupun pencetakan struk printer thermal ESC/POS.
3. Tidak memerlukan integrasi scanner barcode eksternal atau kamera.
4. Tidak menggunakan framework web atau framework GUI berat pihak ketiga (seperti Flet, PyQt, atau Django).

---

## 3. Persona Pengguna & Alur Kerja Sistem

### A. Persona Pengguna
- **Pemilik Toko (Owner):** Memantau total nilai aset modal, menambah produk baru, dan memeriksa daftar barang yang berstatus kritis untuk segera dipesan ulang.
- **Operator Gudang / Staf Toko:** Mencatat barang masuk dari kiriman supplier dan mencatat barang keluar saat terjadi penjualan atau ditemukan barang rusak/kedaluwarsa.

### B. Alur Operasional Utama
1. **Alur Pendaftaran Barang Baru:** Operator memasukkan kode unik, nama produk, kategori, satuan, harga beli, harga jual, stok awal, dan batas minimal stok aman.
2. **Alur Barang Masuk (Restock):** Kiriman barang datang $\rightarrow$ pilih produk $\rightarrow$ masukkan kuantitas masuk ($> 0$) $\rightarrow$ isi keterangan sumber $\rightarrow$ stok fisik bertambah dan log mutasi tercatat.
3. **Alur Barang Keluar (Penjualan / Kerusakan):** Operator memilih barang $\rightarrow$ memasukkan kuantitas keluar.
   - *Kondisi Validasi:* Jika kuantitas keluar $>$ stok fisik saat ini, sistem **membatalkan mutasi** dan memunculkan peringatan bahwa stok tidak mencukupi.
   - Jika kuantitas keluar $\le$ stok saat ini: stok fisik berkurang dan log mutasi keluar tercatat.
4. **Alur Audit & Peringatan:** Setiap saat pengguna dapat melihat tabel barang dengan sorotan khusus untuk produk yang memiliki stok $\le$ batas minimum serta melihat ringkasan total nilai aset rupiah.

---

## 4. Kebutuhan Fungsional Sistem (Functional Requirements)

### Modul 1: Dashboard Ringkasan & Status Visual
- Menampilkan 4 kartu informasi utama: Total Jenis Barang (SKU), Total Kuantitas Fisik Barang, Estimasi Total Nilai Aset Gudang (Rupiah), dan Jumlah Barang Berstatus Kritis.
- Memberikan penanda visual status barang: `[KRITIS / RESTOCK]` jika stok $\le$ batas minimum, dan `[AMAN]` jika stok $>$ batas minimum.

### Modul 2: Master Data Barang (Inventory Management)
- **Tambah Barang:** Form input data barang baru dengan pemeriksaan keunikan kode barang (*case-insensitive*).
- **Ubah Data Barang (Edit):** Memperbarui nama, kategori, satuan, harga beli/jual, dan ambang batas stok.
- **Hapus Data Barang (Delete):** Menghapus data barang dengan konfirmasi dialog peringatan.
- **Pencarian Cepat (Live Search):** Filter tabel secara instan berdasarkan nama produk atau kode barang.
- **Tabel Data Terstruktur:** Penataan kolom rapi menggunakan `ttk.Treeview` lengkap dengan bilah penggulung (*scrollbar*).

### Modul 3: Transaksi Mutasi Barang Masuk (Restock)
- Memilih barang terdaftar, menginput jumlah masuk (harus integer $> 0$), dan mengisi keterangan (misal: "Restock Pabrik", "Kiriman Pemasok").
- Menambahkan stok fisik secara atomik dan membuat satu entri log transaksi baru.

### Modul 4: Transaksi Mutasi Barang Keluar
- Memilih barang terdaftar dan menginput kuantitas keluar (harus integer $> 0$).
- **Validasi Mutlak Anti-Stok Minus:** Sistem menolak mutasi jika kuantitas keluar melebihi stok yang tersedia.
- Mencatat keterangan alasan keluar (misal: "Terjual", "Barang Rusak", "Kedaluwarsa").
- Mengurangkan stok fisik secara atomik dan membuat satu entri log transaksi keluar.

### Modul 5: Log Riwayat Transaksi & Filter
- Menampilkan seluruh log mutasi secara kronologis (*newest first*) yang memuat: tanggal & waktu, kode barang, nama barang, jenis mutasi (`MASUK`/`KELUAR`), jumlah, stok sebelum, stok sesudah, dan keterangan.
- Menyediakan filter tampilan riwayat berdasarkan jenis mutasi (`SEMUA`, `MASUK`, `KELUAR`).

### Modul 6: Analisis Data Tabular (Integrasi Pandas)
- Konversi data inventaris ke objek `pandas.DataFrame` untuk menampilkan tabel data terstruktur dan ringkasan statistik (pemenuhan materi Pertemuan 7).

---

## 5. Aturan Bisnis & Integritas Data (Business Rules)

1. **Keunikan Kode Barang:** Setiap kode barang wajib unik dan alfanumerik (misal: `BRG001`). Sistem otomatis mengonversi ke huruf kapital (*uppercase*).
2. **Integritas Non-Negatif:**
   - Stok fisik $\ge 0$ (stok tidak boleh negatif dalam kondisi apa pun).
   - Kuantitas mutasi masuk atau keluar harus bilangan bulat $\ge 1$.
   - Harga beli $\ge 0$ dan harga jual $\ge 0$.
3. **Rumus Total Aset Gudang:**
   $$\text{Nilai Aset Per Produk} = \text{Stok Fisik} \times \text{Harga Beli}$$
   $$\text{Total Nilai Aset Gudang} = \sum_{i=1}^{n} (\text{Stok}_i \times \text{Harga Beli}_i)$$
4. **Logika Ambang Batas Peringatan:**
   $$\text{Status Stok} = \begin{cases} \text{KRITIS}, & \text{jika } \text{Stok Fisik} \le \text{Batas Minimum} \\ \text{AMAN}, & \text{jika } \text{Stok Fisik} > \text{Batas Minimum} \end{cases}$$

---

## 6. Desain Basis Data Relasional (SQLite Schema)

Aplikasi menggunakan berkas basis data SQLite lokal: `stok_gudang.db`.

```
┌────────────────────────────────┐         ┌─────────────────────────────────┐
│            barang              │         │        riwayat_transaksi        │
├────────────────────────────────┤         ├─────────────────────────────────┤
│ id (PK, INTEGER)               │◄───┐     │ id (PK, INTEGER)                │
│ kode_barang (TEXT, UNIQUE)     │    │     │ barang_id (FK, INTEGER) ────────┘
│ nama_barang (TEXT)             │    │     │ kode_barang (TEXT)              │
│ kategori (TEXT)                │    └──── │ nama_barang (TEXT)              │
│ satuan (TEXT)                  │          │ jenis_transaksi (TEXT)          │
│ harga_beli (INTEGER)           │          │ jumlah (INTEGER)                │
│ harga_jual (INTEGER)           │          │ stok_sebelum (INTEGER)          │
│ stok (INTEGER)                 │          │ stok_sesudah (INTEGER)          │
│ min_stok (INTEGER)             │          │ keterangan (TEXT)               │
│ updated_at (TEXT)              │          │ tanggal (TEXT)                  │
└────────────────────────────────┘         └─────────────────────────────────┘
```

### Skema DDL Tabel
```sql
CREATE TABLE IF NOT EXISTS barang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kode_barang TEXT UNIQUE NOT NULL,
    nama_barang TEXT NOT NULL,
    kategori TEXT NOT NULL,
    satuan TEXT NOT NULL,
    harga_beli INTEGER NOT NULL DEFAULT 0,
    harga_jual INTEGER NOT NULL DEFAULT 0,
    stok INTEGER NOT NULL DEFAULT 0,
    min_stok INTEGER NOT NULL DEFAULT 5,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS riwayat_transaksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    barang_id INTEGER NOT NULL,
    kode_barang TEXT NOT NULL,
    nama_barang TEXT NOT NULL,
    jenis_transaksi TEXT NOT NULL CHECK(jenis_transaksi IN ('MASUK', 'KELUAR')),
    jumlah INTEGER NOT NULL CHECK(jumlah > 0),
    stok_sebelum INTEGER NOT NULL,
    stok_sesudah INTEGER NOT NULL,
    keterangan TEXT,
    tanggal TEXT NOT NULL,
    FOREIGN KEY (barang_id) REFERENCES barang (id) ON DELETE CASCADE
);
```

---

## 7. Arsitektur Berkas Terisolasi (Pencegah Konflik Kerja Tim)

Agar setiap anggota tim (Yuken, Mahardika, Renkyna, Prisila) dapat bekerja secara paralel di file masing-masing tanpa terjadi tabrakan kode (*merge conflicts*), struktur direktori dipecah menjadi modul-modul independen:

### A. Arsitektur Fase 1 (Target Besok - P1 s.d. P7 | Folder `progress_p7/`)
```text
Stokku-Desktop/
├── docs/
│   ├── PRD.md                             # Dokumen PRD Master ini
│   └── TASK.md                            # Rencana kerja & pembagian PIC
├── progress_p7/
│   ├── data_store.py                      # [PIC: YUKEN] Inisialisasi list of dicts & data dummy
│   ├── validasi.py                        # [PIC: YUKEN] Logika validasi input, sanitasi angka & kode unik
│   ├── engine_stok.py                     # [PIC: YUKEN] Logika mutasi masuk/keluar anti-minus & hitung aset
│   ├── display_cli.py                     # [PIC: MAHARDIKA] Formatting tabel CLI, banner, & lebar kolom
│   ├── laporan_pandas.py                  # [PIC: RENKYNA] Konversi DataFrame & rekapitulasi data P7
│   ├── test_skenario.py                   # [PIC: PRISILA] Script otomatis pengujian 7 kasus uji
│   └── main_p7.py                         # [PIC: YUKEN] File penggabung (hanya import dan panggil menu)
```

### B. Arsitektur Fase 2 (Menuju UAS - P09 s.d. P16 | Folder `app/`)
```text
Stokku-Desktop/
├── app/
│   ├── __init__.py
│   ├── database/
│   │   └── db_manager.py                  # [PIC: YUKEN] Koneksi SQLite & query DDL/DML parameterized
│   ├── services/
│   │   ├── stok_service.py                # [PIC: YUKEN] Aturan bisnis mutasi atomik & kalkulasi aset
│   │   └── validator.py                   # [PIC: YUKEN] Guard try-except & validasi input pengguna
│   ├── ui/
│   │   ├── main_window.py                 # [PIC: MAHARDIKA] Window utama Tkinter & dashboard cards
│   │   ├── table_view.py                  # [PIC: MAHARDIKA] Komponen ttk.Treeview & pewarnaan baris
│   │   └── dialogs.py                     # [PIC: MAHARDIKA] Form pop-up tambah, edit, & mutasi barang
│   └── reports/
│       └── pandas_reporter.py             # [PIC: RENKYNA] Modul pelaporan & ekspor data tabular
├── tests/
│   └── test_suite.py                      # [PIC: PRISILA] Black-box testing sebelum live demo
├── docs/
│   └── makalah/                           # [PIC: RENKYNA & TIM] Naskah Makalah Format Resmi UBSI
├── presentation/                          # [PIC: MAHARDIKA] Slide Presentasi PPT Resmi
├── main.py                                # [PIC: YUKEN] Titik masuk eksekusi aplikasi desktop
├── stok_gudang.db                         # Berkas basis data SQLite runtime
└── README.md                              # Panduan pengoperasian
```

---

## 8. Pemetaan Silabus Mata Kuliah Dasar Pemrograman UBSI

| Pertemuan | Materi Silabus UBSI | Implementasi Nyata pada Kode Program | Berkas Implementasi |
| :---: | :--- | :--- | :--- |
| **P01** | Pengenalan Python & IDE | Struktur program rapi, indentasi 4 spasi konsisten, penamaan variabel PEP 8, debugging. | Seluruh berkas |
| **P02** | Sintaks Dasar, Variabel & Tipe Data | Variabel kode (`str`), stok & harga (`int`), dictionary `{}` untuk representasi barang. | `models.py`, `database.py` |
| **P03** | String, Operator & Format Angka | Manipulasi string pencarian (`.lower()`), format angka Rupiah (`Rp {:,.0f}`), operator mutasi (`+=`, `-=`). | `models.py`, `ui.py` |
| **P04** | Percabangan (`if...elif...else`) | Validasi mutlak $\text{keluar} \le \text{stok}$, penentuan status kritis $\text{stok} \le \text{min\_stok}$. | `database.py`, `models.py` |
| **P05** | Perulangan (`for` / `while`) | Perulangan `while` untuk loop aplikasi, perulangan `for` untuk iterasi data tabel dan kalkulasi total aset. | `progress_p7/`, `ui.py` |
| **P06** | List & Tuple | Penampungan sekumpulan data dalam `list`, baris log transaksi mutasi dalam `tuple` immutabel. | `database.py`, `models.py` |
| **P07** | Matrix & Library Pandas | Representasi data tabular 2 dimensi pada Treeview, pemanfaatan `pandas.DataFrame` untuk laporan analisis persediaan. | `progress_p7/`, `ui.py` |
| **P08** | Evaluasi Progres Proyek (UTS) | Demonstrasi program berjalan berbasis P1–P7 di depan dosen kelas sebagai nilai pengganti ujian tertulis UTS. | Berkas Proyek |
| **P09** | Fungsi Modular (`def` & `return`) | Pemecahan sistem ke dalam fungsi-fungsi independen: `tambah_barang()`, `proses_mutasi()`, `hitung_total_aset()`. | `models.py`, `database.py` |
| **P10** | Modul & Exception Handling | Pemisahan multi-file modular, proteksi `try...except ValueError` pada seluruh input angka pengguna untuk mencegah crash. | `main.py`, `ui.py` |
| **P11–P16** | Final Project, Laporan & Presentasi | Penyusunan makalah akademik berformat UBSI, demonstrasi live aplikasi bebas bug, dan presentasi kelompok pengganti UAS. | Berkas Makalah & PPT |

---

## 9. Penanganan Kesalahan & Pencegahan Crash (Error Guarding)

1. **Input Karakter pada Kolom Angka:** Seluruh proses konversi `int()` diproteksi oleh blok `try...except ValueError`. Sistem memunculkan dialog pesan ramah pengguna: *"Input harus berupa bilangan bulat positif!"*.
2. **Kuantitas Negatif atau Nol:** Percabangan logika langsung menolak nilai $\le 0$ dengan pesan *"Jumlah transaksi minimal 1!"*.
3. **Kode Barang Kembar:** Sebelum disimpan, kode barang divalidasi ke database. Duplikasi kode ditangkap melalui `sqlite3.IntegrityError` dengan notifikasi *"Kode barang sudah terdaftar!"*.
4. **Stok Tidak Cukup:** Transaksi pengeluaran barang diuji terlebih dahulu. Jika kuantitas keluar melebihi stok fisik, transaksi langsung dibatalkan sebelum menyentuh perintah `UPDATE` SQL.

---

## 10. Roadmap Rilis Versi (v1.0 & v2.0)

### A. Versi 1.0 (v1.0) — Target Besok / Evaluasi UTS Pertemuan 8 (Silabus P01–P07)
- **Fokus:** Mesin Logika Persediaan (*Core In-Memory Stock Engine*) berbasis CLI interaktif.
- **Cakupan Teknis:**
  - Struktur data memori: `list of dicts` untuk master barang dan `list of tuples` untuk log mutasi.
  - Menu interaktif perulangan `while True` dan pemilihan menu `if-elif-else`.
  - Operasi penambahan barang baru dengan validasi kode unik (`in`).
  - Transaksi restock (barang masuk) dan transaksi pengeluaran barang dengan proteksi stok minus.
  - Tabel ringkasan status stok kritis (`stok <= min_stok`) dan akumulasi total aset modal gudang.
  - Konversi data ke tabel analisis `pandas.DataFrame`.
- **Deliverables v1.0:**
  - `progress_p7/main_stokku_p7.py`: Program CLI mandiri yang langsung bisa dijalankan.
  - `progress_p7/demo_skenario.py`: Script otomatis untuk membuktikan 7 kasus uji.
  - Draf Bab II Makalah Progres untuk sesi evaluasi Pertemuan 8 di hadapan Dosen Pengampu (Ali Mustopa, M.Kom).

---

### B. Versi 2.0 (v2.0) — Final Project Menuju UAS (Silabus P09–P16)
- **Fokus:** Transformasi Penuh ke Aplikasi Desktop Native Modern dengan GUI Tkinter dan Database SQLite Permanen.
- **Rincian Tahapan:**
  1. **Fungsi Modular & Subrutin (Slide 09):** Refactoring kode menjadi fungsi-fungsi kecil terisolasi (`def`), parameter formal, return value, dan pemisahan local vs global scope.
  2. **Multi-Modul & Proteksi Try-Except (Slide 10):** Pemisahan file modular (`database.py`, `models.py`, `ui.py`), pemanfaatan library standar (`sqlite3`, `datetime`, `os`, `sys`), serta penanganan eksepsi bertingkat `try...except ValueError` dan `raise`.
  3. **Basis Data SQLite Permanen (Slide 10 & Praktikum):** Migrasi ke basis data berkas permanen `stok_gudang.db` dengan transaksi atomik (`commit`/`rollback`).
  4. **Antarmuka Desktop Native Tkinter (Slide 11–12):** Pembangunan antarmuka GUI modern menggunakan `tkinter` dan `ttk.Treeview`, dashboard visual warna stok kritis, serta dialog form modal pop-up.
  5. **Penyusunan Makalah & Slide PPT (Slide 13–14):** Penulisan naskah makalah ilmiah format resmi UBSI (Bab I s.d. Bab III, daftar pustaka, lampiran running program) dan perancangan slide presentasi PowerPoint.
  6. **Pengujian Mutlak & Live Demo (Slide 15–16):** Uji coba menyeluruh bebas crash dan simulasi demonstrasi langsung di lab komputer di hadapan Dosen Pengampu (Ali Mustopa, M.Kom - AOP).

---

## 11. Pembagian Tanggung Jawab Tim (Kelompok 4)

| Nama Anggota | NIM | Peran Utama | Rincian Tanggung Jawab Nyata |
| :--- | :---: | :--- | :--- |
| **YUKEN VELINO** | 15260767 | Project Lead, Backend & Validation | - Merancang arsitektur data, skema basis data SQLite, dan model data.<br>- Mengembangkan logika mutasi barang masuk/keluar serta formula total aset.<br>- Mengembangkan seluruh fungsi validasi data (kode unik, kuantitas $>0$, validasi mutlak anti-stok minus, dan sanitasi tipe data). |
| **MAHARDIKA ATHAILLAH** | 15260673 | Frontend UI & Desainer Presentasi | - Merancang format estetika tabel CLI (Fase 1) dan layout GUI Tkinter (Fase 2).<br>- Mengatur penataan kolom Treeview, kartu dashboard, dan dialog pop-up.<br>- Menyusun slide presentasi PowerPoint resmi untuk evaluasi kelas. |
| **RENKYNA AFTANIA NASUTION** | 15260847 | Reporting Pandas & Makalah Akademik | - Mengembangkan modul pelaporan dan rekapitulasi data tabular menggunakan Pandas (P07).<br>- Menyaring data transaksi berdasarkan periode dan jenis mutasi.<br>- Menyusun naskah Makalah Laporan Resmi format UBSI (Bab I Pendahuluan, Bab II Pembahasan/Logika Program, Bab III Penutup, Daftar Pustaka). |
| **PRISILA HUTAJULU** *(Tentatif)* | 15260722 | Test Runner & Notulen Pengujian | - Menjalankan skrip uji coba otomatis 7 skenario (TC-01 s.d. TC-07) dan mencatat log hasil pengujian.<br>- Menguji skenario batas input salah/ekstrem untuk memastikan sistem bebas crash.<br>- Membantu dokumentasi tangkapan layar dan notulensi revisi dosen. |

---

## 12. Kriteria Penerimaan Proyek (Acceptance Criteria)

1. **Bebas Crash (Zero Unhandled Exception):** Aplikasi tidak boleh keluar tiba-tiba saat pengguna salah memasukkan huruf pada kolom angka, menginput nilai negatif, atau mencoba mengeluarkan barang melebihi stok.
2. **Kebenaran Mutasi Stok:** Stok bertambah saat barang masuk, berkurang saat barang keluar, dan mutasi keluar selalu dibatalkan jika melebihi stok yang ada.
3. **Kesesuaian Matematis:** Perhitungan total aset modal gudang akurat sesuai rumus $\sum (\text{stok} \times \text{harga beli})$.
4. **Deteksi Visual Stok Menipis:** Seluruh barang yang memiliki $\text{stok} \le \text{min\_stok}$ terdeteksi dan tertandai secara visual di antarmuka.
5. **Kemudahan Menjalankan Program:** Program dapat dijalankan secara langsung hanya dengan perintah `python main.py` menggunakan Python standar tanpa instalasi dependensi luar.
