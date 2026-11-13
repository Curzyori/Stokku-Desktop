"""
Modul Validasi Input & Integritas Data (Pertemuan 3 & 4)
PIC: YUKEN VELINO (15260767) - Kelompok 4 Dasar Pemrograman 15.1C.30
"""


def validasi_kode_unik(kode: str, daftar: list) -> tuple[bool, str]:
    kode_bersih = kode.strip().upper()
    if not kode_bersih:
        return False, "Kode barang tidak boleh kosong."

    if not kode_bersih.isalnum():
        return False, "Kode barang hanya boleh berupa kombinasi huruf dan angka."

    for item in daftar:
        if item["kode"].upper() == kode_bersih:
            return False, f"Kode barang '{kode_bersih}' sudah terdaftar."

    return True, kode_bersih


def validasi_angka_positif(nilai_input: str, nama_field: str = "Nilai", min_val: int = 1) -> tuple[bool, int, str]:
    teks = str(nilai_input).strip()
    if not teks:
        return False, 0, f"{nama_field} tidak boleh kosong."

    if not (teks.isdigit() or (teks.startswith("-") and teks[1:].isdigit())):
        return False, 0, f"{nama_field} harus berupa bilangan bulat."

    nilai_int = int(teks)
    if nilai_int < min_val:
        if min_val == 1:
            return False, 0, f"{nama_field} harus berupa bilangan bulat positif (minimal 1)."
        return False, 0, f"{nama_field} tidak boleh kurang dari {min_val}."

    return True, nilai_int, ""


def validasi_stok_keluar(stok_saat_ini: int, jumlah_keluar: int,
                         satuan: str = "") -> tuple[bool, str]:
    if jumlah_keluar <= 0:
        return False, "Jumlah barang keluar harus lebih dari 0."

    if jumlah_keluar > stok_saat_ini:
        akhiran = f" {satuan}" if satuan else ""
        return False, (
            "Stok tidak mencukupi. Sisa stok fisik saat ini: "
            f"{stok_saat_ini}{akhiran}."
        )

    return True, ""


def validasi_string_tidak_kosong(teks: str, nama_field: str) -> tuple[bool, str]:
    hasil = str(teks).strip()
    if not hasil:
        return False, f"{nama_field} tidak boleh kosong."
    return True, hasil


def cari_barang_by_kode(kode: str, daftar: list):
    kode_cari = kode.strip().upper()
    for item in daftar:
        if item["kode"].upper() == kode_cari:
            return item
    return None
