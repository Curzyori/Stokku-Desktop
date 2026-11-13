# MAKALAH TUGAS PROYEK DASAR PEMROGRAMAN (KODE: 894)

> **Status berkas: DRAF.**
> Naskah ini belum final. Bab I dan Bab II masih berisi materi progres UTS Pertemuan 1 sampai 7.
> Bab III, daftar pustaka, dan lampiran akan dilengkapi menjelang UAS (P13 dan P14),
> termasuk penambahan bab untuk basis data SQLite dan antarmuka Tkinter.

---

## RANCANG BANGUN APLIKASI MANAJEMEN PERSEDIAAN GUDANG UMKM BERBASIS PYTHON (STOKKU DESKTOP)

---

**Diajukan untuk Memenuhi Penilaian Ujian Tengah Semester (UTS) dan Ujian Akhir Semester (UAS)**  
**Mata Kuliah: Dasar Pemrograman (894) - 4 SKS**  
**Program Studi: Teknik Informatika**  
**Fakultas Teknologi Informasi - Universitas Bina Sarana Informatika**

---

### Disusun Oleh: KELOMPOK 4 (KELAS 15.1C.30)

| No | NIM | Nama Mahasiswa | Peran & Tanggung Jawab |
| :---: | :---: | :--- | :--- |
| 1. | **15260767** | **YUKEN VELINO** | Project Lead, Backend Logic, Validasi & Test Runner |
| 2. | **15260673** | **MAHARDIKA ATHAILLAH** | User Interface (CLI/GUI) & Desain Presentasi |
| 3. | **15260847** | **RENKYNA AFTANIA NASUTION** | Modul Analisis Pandas (P7) & Penyusunan Makalah |

**Dosen Pengampu:**  
**Ali Mustopa, M.Kom** (Kode Dosen: AOP)

**UNIVERSITAS BINA SARANA INFORMATIKA**  
**JAKARTA**  
**2026**

---

## KATA PENGANTAR

Puji syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya, sehingga kami dapat menyelesaikan makalah tugas proyek mata kuliah **Dasar Pemrograman (Kode: 894)** yang berjudul **"Rancang Bangun Aplikasi Manajemen Persediaan Gudang UMKM Berbasis Python (Stokku Desktop)"** tepat pada waktunya.

Makalah dan aplikasi ini dirancang sebagai implementasi konkret dari capaian pembelajaran silabus perkuliahan Dasar Pemrograman di Universitas Bina Sarana Informatika (UBSI), khususnya materi Pertemuan 1 hingga Pertemuan 7 untuk evaluasi Ujian Tengah Semester (UTS), serta fondasi modular menuju Ujian Akhir Semester (UAS). Proyek ini berfokus pada digitalisasi pencatatan stok fisik, mitigasi kesalahan pembukuan manual, pencegahan stok minus (*anti-stok minus*), serta pelaporan analisis data persediaan berbasis pustaka Pandas.

Dalam proses penyusunan makalah dan pengembangan aplikasi ini, kami menyampaikan ucapan terima kasih yang sebesar-besarnya kepada:
1. Bapak **Ali Mustopa, M.Kom (AOP)** selaku Dosen Pengampu mata kuliah Dasar Pemrograman kelas 15.1C.30 yang senantiasa membimbing, mengarahkan, dan memberikan wawasan keilmuan pemrograman kepada kami.
2. Rekan-rekan mahasiswa kelas **15.1C.30 Program Studi Teknik Informatika UBSI** atas kerja sama, diskusi, dan kebersamaan yang terjalin selama perkuliahan.
3. Orang tua dan keluarga tercinta yang senantiasa memberikan doa, motivasi, dan dukungan moral maupun materiil.

Kami menyadari sepenuhnya bahwa makalah ini masih memiliki ruang penyempurnaan. Oleh karena itu, kami mengharapkan kritik dan saran yang membangun dari Dosen Pengampu dan pembaca demi kesempurnaan pengembangan sistem ini pada fase berikutnya.

Jakarta, 11 November 2026  
**Tim Penyusun (Kelompok 4)**

---

## DAFTAR ISI

