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

