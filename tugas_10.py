# --- LATIHAN 1 ---
# a. Buatlah sebuah Tuple bernama mahasiswa
mahasiswa = ("Vixel Rizky Perdana", "2605060074", "Teknologi Informasi")
print("Data Mahasiswa:", mahasiswa)

# b. Tampilkan data NIM dan Prodi dengan mengakses indeksnya
print("NIM:", mahasiswa[1])
print("Prodi:", mahasiswa[2])

# c. Penjelasan error   mahasiswa[2] = "Teknologi Informasi"
# Pesan error yang muncul adalah TypeError: 'tuple' object does not support item assignment.
# Hal ini terjadi karena Tuple bersifat immutable, artinya elemen di dalamnya tidak dapat diubah, 
# ditambah, atau dihapus setelah tuple tersebut berhasil dibuat.

# d. Buatlah sebuah Set bernama nilai_angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Nilai Angka:", nilai_angka)
# Penjelasan: Angka 10 dan 4 yang ditulis dua kali hanya akan muncul sekali 
# karena karakteristik utama dari Set adalah menyimpan elemen yang unik (tidak ada duplikasi).



# --- LATIHAN 2 ---
# a. Buatlah dictionary bernama data_mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print("\nData Awal :", data_mahasiswa )

# b. Ubah nilai "prodi" menjadi "Sastra Mesin" dan tambahkan key "angkatan" bernilai 2026
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
print ("Setelah diubah :", data_mahasiswa )

# c. Hapus data "nim", lalu tampilkan hasil akhirnya
del data_mahasiswa["nim"]
print("Data Mahasiswa Akhir:", data_mahasiswa)



# --- LATIHAN 3 ---
# a. Buatlah dictionary bernama keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print(keranjang)

# b. Perulangan menampilkan barang dan harga 
print ("---- Daftar Harga Buah ----")
for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")

# c. Tampilkan total belanja
total_belanja = 0
for harga in keranjang.values():
    total_belanja += harga

print("------------------------------")
print("Total belanja: Rp", total_belanja)