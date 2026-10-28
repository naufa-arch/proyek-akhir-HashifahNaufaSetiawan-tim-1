
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
FILE_DATA = ROOT_DIR / "data" / "nilai_contoh.txt"
FOLDER_OUTPUT = ROOT_DIR / "output"


def baca_data():
    """Membaca nama dan nilai mahasiswa dari file teks."""
    data = []

    if not FILE_DATA.exists():
        raise FileNotFoundError(
            f"File data tidak ditemukan: {FILE_DATA}"
        )

    with open(FILE_DATA, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format salah.")
                continue

            nama = bagian[0].strip()

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai bukan angka.")
                continue

            if not nama or not 0 <= nilai <= 100:
                print(f"Baris {nomor} dilewati: data tidak valid.")
                continue

            data.append({
                "nama": nama,
                "nilai": nilai
            })

    return data


def simpan_laporan(teks):
    """Menyimpan hasil analisis ke folder output."""
    FOLDER_OUTPUT.mkdir(parents=True, exist_ok=True)
    file_laporan = FOLDER_OUTPUT / "hasil_analisis.txt"

    with open(file_laporan, "w", encoding="utf-8") as file:
        file.write(teks)

    return file_laporan
