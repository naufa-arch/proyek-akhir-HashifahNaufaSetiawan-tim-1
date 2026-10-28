
def hitung_rata_rata(data):
    """Menghitung rata-rata nilai mahasiswa."""
    if not data:
        return 0

    total = sum(mahasiswa["nilai"] for mahasiswa in data)
    return total / len(data)


def cari_nilai_tertinggi(data):
    """Mencari mahasiswa dengan nilai tertinggi."""
    if not data:
        return None

    return max(data, key=lambda mahasiswa: mahasiswa["nilai"])


def cari_nilai_terendah(data):
    """Mencari mahasiswa dengan nilai terendah."""
    if not data:
        return None

    return min(data, key=lambda mahasiswa: mahasiswa["nilai"])


def hitung_kelulusan(data, batas=60):
    """Menghitung jumlah mahasiswa yang lulus dan tidak lulus."""
    lulus = sum(
        1 for mahasiswa in data
        if mahasiswa["nilai"] >= batas
    )

    tidak_lulus = len(data) - lulus

    return lulus, tidak_lulus


def buat_laporan(data, batas=60):
    """Menyusun laporan analisis nilai."""
    if not data:
        return "Tidak ada data mahasiswa yang valid."

    rata_rata = hitung_rata_rata(data)
    tertinggi = cari_nilai_tertinggi(data)
    terendah = cari_nilai_terendah(data)
    lulus, tidak_lulus = hitung_kelulusan(data, batas)

    laporan = [
        "=" * 45,
        "         LAPORAN ANALISIS NILAI",
        "=" * 45,
        f"Jumlah mahasiswa : {len(data)}",
        f"Rata-rata nilai  : {rata_rata:.2f}",
        f"Batas kelulusan : {batas}",
        f"Jumlah lulus     : {lulus}",
        f"Tidak lulus      : {tidak_lulus}",
        "",
        f"Nilai tertinggi  : {tertinggi['nama']} "
        f"({tertinggi['nilai']:.2f})",
        f"Nilai terendah   : {terendah['nama']} "
        f"({terendah['nilai']:.2f})",
        "",
        "DAFTAR NILAI MAHASISWA",
        "-" * 45,
    ]

    for nomor, mahasiswa in enumerate(data, start=1):
        nama = mahasiswa["nama"]
        nilai = mahasiswa["nilai"]
        status = "LULUS" if nilai >= batas else "TIDAK LULUS"

        laporan.append(
            f"{nomor}. {nama} | Nilai: {nilai:.2f} | {status}"
        )

    laporan.append("=" * 45)
    return "\n".join(laporan)
