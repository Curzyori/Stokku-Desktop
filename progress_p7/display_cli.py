def format_rupiah(nominal: int) -> str:
    nominal_int = int(nominal)
    tanda = "-" if nominal_int < 0 else ""
    angka_positif = abs(nominal_int)
    formatted = f"{angka_positif:,}".replace(",", ".")
    return f"{tanda}Rp {formatted}"


def status_stok(stok: int, min_stok: int) -> str:
    return "[KRITIS]" if int(stok) <= int(min_stok) else "[AMAN]"


def tampilkan_banner() -> None:
    garis = "=" * 96
    print(garis)
    print("                              STOKKU DESKTOP                              ")
    print("               Manajemen Persediaan Gudang UMKM (In-Memory CLI)            ")
    print("                 Dasar Pemrograman (894) - Kelompok 4 UBSI                ")
    print(garis)


def tampilkan_ringkasan(total_sku: int, total_unit: int, total_aset: int, total_kritis: int) -> None:
    garis = "+" + "-" * 94 + "+"
    status_label = f"{total_kritis} Produk [KRITIS]" if total_kritis > 0 else "0 Produk [AMAN]"
    judul = "RINGKASAN STATUS GUDANG"
    
    col1_a = f"Total Jenis (SKU) : {total_sku} Produk"
    col2_a = f"Total Unit Fisik  : {total_unit} Unit"
    col1_b = f"Total Estimasi    : {format_rupiah(total_aset)}"
    col2_b = f"Status Perhatian  : {status_label}"

    print(garis)
    print(f"|{judul:^94}|")
    print(garis)
    print(f"|  {col1_a:<43}  {col2_a:<45}  |")
    print(f"|  {col1_b:<43}  {col2_b:<45}  |")
    print(garis)


def tampilkan_tabel_barang(daftar_barang: list) -> None:
    if not daftar_barang:
        print("\n[INFO] Belum ada data barang di inventaris gudang.\n")
        return

    garis = "+----------+--------------------------------+-------------+---------+--------------+--------------+-------+-----+----------+"
    header = "| Kode     | Nama Barang                    | Kategori    | Satuan  | Harga Beli   | Harga Jual   | Stok  | Min | Status   |"
    
    print("\n" + garis)
    print(header)
    print(garis)

    for item in daftar_barang:
        kode = str(item.get("kode_barang") or item.get("kode") or "")[:8]
        nama = str(item.get("nama_barang") or item.get("nama") or "")[:30]
        kategori = str(item.get("kategori", ""))[:11]
        satuan = str(item.get("satuan", ""))[:7]
        harga_beli = format_rupiah(item.get("harga_beli", 0))
        harga_jual = format_rupiah(item.get("harga_jual", 0))
        stok = int(item.get("stok", 0))
        min_stok = int(item.get("min_stok", 5))
        status = status_stok(stok, min_stok)

        print(
            f"| {kode:<8} "
            f"| {nama:<30} "
            f"| {kategori:<11} "
            f"| {satuan:<7} "
            f"| {harga_beli:>12} "
            f"| {harga_jual:>12} "
            f"| {stok:>5} "
            f"| {min_stok:>3} "
            f"| {status:^8} |"
        )
    print(garis + "\n")


