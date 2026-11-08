"""
Modul Penyimpanan Data In-Memory (Pertemuan 1, 2, 6)
PIC: YUKEN VELINO (15260767) - Kelompok 4 Dasar Pemrograman 15.1C.30
"""

from datetime import datetime

DATA_AWAL = [
    {
        "kode": "ATK01",
        "nama": "Buku Tulis Kiky 38 Lembar",
        "kategori": "ATK",
        "satuan": "Pcs",
        "harga_beli": 3500,
        "harga_jual": 5000,
        "stok": 15,
        "min_stok": 5,
    },
    {
        "kode": "ATK02",
        "nama": "Pulpen Faster C600 Hitam",
        "kategori": "ATK",
        "satuan": "Pcs",
        "harga_beli": 2500,
        "harga_jual": 3500,
        "stok": 4,
        "min_stok": 5,
    },
    {
        "kode": "KRT01",
        "nama": "Kertas HVS Sinar Dunia A4 75gr",
        "kategori": "Kertas",
        "satuan": "Rim",
        "harga_beli": 42000,
        "harga_jual": 48000,
        "stok": 10,
        "min_stok": 3,
    },
]

daftar_barang = [dict(item) for item in DATA_AWAL]
log_mutasi = []


def inisialisasi_log_awal():
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in DATA_AWAL:
        log_mutasi.append((
            waktu_sekarang,
            item["kode"],
            item["nama"],
            "MASUK",
            item["stok"],
            0,
            item["stok"],
            "Saldo Awal Sistem",
        ))


inisialisasi_log_awal()


def reset_data():
    """Mengembalikan data master dan riwayat mutasi ke kondisi awal."""
    global daftar_barang, log_mutasi
    daftar_barang.clear()
    daftar_barang.extend([dict(item) for item in DATA_AWAL])
    log_mutasi.clear()
    inisialisasi_log_awal()
