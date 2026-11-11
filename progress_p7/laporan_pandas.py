"""
Modul Analisis Tabular & Pelaporan Data Persediaan Berbasis Pandas (Pertemuan 7)
PIC: RENKYNA AFTANIA NASUTION (15260847) - Kelompok 4 Dasar Pemrograman 15.1C.30
Mata Kuliah: Dasar Pemrograman (Kode: 894) - Universitas Bina Sarana Informatika
Dosen Pengampu: Ali Mustopa, M.Kom (AOP)
"""

from typing import List, Dict, Tuple, Optional, Any

try:
    import pandas as pd
    PANDAS_TERSEDIA = True
except ImportError:
    pd = None
    PANDAS_TERSEDIA = False


def cek_ketersediaan_pandas() -> bool:
    """Memeriksa apakah pustaka pandas sudah terpasang di sistem."""
    return PANDAS_TERSEDIA


def format_rupiah(nilai: Any) -> str:
    """Format angka ke dalam mata uang Rupiah standar."""
    try:
        angka = int(round(float(nilai)))
        tanda = "-" if angka < 0 else ""
        return f"{tanda}Rp {abs(angka):,}".replace(",", ".")
    except (ValueError, TypeError):
        return "Rp 0"


def buat_dataframe_barang(daftar_barang: List[Dict[str, Any]]) -> Optional[Any]:
    """
    Mengonversi daftar dictionary barang ke dalam objek pandas.DataFrame.
    Menerapkan materi Pertemuan 7 (Struktur Data Tabular Dua Dimensi).
    Menghitung kolom turunan: Nilai Modal, Estimasi Omzet, Potensi Laba, dan Status Kritis.
    """
    if not PANDAS_TERSEDIA:
        return None

    if not daftar_barang:
        return pd.DataFrame(columns=[
            "Kode", "Nama Barang", "Kategori", "Satuan",
            "Harga Beli", "Harga Jual", "Stok", "Min Stok",
            "Nilai Modal", "Estimasi Omzet", "Potensi Laba", "Status"
        ])

    baris_data = []
    for item in daftar_barang:
        kode = item.get("kode_barang") or item.get("kode", "")
        nama = item.get("nama_barang") or item.get("nama", "")
        kategori = item.get("kategori", "")
        satuan = item.get("satuan", "")
        harga_beli = int(item.get("harga_beli", 0))
        harga_jual = int(item.get("harga_jual", 0))
        stok = int(item.get("stok", 0))
        min_stok = int(item.get("min_stok", 5))

        nilai_modal = stok * harga_beli
        estimasi_omzet = stok * harga_jual
        potensi_laba = (harga_jual - harga_beli) * stok
        status = "KRITIS" if stok <= min_stok else "AMAN"

        baris_data.append({
            "Kode": kode,
            "Nama Barang": nama,
            "Kategori": kategori,
            "Satuan": satuan,
            "Harga Beli": harga_beli,
            "Harga Jual": harga_jual,
            "Stok": stok,
            "Min Stok": min_stok,
            "Nilai Modal": nilai_modal,
            "Estimasi Omzet": estimasi_omzet,
            "Potensi Laba": potensi_laba,
            "Status": status
        })

    df = pd.DataFrame(baris_data)
    return df


def buat_dataframe_mutasi(log_mutasi: List[Tuple]) -> Optional[Any]:
    """
    Mengonversi list of tuple riwayat transaksi mutasi ke pandas.DataFrame.
    """
    if not PANDAS_TERSEDIA:
        return None

    kolom = [
        "Waktu", "Kode", "Nama Barang", "Jenis",
        "Jumlah", "Stok Sebelum", "Stok Sesudah", "Keterangan"
    ]

    if not log_mutasi:
        return pd.DataFrame(columns=kolom)

    data_mutasi = []
    for log in log_mutasi:
        waktu, kode, nama, jenis, jumlah, seb, ses, ket = log
        data_mutasi.append({
            "Waktu": waktu,
            "Kode": kode,
            "Nama Barang": nama,
            "Jenis": jenis,
            "Jumlah": int(jumlah),
            "Stok Sebelum": int(seb),
            "Stok Sesudah": int(ses),
            "Keterangan": ket
        })

    df = pd.DataFrame(data_mutasi)
    return df


def rekapitulasi_kategori(df_barang: Any) -> Optional[Any]:
    """
    Menghasilkan agregasi statistik per kategori menggunakan method groupby() Pandas.
    Menghitung total SKU, total unit fisik, total modal belanja, dan rata-rata harga beli.
    """
    if not PANDAS_TERSEDIA or df_barang is None or df_barang.empty:
        return None

    rekap = df_barang.groupby("Kategori").agg(
        Total_SKU=("Kode", "count"),
        Total_Unit=("Stok", "sum"),
        Total_Modal=("Nilai Modal", "sum"),
        Rata_Harga_Beli=("Harga Beli", "mean")
    ).reset_index()

    rekap["Rata_Harga_Beli"] = rekap["Rata_Harga_Beli"].round(0).astype(int)
    return rekap