def tampilkan_tabel_riwayat(daftar_mutasi: list) -> None:
    if not daftar_mutasi:
        print("\n[INFO] Belum ada riwayat transaksi mutasi.\n")
        return

    garis = "+-----+---------------------+----------+------------------------------+---------+-------+-------+-------+------------------------+"
    header = "| No  | Tanggal & Waktu     | Kode     | Nama Barang                  | Jenis   | Qty   | Awal  | Akhir | Keterangan             |"
    
    print("\n" + garis)
    print(header)
    print(garis)

    for index, mutasi in enumerate(daftar_mutasi, start=1):
        if isinstance(mutasi, dict):
            tanggal = str(mutasi.get("tanggal", ""))[:19]
            kode = str(mutasi.get("kode_barang") or mutasi.get("kode") or "")[:8]
            nama = str(mutasi.get("nama_barang") or mutasi.get("nama") or "")[:28]
            jenis = str(mutasi.get("jenis_transaksi") or mutasi.get("jenis") or "")[:7]
            jumlah = int(mutasi.get("jumlah", 0))
            stok_awal = int(mutasi.get("stok_sebelum", 0))
            stok_akhir = int(mutasi.get("stok_sesudah", 0))
            keterangan = str(mutasi.get("keterangan", ""))[:22]
        elif isinstance(mutasi, (list, tuple)) and len(mutasi) >= 8:
            tanggal = str(mutasi[0])[:19]
            kode = str(mutasi[1])[:8]
            nama = str(mutasi[2])[:28]
            jenis = str(mutasi[3])[:7]
            jumlah = int(mutasi[4])
            stok_awal = int(mutasi[5])
            stok_akhir = int(mutasi[6])
            keterangan = str(mutasi[7])[:22]
        else:
            continue

        qty_str = f"+{jumlah}" if jenis.upper() == "MASUK" else f"-{jumlah}"

        print(
            f"| {index:<3} "
            f"| {tanggal:<19} "
            f"| {kode:<8} "
            f"| {nama:<28} "
            f"| {jenis:<7} "
            f"| {qty_str:>5} "
            f"| {stok_awal:>5} "
            f"| {stok_akhir:>5} "
            f"| {keterangan:<22} |"
        )
    print(garis + "\n")


def tampilkan_pesan_sukses(pesan: str) -> None:
    print(f"[SUKSES] {pesan}")


def tampilkan_pesan_error(pesan: str) -> None:
    print(f"[ERROR] {pesan}")


cetak_tabel_barang = tampilkan_tabel_barang
cetak_log_mutasi = tampilkan_tabel_riwayat


if __name__ == "__main__":
    tampilkan_banner()
    tampilkan_ringkasan(total_sku=3, total_unit=35, total_aset=2450000, total_kritis=1)
    
    contoh_barang = [
        {
            "kode_barang": "BRG001",
            "nama_barang": "Beras Rojolele 5kg",
            "kategori": "Sembako",
            "satuan": "Karung",
            "harga_beli": 65000,
            "harga_jual": 75000,
            "stok": 20,
            "min_stok": 5,
        },
        {
            "kode_barang": "BRG002",
            "nama_barang": "Minyak Goreng 2L",
            "kategori": "Sembako",
            "satuan": "Pouch",
            "harga_beli": 28000,
            "harga_jual": 33000,
            "stok": 3,
            "min_stok": 5,
        },
        {
            "kode_barang": "BRG003",
            "nama_barang": "Gula Pasir 1kg",
            "kategori": "Sembako",
            "satuan": "Bungkus",
            "harga_beli": 15000,
            "harga_jual": 17500,
            "stok": 12,
            "min_stok": 5,
        },
    ]
    tampilkan_tabel_barang(contoh_barang)

    contoh_mutasi = [
        {
            "tanggal": "2026-11-08 09:30:00",
            "kode_barang": "BRG001",
            "nama_barang": "Beras Rojolele 5kg",
            "jenis_transaksi": "MASUK",
            "jumlah": 10,
            "stok_sebelum": 10,
            "stok_sesudah": 20,
            "keterangan": "Pasokan Grosir",
        },
        {
            "tanggal": "2026-11-08 10:15:00",
            "kode_barang": "BRG002",
            "nama_barang": "Minyak Goreng 2L",
            "jenis_transaksi": "KELUAR",
            "jumlah": 7,
            "stok_sebelum": 10,
            "stok_sesudah": 3,
            "keterangan": "Penjualan Toko",
        },
    ]
    tampilkan_tabel_riwayat(contoh_mutasi)
    tampilkan_pesan_sukses("Pengujian demonstrasi visual berhasil dijalankan.")