- **HALAMAN JUDUL**
- **KATA PENGANTAR**
- **DAFTAR ISI**
- **BAB I: PENDAHULUAN**
  - 1.1 Latar Belakang Masalah
  - 1.2 Maksud dan Tujuan
  - 1.3 Ruang Lingkup dan Batasan Masalah
  - 1.4 Metode Pengembangan Perangkat Lunak
- **BAB II: PEMBAHASAN**
  - 2.1 Analisis Kebutuhan Sistem (*Software Requirements*)
  - 2.2 Perancangan Struktur Data dan Arsitektur Logika
  - 2.3 Pemetaan Implementasi Terhadap Silabus Perkuliahan UBSI (P01 - P07)
  - 2.4 Modul Analisis Data Tabular Berbasis Pandas (Pertemuan 7)
  - 2.5 Hasil Pengujian Sistem dan Verifikasi Kasus Uji (TC-01 s.d. TC-07)
  - 2.6 Desain Transisi Menuju Fase 2 (SQLite & GUI Tkinter)
- **BAB III: PENUTUP**
  - 3.1 Kesimpulan
  - 3.2 Saran Pengembangan
- **DAFTAR PUSTAKA**
- **LAMPIRAN**
  - Lampiran 1: Cuplikan Kode Sumber Modul Inti
  - Lampiran 2: Log Eksekusi Pengujian Otomatis

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang Masalah
Usaha Mikro, Kecil, dan Menengah (UMKM) merupakan pilar penggerak ekonomi nasional yang mendominasi aktivitas perdagangan di Indonesia. Kendati demikian, sebagian besar pelaku UMKM, seperti toko kelontong, kios alat tulis kantor (ATK), dan distributor skala rumahan, masih mengandalkan sistem pencatatan manual berbasis buku fisik (*paper-based inventory log*) untuk mencatat arus keluar masuk barang.

Pola pencatatan konvensional tersebut menimbulkan berbagai masalah operasional yang merugikan, antara lain:
1. **Ketiadaan Visibilitas Stok Riil:** Pemilik usaha tidak dapat mengetahui sisa persediaan fisik secara akurat tanpa melakukan penghitungan fisik manual (*stock opname*) yang menyita waktu.
2. **Keterlambatan Pengadaan Kembali (*Stockout*):** Sering terjadi kehabisan barang di rak penjualan karena tidak adanya mekanisme peringatan dini saat stok telah mencapai batas minimum aman.
3. **Penyusutan dan Selisih Stok yang Tidak Terlacak:** Arus keluar barang akibat kerusakan fisik, kedaluwarsa, atau pemakaian internal sering kali luput dicatat sehingga menimbulkan ketidakcocokan saldo modal.
4. **Ketidakpastian Nilai Aset Modal:** Pelaku usaha kesulitan menghitung secara agregat berapa nilai modal belanja yang saat ini tertahan dalam bentuk persediaan barang di gudang.

Untuk menjawab permasalahan tersebut, dirancanglah **Stokku Desktop**, sebuah aplikasi manajemen persediaan dan pencatatan mutasi barang berbasis bahasa pemrograman Python. Sistem ini dirancang dengan prinsip *offline-first* (beroperasi mandiri tanpa ketergantungan koneksi internet), berkohesi tinggi, dan mengutamakan stabilitas eksekusi dengan validasi input yang ketat.

### 1.2 Maksud dan Tujuan
Maksud dan tujuan dari penyusunan makalah serta rancang bangun aplikasi Stokku Desktop adalah:
1. **Memenuhi Capaian Akademik:** Memenuhi tugas proyek mata kuliah Dasar Pemrograman (Kode: 894) di Universitas Bina Sarana Informatika untuk evaluasi Ujian Tengah Semester (UTS, P08) dan Ujian Akhir Semester (UAS, P16).
2. **Sentralisasi Data Persediaan:** Mengintegrasikan pencatatan master produk, saldo barang masuk, dan mutasi barang keluar dalam satu platform terpadu.
3. **Penerapan Proteksi Anti-Stok Minus:** Mengimplementasikan logika kondisional yang menolak transaksi pengeluaran secara otomatis jika kuantitas yang diminta melebihi saldo fisik riil di gudang.
4. **Pemberian Indikator Stok Kritis Otomatis:** Memberikan penanda visual instan `[KRITIS]` pada tabel terminal apabila kuantitas stok berada pada atau di bawah batas minimum (`stok <= min_stok`).
5. **Kalkulasi Nilai Aset Modal:** Menghitung akumulasi total unit fisik dan estimasi nilai kapitalisasi modal barang secara terotomasi dengan rumus matematis $\sum (\text{stok} \times \text{harga beli})$.
6. **Eksplorasi Analisis Tabular Pandas:** Menerapkan pustaka Pandas untuk menyusun analisis agregasi data dua dimensi, pengelompokan kategori (*groupby*), dan penyaringan riwayat transaksi (pemenuhan silabus P07).