def filter_mutasi_berdasarkan_jenis(df_mutasi: Any, jenis: str = "SEMUA") -> Optional[Any]:
    """
    Menyaring data mutasi berdasarkan jenis transaksi (SEMUA, MASUK, atau KELUAR).
    """
    if not PANDAS_TERSEDIA or df_mutasi is None or df_mutasi.empty:
        return df_mutasi

    jenis_bersih = jenis.strip().upper()
    if jenis_bersih in ("MASUK", "KELUAR"):
        return df_mutasi[df_mutasi["Jenis"] == jenis_bersih].copy()
    return df_mutasi.copy()


def ringkasan_statistik_deskriptif(df_barang: Any) -> Dict[str, Any]:
    """
    Menghitung metrik analitis deskriptif inventaris gudang berbasis operasi Pandas.
    """
    if not PANDAS_TERSEDIA or df_barang is None or df_barang.empty:
        return {
            "total_sku": 0,
            "total_unit": 0,
            "total_modal": 0,
            "total_potensi_omzet": 0,
            "total_potensi_laba": 0,
            "jumlah_kritis": 0,
            "produk_terbanyak": "-",
            "produk_tersedikit": "-"
        }

    total_sku = len(df_barang)
    total_unit = int(df_barang["Stok"].sum())
    total_modal = int(df_barang["Nilai Modal"].sum())
    total_omzet = int(df_barang["Estimasi Omzet"].sum())
    total_laba = int(df_barang["Potensi Laba"].sum())
    jumlah_kritis = int((df_barang["Status"] == "KRITIS").sum())

    idx_maks = df_barang["Stok"].idxmax()
    idx_min = df_barang["Stok"].idxmin()

    produk_terbanyak = f"{df_barang.loc[idx_maks, 'Nama Barang']} ({df_barang.loc[idx_maks, 'Stok']} {df_barang.loc[idx_maks, 'Satuan']})"
    produk_tersedikit = f"{df_barang.loc[idx_min, 'Nama Barang']} ({df_barang.loc[idx_min, 'Stok']} {df_barang.loc[idx_min, 'Satuan']})"

    return {
        "total_sku": total_sku,
        "total_unit": total_unit,
        "total_modal": total_modal,
        "total_potensi_omzet": total_omzet,
        "total_potensi_laba": total_laba,
        "jumlah_kritis": jumlah_kritis,
        "produk_terbanyak": produk_terbanyak,
        "produk_tersedikit": produk_tersedikit
    }


def tampilkan_tabel_barang_pandas(df_barang: Any) -> None:
    """Mencetak data master produk dalam format tabel tabular yang terstruktur."""
    if df_barang is None or df_barang.empty:
        print("[INFO] Tidak ada data produk yang dapat ditampilkan.")
        return

    print("\n" + "=" * 105)
    print("                      TABEL MASTER INVENTARIS GUDANG (PANDAS DATAFRAME)                          ")
    print("=" * 105)
    header = f"{'KODE':<8} | {'NAMA PRODUK':<28} | {'KATEGORI':<10} | {'STOK':<6} | {'HARGA BELI':<12} | {'NILAI MODAL':<14} | {'STATUS':<8}"
    print(header)
    print("-" * 105)

    for _, row in df_barang.iterrows():
        status_tag = f"[{row['Status']}]"
        print(
            f"{row['Kode']:<8} | "
            f"{row['Nama Barang'][:28]:<28} | "
            f"{row['Kategori'][:10]:<10} | "
            f"{row['Stok']:<6} | "
            f"{format_rupiah(row['Harga Beli']):<12} | "
            f"{format_rupiah(row['Nilai Modal']):<14} | "
            f"{status_tag:<8}"
        )
    print("=" * 105)


def tampilkan_rekap_kategori(rekap: Any) -> None:
    """Mencetak tabel rekapitulasi nilai persediaan per kategori."""
    if rekap is None or rekap.empty:
        print("[INFO] Belum ada data kategori untuk direkapitulasi.")
        return

    print("\n" + "-" * 76)
    print("            REKAPITULASI PERSEDIAAN PER KATEGORI (GROUPBY P07)              ")
    print("-" * 76)
    print(f"{'KATEGORI':<15} | {'TOTAL SKU':<10} | {'TOTAL UNIT':<12} | {'TOTAL MODAL':<16} | {'RATA-RATA HARGA':<15}")
    print("-" * 76)

    for _, row in rekap.iterrows():
        print(
            f"{row['Kategori']:<15} | "
            f"{row['Total_SKU']:<10} | "
            f"{row['Total_Unit']:<12} | "
            f"{format_rupiah(row['Total_Modal']):<16} | "
            f"{format_rupiah(row['Rata_Harga_Beli']):<15}"
        )
    print("-" * 76)


