# Program Tabel Perkalian
# Input: satu bilangan bulat
# Proses: mengalikan bilangan dengan 1 sampai 10

n = int (input("Masukkan Bilangan: "))

for i in range (1, 11):
    hasil = n * i
    print (f"{n} x {i} = {n * i}")