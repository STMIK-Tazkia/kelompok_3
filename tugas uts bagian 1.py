#bagian 1 soal 6
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
