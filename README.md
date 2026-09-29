# Pertemuan 05 Perulangan Python

Nama: Kesya Nur Aprilliani  
NIM: 2225250219  
Kelas: 3E  

## Tujuan

Menggunakan perulangan for dan while untuk menyelesaikan masalah iteratif menggunakan Python.

## Cara Menjalankan

Untuk menjalankan program Kuis 2, gunakan perintah:

python3 kuis/kuis2_deret_aritmetika.py

Pada Windows dapat menggunakan:

python kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2

1. Memasukkan suku pertama a.
2. Memasukkan beda d.
3. Memasukkan banyak suku n.
4. Memeriksa apakah n merupakan bilangan positif.
5. Jika n kurang dari atau sama dengan 0, program meminta input n kembali.
6. Menginisialisasi total dengan nilai 0.
7. Menggunakan perulangan for sebanyak n kali.
8. Menghitung setiap suku dengan rumus suku = a + i * d.
9. Menambahkan setiap suku ke total.
10. Menampilkan setiap suku.
11. Menampilkan jumlah seluruh suku setelah perulangan selesai.

## Hasil Pengujian

### Test Case 1
Input:
a = 2
d = 3
n = 5

Hasil:
2.00, 5.00, 8.00, 11.00, 14.00

Jumlah:
40.00

Status: Berhasil

### Test Case 2
Input:
a = 10
d = -2
n = 4

Hasil:
10.00, 8.00, 6.00, 4.00

Jumlah:
28.00

Status: Berhasil

### Test Case 3
Input:
a = 1.5
d = 0.5
n = 3

Hasil:
1.50, 2.00, 2.50

Jumlah:
6.00

Status: Berhasil

## Refleksi

Kesalahan yang perlu diperhatikan pada perulangan adalah kondisi berhenti dan pembaruan variabel. Pada program ini, while digunakan untuk memastikan nilai n merupakan bilangan positif. Perulangan for digunakan untuk menghasilkan suku sebanyak n kali. Variabel total harus diinisialisasi sebelum loop agar hasil akumulasi tidak di-reset pada setiap iterasi.