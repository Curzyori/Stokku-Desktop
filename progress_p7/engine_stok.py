"""
Modul Mesin Mutasi Stok & Perhitungan Aset (Pertemuan 3, 4, 5)
PIC: YUKEN VELINO (15260767) - Kelompok 4 Dasar Pemrograman 15.1C.30
"""

from datetime import datetime
from validasi import (
    cari_barang_by_kode,
    validasi_kode_unik,
    validasi_stok_keluar,
    validasi_string_tidak_kosong,
)


def cek_status_stok(stok: int, min_stok: int) -> str:
    """Menentukan status stok: KRITIS jika stok <= min_stok, sebaliknya AMAN."""
    if stok <= min_stok:
        return "KRITIS"
    return "AMAN"


def hitung_total_kuantitas(daftar: list) -> int:
    """Menghitung akumulasi seluruh unit fisik barang di gudang."""
    total = 0
    for item in daftar:
        total += item["stok"]
    return total


def hitung_total_aset_modal(daftar: list) -> int:
    """
    Menghitung total nilai modal persediaan gudang.
    Rumus: sum(stok * harga_beli)
    """
    total = 0
    for item in daftar:
        total += item["stok"] * item["harga_beli"]
    return total


def hitung_barang_kritis(daftar: list) -> int:
    """Menghitung jumlah produk yang persediaannya berada pada atau di bawah batas minimum."""
    jumlah = 0
    for item in daftar:
        if item["stok"] <= item["min_stok"]:
            jumlah += 1
    return jumlah


def ringkasan_inventaris(daftar: list) -> dict:
    """Menghasilkan rekapitulasi data persediaan gudang."""
    return {
        "total_sku": len(daftar),
        "total_unit": hitung_total_kuantitas(daftar),
        "total_aset": hitung_total_aset_modal(daftar),
        "total_kritis": hitung_barang_kritis(daftar),
    }


def tambah_barang_baru(
    daftar: list,
    log: list,
    kode: str,
    nama: str,
    kategori: str,
    satuan: str,
    harga_beli: int,
    harga_jual: int,
    stok_awal: int,
    min_stok: int = 5,
) -> tuple[bool, str]:
    """Menambahkan data produk baru ke dalam koleksi master barang."""
    sukses_kode, hasil_kode = validasi_kode_unik(kode, daftar)
    if not sukses_kode:
        return False, hasil_kode

    sukses_nama, hasil_nama = validasi_string_tidak_kosong(nama, "Nama barang")
    if not sukses_nama:
        return False, hasil_nama

    sukses_kat, hasil_kat = validasi_string_tidak_kosong(kategori, "Kategori")
    if not sukses_kat:
        return False, hasil_kat

    sukses_sat, hasil_sat = validasi_string_tidak_kosong(satuan, "Satuan")
    if not sukses_sat:
        return False, hasil_sat

    if harga_beli < 0:
        return False, "Harga beli tidak boleh negatif."
    if harga_jual < 0:
        return False, "Harga jual tidak boleh negatif."
    if stok_awal < 0:
        return False, "Stok awal tidak boleh negatif."
    if min_stok < 1:
        return False, "Batas minimum stok minimal bernilai 1."

    produk_baru = {
        "kode": hasil_kode,
        "nama": hasil_nama,
        "kategori": hasil_kat,
        "satuan": hasil_sat,
        "harga_beli": harga_beli,
        "harga_jual": harga_jual,
        "stok": stok_awal,
        "min_stok": min_stok,
    }
    daftar.append(produk_baru)

    if stok_awal > 0:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.append((
            waktu,
            hasil_kode,
            hasil_nama,
            "MASUK",
            stok_awal,
            0,
            stok_awal,
            "Pendaftaran Produk Baru",
        ))

    return True, f"Barang '{hasil_nama}' ({hasil_kode}) berhasil ditambahkan."


def transaksi_barang_masuk(
    daftar: list,
    log: list,
    kode: str,
    jumlah: int,
    keterangan: str = "Penerimaan Pasokan",
) -> tuple[bool, str]:
    """Menambah stok fisik barang dan mencatat mutasi masuk."""
    item = cari_barang_by_kode(kode, daftar)
    if item is None:
        return False, f"Barang dengan kode '{kode.strip().upper()}' tidak ditemukan."

    if jumlah <= 0:
        return False, "Jumlah barang masuk harus lebih dari 0."

    stok_sebelum = item["stok"]
    item["stok"] += jumlah
    stok_sesudah = item["stok"]

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ket = keterangan.strip() if keterangan.strip() else "Penerimaan Pasokan"
    log.append((
        waktu,
        item["kode"],
        item["nama"],
        "MASUK",
        jumlah,
        stok_sebelum,
        stok_sesudah,
        ket,
    ))

    return True, f"Stok {item['nama']} bertambah {jumlah} {item['satuan']}. Sisa stok saat ini: {stok_sesudah} {item['satuan']}."


def transaksi_barang_keluar(
    daftar: list,
    log: list,
    kode: str,
    jumlah: int,
    keterangan: str = "Penjualan Toko",
) -> tuple[bool, str]:
    """
    Mengurangi stok fisik barang dan mencatat mutasi keluar.
    Menerapkan validasi ketat anti-stok minus: transaksi dibatalkan jika jumlah keluar > sisa stok.
    """
    item = cari_barang_by_kode(kode, daftar)
    if item is None:
        return False, f"Barang dengan kode '{kode.strip().upper()}' tidak ditemukan."

    valid, pesan_error = validasi_stok_keluar(item["stok"], jumlah, item["satuan"])
    if not valid:
        return False, pesan_error

    stok_sebelum = item["stok"]
    item["stok"] -= jumlah
    stok_sesudah = item["stok"]

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ket = keterangan.strip() if keterangan.strip() else "Penjualan Toko"
    log.append((
        waktu,
        item["kode"],
        item["nama"],
        "KELUAR",
        jumlah,
        stok_sebelum,
        stok_sesudah,
        ket,
    ))

    return True, f"Stok {item['nama']} berkurang {jumlah} {item['satuan']}. Sisa stok saat ini: {stok_sesudah} {item['satuan']}."