### 1.3 Ruang Lingkup dan Batasan Masalah
Agar penelitian dan pengembangan perangkat lunak tetap terfokus dan selaras dengan batasan akademik perkuliahan semester 1, ruang lingkup aplikasi dibatasi sebagai berikut:
1. **Fase 1 (UTS - Pertemuan 1 s.d. 7):**
   - Berjalan pada antarmuka baris perintah (*Command Line Interface* / CLI).
   - Menggunakan struktur data memori (*in-memory*) berupa *list of dictionaries* untuk master barang dan *list of tuples* untuk log mutasi.
   - Pustaka eksternal dibatasi hanya pada `pandas` untuk kebutuhan analisis statistik data tabular pertemuan 7.
2. **Fase 2 (UAS - Pertemuan 9 s.d. 16):**
   - Pengembangan antarmuka desktop berbasis grafis (*Graphical User Interface* / GUI) menggunakan pustaka bawaan `tkinter` dan komponen `ttk.Treeview`.
   - Penyimpanan data permanen berbasis basis data relasional `sqlite3` lokal (`stok_gudang.db`).
3. **Batasan Sistem (*Non-Goals*):**
   - Tidak mencakup sistem kasir Point of Sale (POS) kompleks, transaksi pembayaran tunai/nontunai, atau pencetakan struk termal.
   - Tidak memerlukan arsitektur jaringan *client-server*, sinkronisasi komputasi awan (*cloud*), maupun pemindai kode batang eksternal (*barcode scanner*).

### 1.4 Metode Pengembangan Perangkat Lunak
Pengembangan aplikasi Stokku Desktop menerapkan pendekatan bertahap berbasis modul (*modular development*) yang dipadukan dengan siklus *Test-Driven Development* (TDD):
1. **Analisis Kebutuhan:** Merumuskan dokumen spesifikasi (*Product Requirement Document* / PRD) dan pembagian matriks tanggung jawab (*Task Matrix*).
2. **Perancangan Modul Terisolasi:** Membagi kode sumber menjadi modul-modul independen untuk mencegah konflik penggabungan kode (*zero merge conflicts*) antaranggota tim:
   - Modul Penyimpanan Memori: `progress_p7/data_store.py` (PIC: Yuken Velino)
   - Modul Validasi Input & Kode: `progress_p7/validasi.py` (PIC: Yuken Velino)
   - Modul Mesin Logika Stok & Aset: `progress_p7/engine_stok.py` (PIC: Yuken Velino)
   - Modul Antarmuka Teks CLI: `progress_p7/display_cli.py` (PIC: Mahardika Athaillah)
   - Modul Analisis Pandas: `progress_p7/laporan_pandas.py` (PIC: Renkyna Aftania Nasution)
   - Modul Pengujian Otomatis: `progress_p7/test_skenario.py` (PIC: Yuken Velino)
   - Modul Titik Masuk Utama: `progress_p7/main_p7.py` (Integrator Sistem)
3. **Pengujian Verifikasi Otomatis:** Menjalankan 7 skenario pengujian transaksi (TC-01 hingga TC-07) untuk memastikan keandalan logika tanpa intervensi input manual.

---

## BAB II: PEMBAHASAN

