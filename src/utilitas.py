
def tampilkan_judul():
    """Menampilkan judul aplikasi."""
    print("=" * 45)
    print("       SISTEM ANALISIS NILAI MAHASISWA")
    print("=" * 45)


def format_nilai(nilai):
    """Mengubah nilai menjadi format dua angka desimal."""
    return f"{nilai:.2f}"


def status_kelulusan(nilai, batas=60):
    """Menentukan status kelulusan mahasiswa."""
    if nilai >= batas:
        return "LULUS"
    return "TIDAK LULUS"
