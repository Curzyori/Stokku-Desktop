# Stokku Desktop

> Aplikasi manajemen persediaan dan pencatatan mutasi stok gudang berbasis Python (berjalan secara luring / offline-first).

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite3-green.svg)](https://www.sqlite.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter%2Fttk-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Informasi Akademik

Proyek ini dikembangkan untuk penilaian Ujian Tengah Semester (UTS, P08) dan Tugas Akhir Ujian Akhir Semester (UAS, P11-P16) pada mata kuliah Dasar Pemrograman (Python, Kode: 894):

- Perguruan Tinggi: Universitas Bina Sarana Informatika (UBSI)
- Program Studi / Kelas: Teknik Informatika / 15.1C.30
- Dosen Pengampu: Ali Mustopa, M.Kom (Kode Dosen: AOP)
- Kelompok: 4 (Empat)

### Anggota Tim Pengembang

| No | NIM | Nama Lengkap | Peran Utama |
| :---: | :---: | :--- | :--- |
| 1 | **15260767** | **YUKEN VELINO** | Project Lead, Logika Backend, Validasi & Test Runner |
| 2 | **15260673** | **MAHARDIKA ATHAILLAH** | Tampilan Antarmuka (UI) & Desain Presentasi |
| 3 | **15260847** | **RENKYNA AFTANIA NASUTION** | Modul Analisis Pandas (P7) & Dokumentasi Akademik |

---

## Latar Belakang

Pencatatan persediaan barang pada toko kelontong atau gudang UMKM sering kali masih dilakukan manual pada buku tulis. Cara manual ini menimbulkan beberapa kendala:
- Jumlah stok fisik tidak terpantau sebelum dilakukan penghitungan ulang fisik (stock opname).
- Keterlambatan memesan kembali barang yang sudah habis di rak penyimpanan.
- Selisih stok akibat barang rusak, kedaluwarsa, atau pemakaian sendiri yang terlewat dicatat.
- Kesulitan mengetahui total modal belanja yang masih tersimpan dalam bentuk barang di gudang.

Stokku Desktop dibangun untuk membantu pencatatan barang dan mutasi keluar-masuk secara rapi tanpa membutuhkan koneksi internet atau server eksternal.

---

## Fitur Pokok

1. **Ringkasan Data Persediaan:**
   - Menampilkan total jenis barang (SKU), total unit fisik, estimasi modal belanja barang, dan jumlah barang yang stoknya menipis.
   - Penanda status visual otomatis (`[KRITIS]`) jika stok berada pada atau di bawah batas minimum aman.
2. **Pengelolaan Data Barang (Master Inventory):**
   - Penambahan barang baru dengan validasi kode alfanumerik unik (tidak membedakan huruf besar-kecil).
   - Pembaruan rincian barang (nama, kategori, satuan, harga beli, harga jual, dan batas minimum stok).
   - Penghapusan data barang disertai dialog konfirmasi.
   - Pencarian langsung berdasarkan nama atau kode barang.
3. **Pencatatan Barang Masuk (Restock):**
   - Penambahan stok fisik dari pemasok disertai keterangan asal barang.
4. **Pencatatan Barang Keluar (Pencegahan Stok Minus):**
   - Pengurangan stok untuk penjualan toko, barang rusak, atau kedaluwarsa.
   - Sistem menolak transaksi dan membatalkan perubahan apabila kuantitas keluar melebihi stok yang tersedia.
5. **Riwayat Mutasi:**
   - Catatan runtut waktu atas seluruh arus keluar-masuk barang, mencakup tanggal, kuantitas, sisa stok sebelum dan sesudah, serta keterangan transaksi.
6. **Laporan Data Tabular (Pandas):**
   - Konversi data inventaris ke bentuk `pandas.DataFrame` untuk keperluan analisis persediaan (materi perkuliahan Pertemuan 7).

---

## Lingkungan Pengembangan & Pustaka

- Bahasa Pemrograman: Python 3 (Python 3.8 hingga 3.14)
- Antarmuka Grafis (GUI Fase 2): Tkinter dan `tkinter.ttk` (pustaka standar Python)
- Basis Data (Fase 2): SQLite3 (`sqlite3` pustaka standar Python, berkas lokal `stok_gudang.db`)
- Analisis Data (Fase 1 P07): Pandas (`pandas.DataFrame`)
- Instalasi Pustaka: Hanya modul `pandas` yang dipasang melalui pip untuk materi Pertemuan 7, modul lainnya menggunakan pustaka bawaan Python.

---

## Tahapan Rilis Proyek

### 1. Versi 1.0 (Target Evaluasi UTS Pertemuan 8 | Silabus P01-P07)
- Fokus: Logika dasar persediaan berbasis antarmuka terminal (CLI) dengan struktur data di memori.
- Cakupan Materi: Variabel dan tipe data (P2), string dan operator (P3), percabangan validasi stok (P4), perulangan menu (P5), koleksi list dan tuple (P6), serta analisis DataFrame Pandas (P7).
- Folder Kerja: `progress_p7/`.

### 2. Versi 2.0 (Target Final Project UAS | Silabus P09-P16)
- Fokus: Pengembangan antarmuka desktop menggunakan Tkinter dan penyimpanan data permanen dengan SQLite.
- Cakupan Materi: Fungsi modular (P9), penanganan eksepsi `try...except` dan pembagian multi-berkas (P10), antarmuka Tkinter dan `ttk.Treeview` (P11-P12), penyusunan naskah laporan format UBSI dan slide presentasi (P13-P14), serta demonstrasi program di laboratorium (P15-P16).
- Folder Kerja: `app/` dan `main.py`.

---

## Struktur Direktori

```text
Stokku-Desktop/
├── docs/
│   ├── PRD.md                             # Spesifikasi kebutuhan sistem
│   └── TASK.md                            # Pembagian tugas dan daftar kerja tim
├── progress_p7/                           # Fase 1: Logika memori P1-P7 (Bahan UTS)
│   ├── data_store.py                      # [YUKEN] Struktur data list dan data awal
│   ├── validasi.py                        # [YUKEN] Fungsi validasi input dan keunikan kode
│   ├── engine_stok.py                     # [YUKEN] Perhitungan mutasi dan total aset
│   ├── display_cli.py                     # [MAHARDIKA] Tampilan tabel CLI dan penanda visual
│   ├── laporan_pandas.py                  # [RENKYNA] Analisis DataFrame Pandas (P7)
│   ├── test_skenario.py                   # [YUKEN] Skrip pengujian otomatis 7 kasus uji
│   └── main_p7.py                         # [YUKEN] Menu utama program terminal
├── app/                                   # Fase 2: GUI Tkinter dan SQLite (Bahan UAS)
│   ├── __init__.py
│   ├── database/
│   │   └── db_manager.py                  # [YUKEN] Koneksi dan query SQLite3
│   ├── services/
│   │   ├── stok_service.py                # [YUKEN] Aturan mutasi data dan transaksi
│   │   └── validator.py                   # [YUKEN] Penanganan kesalahan dan validasi input
│   ├── ui/
│   │   ├── main_window.py                 # [MAHARDIKA] Jendela utama Tkinter
│   │   ├── table_view.py                  # [MAHARDIKA] Tabel data ttk.Treeview
│   │   └── dialogs.py                     # [MAHARDIKA] Dialog form tambah dan mutasi
│   └── reports/
│       └── pandas_reporter.py             # [RENKYNA] Modul ekspor dan ringkasan data
├── main.py                                # Titik masuk eksekusi aplikasi desktop
├── LICENSE                                # Berkas lisensi MIT
├── .gitignore                             # Berkas pengecualian Git
└── README.md                              # Dokumentasi utama proyek
```

---

## Petunjuk Menjalankan Program

### Menjalankan Versi CLI (Fase 1, Progres P1-P7)

Jalankan menu utama program:
```bash
python progress_p7/main_p7.py
```

Jalankan pengujian otomatis:
```bash
python progress_p7/test_skenario.py
```

### Menjalankan Versi Desktop GUI (Fase 2, Versi Final UAS)

```bash
python main.py
```

---

## Lisensi

Proyek ini menggunakan lisensi **MIT License**. Rincian lengkap tersedia pada berkas [LICENSE](LICENSE).