### 2.1 Analisis Kebutuhan Sistem
Aplikasi Stokku Desktop dirancang dengan berpegang pada 5 aturan bisnis (*business rules*) fundamental:
1. **Keunikan Kode Barang:** Setiap barang wajib memiliki identitas kode alfanumerik yang unik dan bersifat tidak peka huruf besar-kecil (*case-insensitive*). Sistem secara otomatis mengonversi kode masukan ke huruf kapital (misal: `atk01` menjadi `ATK01`).
2. **Validitas Nilai Angka Non-Negatif:**
   - Kuantitas stok awal, harga beli modal, dan harga jual bernilai minimal 0 (bilangan bulat).
   - Kuantitas transaksi barang masuk atau keluar wajib bernilai minimal 1.
3. **Proteksi Anti-Stok Minus:**
   Saat transaksi barang keluar diproses, sistem membandingkan kuantitas keluar ($Q_{\text{keluar}}$) dengan stok persediaan fisik saat ini ($S_{\text{saat\_ini}}$):
   $$\text{Validasi Mutasi Keluar} = \begin{cases} \text{Diterima}, & \text{jika } Q_{\text{keluar}} \le S_{\text{saat\_ini}} \\ \text{Ditolak (Batal)}, & \text{jika } Q_{\text{keluar}} > S_{\text{saat\_ini}} \end{cases}$$
4. **Perhitungan Nilai Modal Barang:**
   Total nilai kapitalisasi barang gudang dihitung secara kumulatif:
   $$\text{Nilai Aset Produk}_i = \text{Stok}_i \times \text{Harga Beli}_i$$
   $$\text{Total Nilai Modal Gudang} = \sum_{i=1}^{n} (\text{Stok}_i \times \text{Harga Beli}_i)$$
5. **Penentuan Indikator Visual Status Stok:**
   $$\text{Status Stok} = \begin{cases} \text{[KRITIS]}, & \text{jika } \text{Stok Fisik} \le \text{Batas Minimum (min\_stok)} \\ \text{[AMAN]}, & \text{jika } \text{Stok Fisik} > \text{Batas Minimum (min\_stok)} \end{cases}$$

---

### 2.2 Perancangan Struktur Data dan Arsitektur Logika
Pada implementasi Fase 1 (Evaluasi UTS), sistem menggunakan struktur data bawaan Python di memori:
1. **Master Data Barang (`daftar_barang`):**
   Disimpan dalam format *list of dictionaries* yang fleksibel dan mudah diiterasi:
   ```python
   {
       "kode": "ATK01",
       "nama": "Buku Tulis Kiky 38 Lembar",
       "kategori": "ATK",
       "satuan": "Pcs",
       "harga_beli": 3500,
       "harga_jual": 5000,
       "stok": 15,
       "min_stok": 5
   }
   ```
2. **Catatan Mutasi Transaksi (`log_mutasi`):**
   Disimpan dalam format *list of tuples* dengan sifat *immutable* untuk menjaga keaslian jejak audit:
   ```python
   (waktu, kode, nama, jenis, kuantitas, stok_sebelum, stok_sesudah, keterangan)
   ```

---

### 2.3 Pemetaan Implementasi Terhadap Silabus Perkuliahan UBSI
Aplikasi Stokku Desktop dibangun dengan merefleksikan seluruh materi perkuliahan Dasar Pemrograman dari Pertemuan 1 hingga Pertemuan 7:

