# Spesifikasi Kebutuhan Perangkat Lunak (PRD)
## Stokku Desktop: Sistem Manajemen Stok Gudang UMKM

- Nama Perangkat Lunak: Stokku Desktop
- Deskripsi: Aplikasi manajemen persediaan dan pencatatan mutasi stok gudang berbasis Python
- Versi: 1.0 (Evaluasi UTS) / 2.0 (Evaluasi UAS)
- Status Dokumen: Disetujui
- Tanggal Pembaruan: 13 November 2026
- Mata Kuliah: Dasar Pemrograman (Kode: 894), 4 SKS
- Program Studi / Kelas: Teknik Informatika / 15.1C.30
- Institusi: Universitas Bina Sarana Informatika (UBSI)
- Dosen Pengampu: Ali Mustopa, M.Kom (Kode Dosen: AOP)
- Identitas Tim Pengembang (Kelompok 4):
  1. 15260767 - YUKEN VELINO [@Curzyori](https://github.com/Curzyori) (Project Lead, Logika Backend, Validasi Data, dan Test Runner)
  2. 15260673 - MAHARDIKA ATHAILLAH [@dikah4300](https://github.com/dikah4300) (Tampilan Antarmuka dan Desain Presentasi)
  3. 15260847 - RENKYNA AFTANIA NASUTION [@renkynatania-dotcom](https://github.com/renkynatania-dotcom) (Modul Laporan Pandas dan Makalah Laporan)

---

## 1. Latar Belakang dan Ruang Lingkup Masalah

Sebagian besar pelaku usaha kecil, seperti toko kelontong atau distributor barang rumahan, masih mencatat arus persediaan barang menggunakan buku tulis manual. Pencatatan manual tersebut menimbulkan sejumlah kendala operasional:
- Ketiadaan informasi sisa stok fisik secara cepat tanpa menghitung ulang fisik barang (stock opname).
- Keterlambatan melakukan pemesanan ulang ke pemasok ketika barang di rak sudah habis.
- Terjadinya selisih pembukuan akibat barang rusak, kedaluwarsa, atau pemakaian internal yang tidak tercatat.
- Ketidakjelasan total nilai modal belanja yang saat ini tersimpan dalam bentuk barang di gudang.

Stokku Desktop dikembangkan sebagai aplikasi komputer yang berjalan mandiri di tingkat lokal tanpa mewajibkan koneksi internet atau server luar. Program ini dirancang sekaligus untuk memenuhi capaian pembelajaran silabus mata kuliah Dasar Pemrograman (Python) di Universitas Bina Sarana Informatika dari Pertemuan 1 hingga Pertemuan 16.

Pada implementasi intinya, aplikasi memanfaatkan pustaka bawaan bahasa Python. Dengan demikian, program dapat langsung dijalankan pada komputer laboratorium kampus maupun perangkat dosen penguji tanpa kesulitan pemasangan paket tambahan. Pustaka eksternal Pandas hanya dipakai pada modul laporan untuk pemenuhan materi praktikum Pertemuan 7.

---

## 2. Tujuan dan Batasan Sistem

### A. Tujuan Proyek
1. Sentralisasi Data Persediaan: Mencatat daftar produk, transaksi barang masuk, dan transaksi barang keluar pada satu sistem terpadu.
2. Pencegahan Stok Negatif: Menolak transaksi pengeluaran barang apabila kuantitas yang diminta melebihi sisa fisik yang ada di gudang.
3. Peringatan Stok Menipis: Mendeteksi serta memberikan penanda visual jika persediaan barang berada pada atau di bawah batas minimum (`stok <= min_stok`).
4. Catatan Mutasi Kronologis: Menyimpan riwayat perubahan barang secara urut waktu lengkap dengan kuantitas, sisa stok, dan keterangan kegiatan.
5. Perhitungan Nilai Modal Barang: Menghitung total unit persediaan dan estimasi nilai modal barang secara otomatis melalui rumus $\sum \text{stok} \times \text{harga beli}$.
6. Portabilitas: Program dapat berjalan pada sistem operasi Windows, Linux, maupun macOS yang telah terpasang Python 3.

### B. Batasan Sistem (Non-Goals)
Fitur-fitur berikut tidak dimasukkan ke dalam ruang lingkup aplikasi demi menjaga kesesuaian dengan silabus perkuliahan:
1. Tidak membutuhkan koneksi internet, sinkronisasi komputasi awan (cloud), maupun sistem multipengguna daring.
2. Tidak mencakup fitur kasir penjualan point-of-sale (POS) kompleks, pembayaran nontunai, atau pencetakan struk belanja melalui printer thermal.
3. Tidak mewajibkan integrasi alat pemindai barcode eksternal atau kamera.
4. Tidak menggunakan kerangka kerja web maupun kerangka kerja grafis pihak ketiga di luar modul bawaan Python.

---

## 3. Persona Pengguna dan Alur Kerja

### A. Pengguna Sistem
- Pemilik Usaha: Memeriksa nilai total modal barang di gudang dan melihat daftar barang yang stoknya menipis untuk segera dipesan kembali.
- Staf / Operator Gudang: Mencatat barang masuk dari pemasok serta mencatat barang keluar saat terjadi penjualan atau pemusnahan barang rusak.

### B. Alur Operasional Utama
1. Pendaftaran Barang Baru: Operator memasukkan kode barang, nama produk, kategori, satuan, harga beli, harga jual, stok awal, dan batas minimum stok aman.
2. Pencatatan Barang Masuk: Operator memilih barang terdaftar, memasukkan kuantitas masuk (harus lebih besar dari 0), serta menuliskan keterangan sumber pasokan. Sistem menambahkan stok dan mencatat mutasi.
3. Pencatatan Barang Keluar: Operator memilih barang dan memasukkan kuantitas keluar.
   - Pemeriksaan Validasi: Apabila kuantitas keluar lebih besar dari stok fisik saat ini, sistem membatalkan transaksi serta memunculkan pesan peringatan bahwa stok tidak mencukupi.
   - Apabila kuantitas keluar valid, sistem memotong stok fisik dan menyimpan catatan mutasi keluar.
4. Pemantauan Riwayat dan Status: Pengguna dapat memeriksa tabel persediaan yang menyorot barang berstatus kritis serta melihat akumulasi nilai modal gudang.

---

## 4. Kebutuhan Fungsional

### Modul 1: Ringkasan Informasi dan Penanda Visual
- **Fase 1 (CLI, sudah berjalan):** Penanda visual status `[KRITIS]` bila stok kurang dari atau sama dengan batas minimum, dan `[AMAN]` bila stok melebihi batas minimum. Penanda ini tampil pada kolom Status di tabel Menu 1.
- **Fase 2 (GUI, belum dibuat):** Kartu ringkasan berisi total jenis barang (SKU), total kuantitas unit, estimasi nilai modal belanja (Rupiah), dan jumlah produk berstatus kritis. Fungsi `tampilkan_ringkasan()` sudah tersedia di `display_cli.py` namun belum dipanggil oleh Menu 1.

### Modul 2: Pengelolaan Data Barang (Master Inventory)
- **Fase 1 (CLI, sudah berjalan):**
  - Tambah Barang: Form 8 kolom dengan pemeriksaan keunikan kode barang (tidak membedakan huruf besar-kecil), validasi alfanumerik, dan validasi bilangan bulat.
  - Tampilan Tabel: Tabel teks berformat dengan garis, lebar kolom proporsional, format Rupiah, dan kolom Status.
  - Pencarian: Fungsi `cari_barang_by_kode()` tersedia di `validasi.py` dan dipakai oleh Menu 3 dan Menu 4 untuk menunjuk produk berdasarkan kode.
- **Fase 2 (GUI, belum dibuat):**
  - Ubah Barang: Memperbarui data nama, kategori, satuan, harga beli, harga jual, dan batas minimum stok.
  - Hapus Barang: Menghapus data barang terpilih dengan dialog konfirmasi.
  - Pencarian langsung: Menyaring baris tabel `ttk.Treeview` berdasarkan kata kunci nama atau kode produk.

### Modul 3: Transaksi Mutasi Barang Masuk (Restock)
- **Fase 1 (CLI, sudah berjalan):** Memilih barang terdaftar berdasarkan kode, memasukkan kuantitas masuk (bilangan bulat minimal 1), dan mengisi keterangan sumber barang (default "Pasokan Pemasok"). Sistem menambah `stok += jumlah` dan mencatat tuple mutasi `MASUK` berisi stok sebelum dan sesudah.

### Modul 4: Transaksi Mutasi Barang Keluar
- **Fase 1 (CLI, sudah berjalan):** Memilih barang berdasarkan kode, memasukkan kuantitas keluar (bilangan bulat minimal 1), dan mengisi keterangan alasan (default "Penjualan Toko"). Bila kuantitas melebihi stok fisik, sistem membatalkan transaksi tanpa mengubah stok dan tanpa menambah log. Bila valid, sistem menjalankan `stok -= jumlah` dan mencatat tuple mutasi `KELUAR`.

### Modul 5: Riwayat Transaksi Mutasi
- **Fase 1 (CLI, sudah berjalan):**
  - Menu 5 menampilkan **seluruh** riwayat mutasi secara kronologis naik (entri terlama di posisi paling atas, transaksi terbaru di paling bawah), memuat nomor, tanggal dan waktu, kode, nama barang, jenis, kuantitas bertanda (`+` untuk MASUK, `-` untuk KELUAR), stok sebelum, stok sesudah, dan keterangan.
  - Penyaringan per jenis mutasi tersedia di dalam Menu 6, sub-menu 4 (semua), 5 (MASUK saja), dan 6 (KELUAR saja).
- **Fase 2 (GUI, belum dibuat):** Tombol penyaring `SEMUA` / `MASUK` / `KELUAR` langsung pada tab riwayat.

### Modul 6: Analisis Data Tabular dengan Pandas
- **Fase 1 (CLI, sudah berjalan, wajib pustaka `pandas`):**
  - Sub-menu 1: Matriks data produk 12 kolom termasuk turunan Nilai Modal, Estimasi Omzet, Potensi Laba, dan Status.
  - Sub-menu 2: Rekapitulasi per kategori memakai `groupby("Kategori")` dengan agregasi `count`, `sum`, dan `mean`.
  - Sub-menu 3: Ringkasan statistik deskriptif memakai `sum`, `idxmax`, dan `idxmin`.
  - Sub-menu 4, 5, 6: Riwayat mutasi lengkap, filter MASUK, dan filter KELUAR.
  - Bila `pandas` belum terpasang, Menu 6 menampilkan instruksi `pip install pandas` dan kembali ke menu utama tanpa crash.

### Modul 7: Skrip Uji Otomatis (Menu 7)
- **Fase 1 (CLI, sudah berjalan):** Menjalankan TC-01 s.d. TC-07 tanpa input manual dan mencetak status lulus per kasus beserta persentase akhir.
- **Perhatian:** Fungsi ini memanggil `reset_data()` di awal eksekusi, sehingga seluruh data yang sudah diinput pengguna dikembalikan ke 3 produk bawaan. Perilaku ini disengaja agar hasil pengujian deterministik.

---

## 5. Aturan Bisnis dan Validasi Data

1. Keunikan Kode Barang: Setiap kode barang wajib unik dan bersifat alfanumerik. Sistem secara otomatis mengubah kode ke huruf kapital.
2. Nilai Bilangan Non-Negatif:
   - Sisa stok fisik bernilai minimal 0 (tidak diperbolehkan negatif).
   - Kuantitas mutasi masuk atau keluar harus bilangan bulat minimal 1.
   - Harga beli dan harga jual bernilai minimal 0.
3. Perhitungan Total Nilai Modal:
   $$\text{Nilai Aset Produk} = \text{Stok Fisik} \times \text{Harga Beli}$$
   $$\text{Total Nilai Modal Gudang} = \sum_{i=1}^{n} (\text{Stok}_i \times \text{Harga Beli}_i)$$
4. Penentuan Status Peringatan:
   $$\text{Status Stok} = \begin{cases} \text{KRITIS}, & \text{jika } \text{Stok Fisik} \le \text{Batas Minimum} \\ \text{AMAN}, & \text{jika } \text{Stok Fisik} > \text{Batas Minimum} \end{cases}$$

---

## 6. Struktur Basis Data (SQLite Schema Fase 2)

Aplikasi menyimpan data pada berkas SQLite lokal bernama `stok_gudang.db`.

```
+--------------------------------+         +---------------------------------+
|            barang              |         |        riwayat_transaksi        |
+--------------------------------+         +---------------------------------+
| id (PK, INTEGER)               |<----+   | id (PK, INTEGER)                |
| kode_barang (TEXT, UNIQUE)     |     |   | barang_id (FK, INTEGER) --------+
| nama_barang (TEXT)             |     |   | kode_barang (TEXT)              |
| kategori (TEXT)                |     +-- | nama_barang (TEXT)              |
| satuan (TEXT)                  |         | jenis_transaksi (TEXT)          |
| harga_beli (INTEGER)           |         | jumlah (INTEGER)                |
| harga_jual (INTEGER)           |         | stok_sebelum (INTEGER)          |
| stok (INTEGER)                 |         | stok_sesudah (INTEGER)          |
| min_stok (INTEGER)             |         | keterangan (TEXT)               |
| updated_at (TEXT)              |         | tanggal (TEXT)                  |
+--------------------------------+         +---------------------------------+
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

## 7. Pembagian Berkas dan Struktur Modul

Agar setiap anggota tim dapat mengerjakan bagiannya secara terpisah tanpa saling menimpa kode pada git:

### A. Struktur Berkas Fase 1 (Evaluasi UTS, Materi P1 sampai P7 | Folder `progress_p7/`)
```text
Stokku-Desktop/
├── docs/
│   ├── PRD.md                             # Dokumen spesifikasi kebutuhan sistem
│   ├── TASK.md                            # Rencana tugas dan matriks penanggung jawab
│   ├── assets/                            # Aset gambar dokumentasi dan preview
│   │   ├── P1_2026-11-13.jpg              # Sesi 1: Yuken dan Mahardika
│   │   ├── P2_2026-11-13.jpg              # Sesi 2: Yuken, Mahardika, Renkyna
│   │   ├── cli_*.png                      # Preview eksekusi Menu 1, 4, dan 7
│   │   └── diagrams/                      # Render PNG seluruh diagram mermaid
│   ├── diagrams/                          # Sumber mermaid (.mmd) per diagram
│   ├── makalah/                           # [RENKYNA] Draf makalah evaluasi UTS
│   └── presentasi/                        # [YUKEN] Deck presentasi UTS (14 slide, .pptx dan .pdf)
├── progress_p7/
│   ├── data_store.py                      # [YUKEN] Struktur data list dictionary dan data awal
│   ├── validasi.py                        # [YUKEN] Validasi input angka, keunikan kode, dan batas stok
│   ├── engine_stok.py                     # [YUKEN] Logika mutasi stok dan kalkulasi nilai modal
│   ├── display_cli.py                     # [MAHARDIKA] Format tabel CLI dan penanda visual status
│   ├── laporan_pandas.py                  # [RENKYNA] Analisis DataFrame Pandas (materi P07)
│   ├── test_skenario.py                   # [YUKEN] Skrip pengujian otomatis 7 kasus uji
│   └── main_p7.py                         # [YUKEN] Titik masuk dan menu utama program terminal
├── tests/
│   ├── test_display_cli.py                # [MAHARDIKA] 9 unit test antarmuka terminal
│   └── test_laporan_pandas.py             # [RENKYNA] 6 unit test analitik Pandas
├── requirements.txt                       # Dependensi eksternal (pandas)
```

> **Status Fase 2: belum dibuat.** Direktori `app/` dan berkas `main.py` belum ada di repositori. Struktur di bawah adalah rencana target.

### B. Struktur Berkas Fase 2 (Evaluasi UAS, Materi P09 sampai P16 | Folder `app/`)
```text
Stokku-Desktop/
├── app/
│   ├── __init__.py
│   ├── database/
│   │   └── db_manager.py                  # [YUKEN] Koneksi dan query SQLite3
│   ├── services/
│   │   ├── stok_service.py                # [YUKEN] Logika transaksi dan perhitungan aset
│   │   └── validator.py                   # [YUKEN] Pemeriksaan input dan proteksi try-except
│   ├── ui/
│   │   ├── main_window.py                 # [MAHARDIKA] Jendela utama Tkinter dan kartu ringkasan
│   │   ├── table_view.py                  # [MAHARDIKA] Komponen ttk.Treeview dan pewarnaan baris
│   │   └── dialogs.py                     # [MAHARDIKA] Form dialog tambah, ubah, dan mutasi
│   └── reports/
│       └── pandas_reporter.py             # [RENKYNA] Modul ekspor dan ringkasan data tabular
├── tests/
│   └── test_suite.py                      # [YUKEN] Pengujian menyeluruh sistem
├── docs/
│   ├── makalah/                           # [RENKYNA] Berkas naskah makalah format resmi UBSI
│   └── presentasi/                        # [YUKEN] Deck presentasi final (.pptx dan .pdf)
├── main.py                                # [YUKEN] Titik masuk eksekusi antarmuka desktop
├── stok_gudang.db                         # Berkas basis data SQLite
└── README.md                              # Panduan penggunaan proyek
```

---

## 8. Pemetaan Silabus Mata Kuliah Dasar Pemrograman UBSI

| Pertemuan | Materi Perkuliahan UBSI | Penerapan pada Kode Program | Berkas Implementasi |
| :---: | :--- | :--- | :--- |
| **P01** | Pengenalan Python dan Lingkungan Kerja | Struktur penulisan rapi, indentasi 4 spasi, penamaan variabel sesuai kaidah PEP 8. | Seluruh berkas |
| **P02** | Sintaks Dasar, Variabel, dan Tipe Data | Variabel kode dan nama (`str`), harga dan stok (`int`), `bool` pada penanda pandas, `dict` untuk produk. | `progress_p7/data_store.py`, `progress_p7/laporan_pandas.py` |
| **P03** | String, Operator, dan Format Angka | Normalisasi input (`.strip()`, `.upper()`, `.isdigit()`), format nominal Rupiah, operator mutasi (`+=`, `-=`). | `progress_p7/validasi.py`, `progress_p7/display_cli.py` |
| **P04** | Percabangan (`if...elif...else`) | Validasi $\text{keluar} \le \text{stok}$, pengecekan status kritis $\text{stok} \le \text{min\_stok}$. | `progress_p7/validasi.py`, `app/services/validator.py` |
| **P05** | Perulangan (`for` dan `while`) | Perulangan `while True` untuk navigasi menu, perulangan `for` untuk pencetakan baris tabel dan hitung aset. | `progress_p7/main_p7.py`, `progress_p7/display_cli.py` |
| **P06** | List dan Tuple | Penampungan daftar produk dalam list, baris riwayat mutasi disimpan dalam bentuk tuple. | `progress_p7/data_store.py`, `progress_p7/engine_stok.py` |
| **P07** | Matriks dan Analisis Data Pandas | `DataFrame` 12 kolom, `groupby` per kategori, agregasi `agg`, `sum`, `idxmax`, `idxmin`, dan filter boolean. | `progress_p7/laporan_pandas.py` |
| **P08** | Evaluasi Progres Proyek (UTS) | Demonstrasi program berbasis Pertemuan 1 sampai 7 di depan dosen kelas sebagai pengganti ujian tertulis UTS. | Berkas di `progress_p7/` |
| **P09** | Fungsi Modular (`def` dan `return`) | Seluruh Fase 1 sudah berbentuk fungsi modular: 8 fungsi di `engine_stok.py`, 5 di `validasi.py`, 8 di `display_cli.py`, 11 di `laporan_pandas.py`, ditambah 2 alias kompatibilitas. | `progress_p7/*.py` |
| **P10** | Modul dan Penanganan Eksepsi | Multi-berkas sudah berjalan (6 modul + 2 test). Eksepsi formal `try...except ValueError` dan `sqlite3.IntegrityError` dijadwalkan pada Fase 2. | `progress_p7/`, target `app/services/validator.py` |
| **P11-P16** | Tugas Akhir, Laporan, dan Presentasi | Makalah akademik dan slide presentasi sudah tersedia; uji coba laboratorium dan presentasi UAS menyusul. | `docs/makalah/`, `docs/presentasi/` |

---

## 9. Penanganan Kesalahan Input

### Fase 1 (CLI, sudah berjalan)

Validasi dilakukan sebelum konversi angka, bukan dengan `try...except ValueError`. Pendekatan ini dipilih karena seluruh input di Fase 1 dibaca sebagai `str` dari `input()`, sehingga pemeriksaan karakter dapat dilakukan eksplisit dan pesan kesalahan bisa lebih spesifik.

1. **Input Karakter pada Kolom Angka:** `validasi_angka_positif()` memeriksa `teks.isdigit()` (dan menangani tanda negatif secara terpisah). Bila bukan bilangan bulat, fungsi mengembalikan `(False, 0, pesan)` dan pemanggil langsung menampilkan peringatan tanpa menghentikan program.
2. **Kuantitas Nol atau Negatif:** Ditolak dengan batas minimum per field. Kuantitas mutasi memakai `min_val=1`, harga dan stok awal memakai `min_val=0`, batas minimum stok memakai `min_val=1`.
3. **Kode Barang Duplikat:** `validasi_kode_unik()` menormalkan input dengan `strip().upper()` lalu membandingkan terhadap seluruh kode terdaftar. Karena perbandingan dilakukan setelah normalisasi, `atk01` dan `ATK01` dianggap sama.
4. **Stok Tidak Cukup:** `validasi_stok_keluar()` menolak transaksi bila `jumlah > stok`. Pada kondisi ini stok tidak diubah dan `log_mutasi` tidak bertambah, sehingga invarian `stok >= 0` selalu terjaga.

### Fase 2 (GUI, belum dibuat)

Protokol `try...except ValueError` baru akan diterapkan pada pembacaan nilai dari widget Tkinter, dan `sqlite3.IntegrityError` akan ditangkap pada operasi `INSERT` untuk menangani benturan kode barang di level basis data.

---

## 10. Rencana Rilis Versi

### A. Versi 1.0 (Evaluasi UTS Pertemuan 8, Silabus P01-P07) - SELESAI
- Fokus: Logika dasar persediaan berbasis antarmuka terminal (CLI) dengan struktur data di memori.
- Cakupan Teknis yang Sudah Terimplementasi:
  - Struktur data memori: `list of dictionary` untuk data barang dan `list of tuple` untuk catatan mutasi.
  - Menu interaktif perulangan `while True` dengan percabangan `if-elif-else` untuk 8 pilihan (0 s.d. 7).
  - Operasi penambahan barang baru dengan validasi keunikan kode, alfanumerik, dan bilangan bulat.
  - Transaksi barang masuk dan transaksi barang keluar dengan proteksi sisa stok (`stok >= 0`).
  - Tabel persediaan dengan penanda status `[KRITIS]` / `[AMAN]`, format Rupiah, dan lebar kolom proporsional.
  - Riwayat mutasi lengkap dengan stok sebelum dan sesudah.
  - Analisis `pandas.DataFrame`: `groupby` kategori, statistik deskriptif, dan filter mutasi.
- Hasil Kerja Versi 1.0 (terverifikasi):
  - `progress_p7/main_p7.py`: Program CLI dengan 8 menu.
  - `progress_p7/test_skenario.py`: 7 kasus uji, seluruhnya lulus.
  - `tests/test_display_cli.py` dan `tests/test_laporan_pandas.py`: 15 unit test, seluruhnya lulus.
  - `docs/makalah/MAKALAH_STOKKU_DESKTOP.md`: draf naskah akademik format UBSI (belum final, naskah lengkap disusun menjelang UAS).
  - `docs/presentasi/STOKKU_DESKTOP_PROGRES_P7.pptx` berisi 14 slide beserta versi PDF, termasuk slide 1 layar kosong, slide 4 sampai 6 diagram dan flowchart, slide 7 sampai 8 tampilan output, dan slide 12 dokumentasi kegiatan.
  - `docs/assets/P1_2026-11-13.jpg` dan `docs/assets/P2_2026-11-13.jpg`: foto dokumentasi dua sesi kerja tim.

### Keterbatasan Versi 1.0

1. Data bersifat in-memory: menutup program mengembalikan data ke 3 produk bawaan.
2. Menu 7 memanggil `reset_data()`, sehingga data pengguna kembali ke kondisi awal setelah pengujian.
3. Menu 1 mencetak tabel saja; kartu ringkasan (`tampilkan_ringkasan`) belum dipanggil dan baru dipakai di Fase 2.
4. Fitur Ubah Barang, Hapus Barang, dan Pencarian langsung belum ada di CLI.
5. Menu 5 menampilkan riwayat kronologis naik; filter jenis mutasi hanya tersedia di Menu 6 sub-menu 4, 5, dan 6.

### B. Versi 2.0 (Target Akhir UAS, Silabus P09-P16)
- Fokus: Pengembangan antarmuka desktop menggunakan Tkinter dan penyimpanan data permanen dengan basis data SQLite.
- Rincian Tahapan:
  1. Fungsi Modular (P09): Pengelompokan logika ke dalam fungsi independen, pembatasan variabel lokal, dan penggunaan nilai kembalian `return`.
  2. Multi-Modul dan Eksepsi (P10): Pemisahan berkas modul (`db_manager.py`, `stok_service.py`, `validator.py`), pemanfaatan modul standar (`sqlite3`, `datetime`), serta penanganan eksepsi bertingkat `try...except`.
  3. Basis Data SQLite Permanen (P10): Penyimpanan berkas `stok_gudang.db` dengan mekanisme transaksi basis data (`commit` dan `rollback`).
  4. Antarmuka Desktop Tkinter (P11-P12): Pembuatan antarmuka visual menggunakan `tkinter` dan `ttk.Treeview`, kartu ringkasan informasi, dan form dialog pop-up.
  5. Penyusunan Makalah dan Slide (P13-P14): Penulisan naskah laporan sesuai format resmi UBSI dan perancangan slide presentasi.
  6. Uji Coba dan Demonstrasi (P15-P16): Pengujian menyeluruh bebas crash dan demonstrasi langsung di hadapan Dosen Pengampu.

---

## 11. Pembagian Tanggung Jawab Anggota Tim

| Nama Anggota | NIM | Akun GitHub | Peran | Rincian Tanggung Jawab |
| :--- | :---: | :---: | :--- | :--- |
| **YUKEN VELINO** | 15260767 | [@Curzyori](https://github.com/Curzyori) | Project Lead, Backend, Validasi, dan Pengujian | - Merancang struktur data, skema basis data SQLite, dan model data.<br>- Menulis logika mutasi barang masuk/keluar serta rumus akumulasi nilai modal.<br>- Menyusun fungsi validasi (kode unik, kuantitas positif, batas stok, dan tipe data).<br>- Mengembangkan dan mengeksekusi skrip pengujian otomatis (test_skenario.py dan test_suite.py). |
| **MAHARDIKA ATHAILLAH** | 15260673 | [@dikah4300](https://github.com/dikah4300) | Tampilan Antarmuka dan Presentasi | - Merancang format tabel CLI (Fase 1) dan tata letak antarmuka Tkinter (Fase 2).<br>- Mengatur penataan kolom Treeview, kartu ringkasan, dan dialog form.<br>- Menyusun slide materi presentasi resmi untuk penilaian kelas. |
| **RENKYNA AFTANIA NASUTION** | 15260847 | [@renkynatania-dotcom](https://github.com/renkynatania-dotcom) | Modul Laporan dan Makalah Laporan | - Mengembangkan modul pelaporan dan rekapitulasi data menggunakan Pandas (P07).<br>- Menyaring data transaksi berdasarkan jenis mutasi.<br>- Menyusun naskah Makalah Laporan Resmi format UBSI (Bab I Pendahuluan, Bab II Pembahasan, Bab III Penutup, dan Daftar Pustaka) serta mendokumentasikan hasil pengujian sistem. |

---

## 12. Kriteria Keberhasilan Program

1. Kestabilan Eksekusi: Program tidak keluar tiba-tiba (crash) saat pengguna salah memasukkan huruf pada kolom angka, memasukkan nilai negatif, atau memasukkan kuantitas keluar yang melebihi stok fisik.
2. Ketepatan Mutasi Stok: Stok bertambah saat barang masuk, berkurang saat barang keluar, dan transaksi pengeluaran otomatis dibatalkan apabila melebihi sisa stok di gudang.
3. Ketepatan Perhitungan Nilai: Akumulasi nilai modal belanja persediaan dihitung tepat sesuai formula $\sum (\text{stok} \times \text{harga beli})$.
4. Penanda Barang Kritis: Barang yang memiliki stok kurang dari atau sama dengan batas minimum (`stok <= min_stok`) terdeteksi dan tertandai secara visual pada tampilan data.
5. Kemudahan Pengoperasian: Program dapat dijalankan langsung dengan perintah Python standar tanpa konfigurasi yang rumit.
