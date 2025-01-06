#bagian 3 soal 1
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

#bagian 3 Soal 2
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