| Pertemuan | Materi Perkuliahan UBSI | Implementasi Konkret pada Kode Stokku Desktop | Lokasi Berkas |
| :---: | :--- | :--- | :--- |
| **P01** | Pengenalan Pemrograman Python | Penataan berkas bersih, penulisan modular, dokumentasi *docstring*, serta kepatuhan standar PEP 8. | Seluruh berkas |
| **P02** | Sintaks Dasar, Variabel, dan Tipe Data | Tipe data `str` untuk teks nama dan kode, `int` untuk kuantitas stok dan nominal Rupiah, serta `dict` untuk merepresentasikan entitas barang. | `data_store.py` |
| **P03** | String, Operator, dan Format Angka | Manipulasi string (`.upper()`, `.strip()`), format uang Rupiah (`format_rupiah`), dan operator aritmatika (`+=`, `-=`, `*`). | `display_cli.py`, `engine_stok.py` |
| **P04** | Percabangan Logika (`if...elif...else`) | Evaluasi syarat keunikan kode barang, validasi pencegah stok minus ($Q \le S$), serta evaluasi status kritis stok. | `validasi.py`, `engine_stok.py` |
| **P05** | Perulangan (`while` dan `for`) | Navigasi menu utama dengan perulangan `while True`, iterasi pencetakan baris tabel, dan kalkulasi akumulasi total modal. | `main_p7.py`, `display_cli.py` |
| **P06** | List dan Tuple | Penggunaan `list` sebagai kontainer dinamis data produk dan `tuple` sebagai rekaman kronologis transaksi mutasi. | `data_store.py`, `engine_stok.py` |
| **P07** | Matriks dan Analisis Data Pandas | Transformasi matriks data dua dimensi menjadi objek `pandas.DataFrame`, operasi `groupby()` kategori, dan filtering data. | `laporan_pandas.py` |

---

### 2.4 Modul Analisis Data Tabular Berbasis Pandas (Pertemuan 7)
Modul `progress_p7/laporan_pandas.py` dirancang secara khusus oleh **Renkyna Aftania Nasution (15260847)** guna memenuhi capaian silabus Pertemuan 7 mengenai manipulasi data tabular dua dimensi dan agregasi statistik.

Fitur-fitur utama pada modul ini meliputi:
1. **Konversi Struktur Data ke `pandas.DataFrame` (`buat_dataframe_barang`):**
   Mengubah kumpulan dictionary inventaris menjadi DataFrame dengan menyisipkan kolom terhitung secara otomatis:
   - `Nilai Modal` = $\text{Stok} \times \text{Harga Beli}$
   - `Estimasi Omzet` = $\text{Stok} \times \text{Harga Jual}$
   - `Potensi Laba` = $(\text{Harga Jual} - \text{Harga Beli}) \times \text{Stok}$
   - `Status` = Evaluasi bersyarat `KRITIS` atau `AMAN`.
2. **Agregasi Kategori Menggunakan `groupby()` (`rekapitulasi_kategori`):**
   Meringkas data persediaan per kategori untuk menghitung jumlah ragam produk (`count`), total kuantitas unit (`sum`), total akumulasi modal (`sum`), dan rata-rata harga beli modal (`mean`).
3. **Penyaringan Log Mutasi Berdasarkan Kriteria Transaksi (`filter_mutasi_berdasarkan_jenis`):**
   Memungkinkan pengguna menyaring riwayat transaksi arus barang secara spesifik menjadi mutasi `MASUK` saja (pengadaan pasokan) atau mutasi `KELUAR` saja (penjualan/pemusnahan).
4. **Analisis Statistik Deskriptif (`ringkasan_statistik_deskriptif`):**
   Menghitung ringkasan metrik secara instan meliputi total SKU, total unit fisik, total modal, proyeksi omzet, proyeksi keuntungan, serta melacak produk dengan sisa persediaan tertinggi dan terendah di gudang.
5. **Mekanisme *Graceful Fallback*:**
   Jika program dijalankan pada perangkat laboratorium yang belum terpasang modul `pandas`, sistem tidak mengalami kegagalan fatal (*crash*), melainkan menampilkan petunjuk ramah pengguna untuk melakukan pemasangan pustaka via `pip install pandas`.

---

### 2.5 Hasil Pengujian Sistem dan Verifikasi Kasus Uji
Pengujian sistem dilakukan melalui skrip pengujian otomatis `progress_p7/test_skenario.py` yang mencakup 7 skenario pengujian utama (TC-01 sampai TC-07):

