
from data_io import baca_data, simpan_laporan
from analisis import buat_laporan
from utilitas import tampilkan_judul


def main():
    tampilkan_judul()

    try:
        data = baca_data()

        if not data:
            print("Tidak ada data valid untuk dianalisis.")
            return

        laporan = buat_laporan(data, batas=60)

        print(laporan)

        lokasi = simpan_laporan(laporan)
        print(f"\nLaporan berhasil disimpan di:\n{lokasi}")

    except FileNotFoundError as error:
        print(f"Terjadi kesalahan: {error}")

    except OSError as error:
        print(f"Gagal membaca atau menyimpan file: {error}")


if __name__ == "__main__":
    main()