def tampilkan_tabel_mutasi_pandas(df_mutasi: Any, filter_judul: str = "SEMUA") -> None:
    """Mencetak tabel log mutasi transaksi arus barang."""
    if df_mutasi is None or df_mutasi.empty:
        print(f"[INFO] Tidak ada riwayat mutasi dengan filter [{filter_judul}].")
        return

    print("\n" + "=" * 108)
    print(f"               TABEL RIWAYAT MUTASI ARUS BARANG [FILTER: {filter_judul}] (PANDAS DATAFRAME)             ")
    print("=" * 108)
    print(f"{'WAKTU':<19} | {'KODE':<8} | {'JENIS':<7} | {'JUMLAH':<6} | {'SEBELUM':<8} | {'SESUDAH':<8} | {'KETERANGAN':<30}")
    print("-" * 108)

    for _, row in df_mutasi.iterrows():
        print(
            f"{row['Waktu']:<19} | "
            f"{row['Kode']:<8} | "
            f"{row['Jenis']:<7} | "
            f"{row['Jumlah']:<6} | "
            f"{row['Stok Sebelum']:<8} | "
            f"{row['Stok Sesudah']:<8} | "
            f"{row['Keterangan'][:30]:<30}"
        )
    print("=" * 108)


def tampilkan_laporan_pandas(daftar_barang: List[Dict[str, Any]], log_mutasi: List[Tuple]) -> None:
    """
    Titik integrasi utama yang dipanggil oleh main_p7.py pada Opsi Menu 6.
    Menampilkan menu navigasi analisis laporan berbasis Pandas dengan antarmuka terminal interaktif.
    """
    if not PANDAS_TERSEDIA:
        print("\n" + "!" * 72)
        print(" [PERINGATAN] Modul 'pandas' belum terpasang pada lingkungan Python Anda.")
        print(" Modul ini diperlukan untuk menguji materi Silabus Pertemuan 7 (Data Tabular).")
        print(" Silakan jalankan perintah instalasi berikut pada terminal Anda:")
        print("     pip install pandas")
        print("!" * 72)
        return

    df_barang = buat_dataframe_barang(daftar_barang)
    df_mutasi = buat_dataframe_mutasi(log_mutasi)

    while True:
        print("\n" + "=" * 65)
        print("     SUB-MENU ANALISIS PERSEDIAAN PANDAS (SILABUS P07)     ")
        print("     Penanggung Jawab: RENKYNA AFTANIA NASUTION (15260847) ")
        print("=" * 65)
        print(" 1. Tampilkan Matriks Data Produk & Nilai Modal (DataFrame)")
        print(" 2. Rekapitulasi Nilai Aset per Kategori (Groupby Analysis)")
        print(" 3. Ringkasan Statistik Deskriptif Persediaan")
        print(" 4. Riwayat Mutasi Lengkap (Semua Transaksi)")
        print(" 5. Riwayat Mutasi Barang Masuk Saja (Restock)")
        print(" 6. Riwayat Mutasi Barang Keluar Saja")
        print(" 0. Kembali ke Menu Utama")
        print("-" * 65)

        pilihan = input("Pilih sub-menu analisis [0-6]: ").strip()

        if pilihan == "1":
            tampilkan_tabel_barang_pandas(df_barang)
        elif pilihan == "2":
            rekap = rekapitulasi_kategori(df_barang)
            tampilkan_rekap_kategori(rekap)
        elif pilihan == "3":
            stats = ringkasan_statistik_deskriptif(df_barang)
            print("\n" + "-" * 60)
            print("         RINGKASAN METRIK ANALISIS PERSEDIAAN GUDANG          ")
            print("-" * 60)
            print(f" - Total Item Terdaftar (SKU) : {stats['total_sku']} Produk")
            print(f" - Total Akumulasi Kuantitas  : {stats['total_unit']} Unit")
            print(f" - Total Nilai Modal Belanja  : {format_rupiah(stats['total_modal'])}")
            print(f" - Estimasi Potensi Omzet     : {format_rupiah(stats['total_potensi_omzet'])}")
            print(f" - Estimasi Potensi Laba Kotor: {format_rupiah(stats['total_potensi_laba'])}")
            print(f" - Produk dalam Status Kritis : {stats['jumlah_kritis']} SKU")
            print(f" - Stok Persediaan Tertinggi  : {stats['produk_terbanyak']}")
            print(f" - Stok Persediaan Terendah   : {stats['produk_tersedikit']}")
            print("-" * 60)
        elif pilihan == "4":
            tampilkan_tabel_mutasi_pandas(df_mutasi, "SEMUA MUTASI")
        elif pilihan == "5":
            df_masuk = filter_mutasi_berdasarkan_jenis(df_mutasi, "MASUK")
            tampilkan_tabel_mutasi_pandas(df_masuk, "BARANG MASUK")
        elif pilihan == "6":
            df_keluar = filter_mutasi_berdasarkan_jenis(df_mutasi, "KELUAR")
            tampilkan_tabel_mutasi_pandas(df_keluar, "BARANG KELUAR")
        elif pilihan == "0":
            break
        else:
            print("[Peringatan] Pilihan tidak valid. Silakan pilih angka 0 sampai 6.")