| Kode Kasus Uji | Skenario yang Diuji | Nilai Masukan / Aksi | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-01** | Inisialisasi Data Master & Saldo Awal | Pemuatan modul awal | Terpasang 3 produk bawaan (ATK01, ATK02, KRT01) dan 3 log saldo awal | **LULUS** |
| **TC-02** | Tambah Barang Baru & Proteksi Kode Unik | Menambah kode `ATK03` lalu mencoba duplikasi `atk01` | `ATK03` berhasil tersimpan, duplikasi ditolak sistem | **LULUS** |
| **TC-03** | Transaksi Barang Masuk (Restock) | Menambah 10 unit pada barang `ATK01` (stok awal: 15) | Stok `ATK01` bertambah menjadi 25 unit, log mutasi bertambah | **LULUS** |
| **TC-04** | Transaksi Barang Keluar Valid | Mengeluarkan 5 unit dari `ATK01` (stok saat itu: 25) | Stok `ATK01` berkurang menjadi 20 unit, mutasi tercatat | **LULUS** |
| **TC-05** | Proteksi Anti-Stok Minus (Kuantitas Berlebih) | Mengeluarkan 50 unit dari `ATK02` (stok tersedia: 4) | Transaksi ditolak sistem, saldo stok tetap 4, mutasi keluar dibatalkan | **LULUS** |
| **TC-06** | Deteksi Penanda Visual Stok Kritis | Pengeluaran 3 unit `KRT01` (stok awal: 10, min: 3, sisa: 3) | Sistem menetapkan status `[KRITIS]` karena stok $\le$ batas minimum | **LULUS** |
| **TC-07** | Akurasi Perhitungan Akumulasi Nilai Modal | Kalkulasi rumus $\sum (\text{stok} \times \text{harga beli})$ | Total kuantitas = 47 unit, Total nilai modal = Rp 257.000 tepat 100% | **LULUS** |

**Hasil Ringkasan Uji:** Seluruh kasus uji (7 dari 7 skenario) dinyatakan **LULUS (100% Success Rate)** tanpa terjadi *runtime crash*.

---

### 2.6 Desain Transisi Menuju Fase 2 (Evaluasi UAS)
Pada paruh kedua perkuliahan (Pertemuan 9 s.d. 16), sistem Stokku Desktop akan ditingkatkan (*upgraded*) ke Versi 2.0 dengan rencana teknis:
1. **Penerapan Fungsi Modular (P09):** Pemisahan logika aplikasi ke dalam layanan mandiri (`app/services/stok_service.py`) dengan pembatasan variabel lokal dan penggunaan *pure functions*.
2. **Penanganan Eksepsi Bertingkat (P10):** Proteksi menyeluruh menggunakan blok `try...except ValueError` dan `try...except sqlite3.Error` untuk menangkap galat input tanpa menghentikan program.
3. **Penyimpanan Permanen SQLite (P10):** Migrasi dari struktur data memori ke berkas basis data relasional lokal `stok_gudang.db` dengan skema tabel ternormalisasi `barang` dan `riwayat_transaksi`.
4. **Antarmuka Desktop Tkinter & ttk.Treeview (P11 - P12):** Mengganti antarmuka teks terminal menjadi jendela aplikasi desktop modern lengkap dengan kartu ringkasan informasi, filter pencarian waktu nyata (*real-time*), dan dialog pop-up.

---

## BAB III: PENUTUP

### 3.1 Kesimpulan
Berdasarkan perancangan, implementasi, dan pengujian yang telah dilakukan, dapat ditarik beberapa kesimpulan pokok:
1. Aplikasi **Stokku Desktop** berhasil mengimplementasikan seluruh materi perkuliahan Dasar Pemrograman silabus Pertemuan 1 hingga Pertemuan 7 dalam bentuk aplikasi manajemen stok gudang UMKM yang fungsional dan stabil.
2. Mekanisme validasi logika kondisional pada transaksi pengeluaran barang berhasil mencegah terjadinya stok minus secara mutlak, sehingga integritas data persediaan gudang tetap terjaga.
3. Penerapan pustaka Pandas pada modul pelaporan (`laporan_pandas.py`) memberikan kemudahan dalam menganalisis data inventaris dua dimensi, menghasilkan rekapitulasi nilai modal per kategori, dan menyaring log mutasi secara efisien.
4. Pengujian otomatis membuktikan bahwa program lulus 100% pada seluruh skenario fungsionalitas dan aman dari kegagalan eksekusi (*crash*).

