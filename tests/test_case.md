
# Test Case - Sistem Analisis Nilai Mahasiswa

## TC-01: Membaca Data Valid
- Input: File berisi nama dan nilai yang valid.
- Hasil yang diharapkan: Data berhasil dibaca.

## TC-02: Menghitung Rata-rata
- Input: Nilai 80, 70, 90.
- Hasil yang diharapkan: Rata-rata 80.00.

## TC-03: Menentukan Kelulusan
- Input: Nilai 75 dan batas kelulusan 60.
- Hasil yang diharapkan: LULUS.

## TC-04: Nilai di Bawah Batas
- Input: Nilai 50 dan batas kelulusan 60.
- Hasil yang diharapkan: TIDAK LULUS.

## TC-05: Nilai pada Batas Kelulusan
- Input: Nilai 60 dan batas kelulusan 60.
- Hasil yang diharapkan: LULUS.

## TC-06: Data Kosong
- Input: File kosong.
- Hasil yang diharapkan: Program menampilkan pesan bahwa tidak ada data valid.

## TC-07: Nilai Tidak Valid
- Input: Nama mahasiswa dengan nilai berupa teks atau nilai di luar 0-100.
- Hasil yang diharapkan: Baris tidak valid dilewati.

## TC-08: Menyimpan Laporan
- Input: Data mahasiswa valid.
- Hasil yang diharapkan: Laporan tersimpan di output/hasil_analisis.txt.
