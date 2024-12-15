
# Perkalian Matriks 4x4
matriksC = [
    [44, 55, 34, 10],
    [33, 25, 75, 13],
    [21, 71, 21, 11],
    [33, 88, 32, 15]
]

matriksD = [
    [1, 1, 1, 1],
    [2, 1, 0, 0],
    [0, 0, 1, 2],
    [1, 1, 1, 1]
]

# Perkalian matriks
hasil = [[sum(matriksC[i][k] * matriksD[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

# Menampilkan hasil perkalian
print("Hasil Perkalian Matriks:")
for baris in hasil:
    print(baris)

# Definisikan himpunan A dan B
A = {231, 768, 50, 18, 22, 390, 23, 14, 8, 19}
B = {19, 12, 56, 21, 21.7, 768, 8, 6, 4, 22}

# Fungsi untuk menghitung irisan dan beda setangkup
def hitung_himpunan(A, B):
    irisan = A.intersection(B)
    beda_setangkup = A.symmetric_difference(B)
    return irisan, beda_setangkup

# Fungsi untuk peluang (P(A) dan P(B))
def peluang(A, B):
    total_universum = len(A.union(B))  # Total elemen gabungan A dan B
    P_A = len(A) / total_universum
    P_B = len(B) / total_universum
    return P_A, P_B

# Hitung irisan dan beda setangkup
irisan, beda_setangkup = hitung_himpunan(A, B)

# Hitung peluang
P_A, P_B = peluang(A, B)

# Cetak hasil
print("Irisan A dan B:", irisan)
print("Beda setangkup A dan B:", beda_setangkup)
print("Peluang P(A):", P_A)
print("Peluang P(B):", P_B)


# Definisikan himpunan A
A = {109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 378, 400, 101, 201, 301, 1}

# Fungsi untuk mengurutkan himpunan A dengan bubble sort
def bubble_sort(parameter):
    n = len(parameter)
    # Melakukan bubble sort
    for i in range(n):
        swapped = False
        # Mengurangi perbandingan elemen setelah setiap iterasi karena elemen terbesar sudah berada di akhir
        for j in range(0, n - i - 1):
            if parameter[j] > parameter[j + 1]:
                # Tukar elemen jika elemen sebelumnya lebih besar
                parameter[j], parameter[j + 1] = parameter[j + 1], parameter[j]
                swapped = True
        # Jika tidak ada pertukaran, parameter array sudah terurut
        if not swapped:
            break
    return parameter

# Mengubah himpunan A menjadi list agar bisa diurutkan
A_list = list(A)

# Mengurutkan Himpunan A dengan bubble sort
sorted_A = bubble_sort(A_list)

# Menampilkan hasil setelah diurutkan
print("Himpunan yang diurutkan:", sorted_A)

# Himpunan yang diberikan
A = {109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 378, 400, 101, 201, 301, 1}

# Fungsi Untuk Mencari Nilai X Pada Himpunan A
x = 109

# Mengubah himpunan menjadi list dan mengurutkannya
sorted_A = sorted(A)

# Mencari indeks elemen x dalam list yang terurut
if x in sorted_A:
    index = sorted_A.index(x)
    print(f"Nilai {x} ditemukan pada indeks {index} dalam himpunan yang terurut.")
else:
    print(f"Nilai {x} tidak ditemukan dalam himpunan.")
