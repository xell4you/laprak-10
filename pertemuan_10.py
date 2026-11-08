# Program 10.1 Tuples dan sets

# LIST menggunakan kurung siku
data_list = [10, 2, 4, 3, 2]
print("Data List:", data_list)

# TUPLES menggunakan kurung biasa (Immutable / tidak bisa diubah)
data_tuples = (7, 8, 10, 11)
print("Data Tuples:", data_tuples)
print("Indeks ke-1 tuple:", data_tuples[1])

# Baris di bawah ini akan menyebabkan error jika di-uncomment karena tuple bersifat immutable:
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# SETS (Himpunan) menggunakan kurung kurawal (Unik dan tidak terurut)
data_sets = {10, 4, 3, 2, 7, 6, 5}
print("Data Sets:", data_sets)

# Catatan: data_sets[0] akan error karena set tidak memiliki indeks tetap.



# Program 10.2 Dictionary

# List -> mengakses dengan menggunakan indeks angka
data_list = ['ucup', 'rendi', 'salsa']
print("List indeks ke-0:", data_list[0])

# Dictionary (dict): associative array (menggunakan key sebagai identifier)
data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'rd': 'rendi',
    'sl': 'salsa',
    'nmbr': 100,
    'list': data_list
}

print("Akses key 'cp':", data_dict['cp'])
print("Akses key 'nmbr':", data_dict['nmbr'])
print("Akses key 'list':", data_dict['list'])



# Program 10.3 Operasi Dictionary[cite: 3, 4]

data_dict = {
    "cup": "ucup surucup",
    "pet": "opet saripet",
    "ndo": "nando surundo"
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# Mengecek apakah key ada atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses value (read) dengan pemanggilan key dan fungsi get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan"))  # pesan default jika key tidak ada

# Mengupdate data
data_dict["cup"] = "ucup si ganteng"
print("Update data cup:", data_dict)

data_dict["de"] = "ade si adek"
print("Tambah data de:", data_dict)

data_dict.update({"cup": "ucup surucup"})
print("Update dengan update():", data_dict)

data_dict.update({"iwn": "iwan mang keren"})  # ditambah jika belum ada
print("Tambah data iwn:", data_dict)

# Menghapus data
del data_dict["iwn"]
print("Setelah menghapus iwn:", data_dict)



# Program 10.4 Looping Dictionary

teman_teman = {
    "cup": "ucup surucup",
    "tong": "sotong surotong",
    "lur": "lur sedulur",
    "wel": "bung towel"
}

# Looping first try (yang keluar hanya key-nya saja)
print("--- Looping Key Saja ---")
for teman in teman_teman:
    print(teman)

# Menggunakan method .keys()
print("--- Menggunakan .keys() ---")
keys = teman_teman.keys()
print(keys)
for key in teman_teman.keys():
    print(teman_teman.get(key))

# Menggunakan method .values()
print("--- Menggunakan .values() ---")
values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

# Menggunakan method .items()
print("--- Menggunakan .items() ---")
items = teman_teman.items()
print(items)
for item in teman_teman.items():
    print(item)

# Looping key dan value secara bersamaan
print("--- Looping Key & Value ---")
for key, value in teman_teman.items():
    print(f"key: {key}, value: {value}")