### 3.2 Saran Pengembangan
Demi penyempurnaan sistem pada tahap evaluasi Ujian Akhir Semester (UAS), beberapa saran pengembangan yang direkomendasikan adalah:
1. Mengintegrasikan basis data SQLite permanen agar seluruh data barang dan riwayat mutasi tetap tersimpan saat komputer dimatikan.
2. Membangun antarmuka berbasis grafis (GUI Tkinter) dengan tata warna yang kontras, ergonomis, dan ramah pengguna bagi operator gudang.
3. Menambahkan fitur ekspor laporan ke format berkas Excel (`.xlsx`) atau PDF untuk mempermudah pencetakan dokumen fisik pembukuan UMKM.

---

## DAFTAR PUSTAKA

1. Mustopa, Ali. (2026). *Modul Pembelajaran Praktikum Dasar Pemrograman (Python)*. Jakarta: Program Studi Teknik Informatika, Universitas Bina Sarana Informatika.
2. McKinney, Wes. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.)*. Sebastopol, CA: O'Reilly Media.
3. Python Software Foundation. (2026). *Python 3.13 Standard Library Documentation*. Diakses dari https://docs.python.org/3/
4. Sweigart, Al. (2019). *Automate the Boring Stuff with Python: Practical Programming for Total Beginners (2nd ed.)*. San Francisco: No Starch Press.
5. Sitorus, Lamhot. (2015). *Algoritma dan Pemrograman*. Yogyakarta: Andi Offset.

---

## LAMPIRAN

### Lampiran 1: Cuplikan Kode Modul Laporan Pandas (`progress_p7/laporan_pandas.py`)
```python
def buat_dataframe_barang(daftar_barang: List[Dict[str, Any]]) -> Optional[Any]:
    baris_data = []
    for item in daftar_barang:
        nilai_modal = item["stok"] * item["harga_beli"]
        estimasi_omzet = item["stok"] * item["harga_jual"]
        status = "KRITIS" if item["stok"] <= item["min_stok"] else "AMAN"
        baris_data.append({
            "Kode": item["kode"],
            "Nama Barang": item["nama"],
            "Kategori": item["kategori"],
            "Stok": item["stok"],
            "Harga Beli": item["harga_beli"],
            "Nilai Modal": nilai_modal,
            "Status": status
        })
    return pd.DataFrame(baris_data)
```

### Lampiran 2: Hasil Eksekusi Pengujian 7 Kasus Uji Otomatis
```text
========================================================================
 PENGUJIAN OTOMATIS SISTEM STOKKU DESKTOP (FASE 1 - UTS P08)
 Mata Kuliah: Dasar Pemrograman (894) - Kelas 15.1C.30 UBSI
 Dosen Pengampu: Ali Mustopa, M.Kom (AOP)
 Test Runner & Backend Lead: YUKEN VELINO (15260767 / @Curzyori)
========================================================================
[TC-01] Pengujian Inisialisasi Data Master & Log Mutasi Awal...
  Status: LULUS (3 data dummy master dan 3 log mutasi awal terpasang)
[TC-02] Pengujian Penambahan Barang Baru & Proteksi Kode Duplikat...
  Status: LULUS (Kode unik berhasil ditambah & duplikasi ditolak)
[TC-03] Pengujian Transaksi Barang Masuk (Restock)...
  Status: LULUS (Stok bertambah dari 15 menjadi 25 unit)
[TC-04] Pengujian Transaksi Barang Keluar Valid...
  Status: LULUS (Stok berkurang dari 25 menjadi 20 unit)
[TC-05] Pengujian Proteksi Anti-Stok Minus (Kuantitas Keluar Berlebih)...
  Status: LULUS (Pengeluaran melebihi stok berhasil ditolak sistem)
[TC-06] Pengujian Deteksi Penanda Visual Stok Kritis...
  Status: LULUS (Status [KRITIS] aktif saat stok <= batas minimum aman)
[TC-07] Pengujian Akurasi Perhitungan Akumulasi Nilai Modal Gudang...
  Status: LULUS (Total kuantitas: 47 unit, Total nilai modal: Rp 257.000)
========================================================================
 HASIL AKHIR PENGUJIAN: 7/7 KASUS UJI LULUS (100% SUCCESS RATE)
========================================================================
```

