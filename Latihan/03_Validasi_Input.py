# Program Validasi Input Nilai
# Input: nilai ujian 0 sampai 100
# Proses: mengulang input jika nilai tidak valid
# Output: nilai yang diterima

nilai = int(input("Masukkan nilai ujian: "))

while nilai < 0 or nilai > 100:
    print("Nilai yang tidak valid.")
    nilai = int(input("Masukkan nilai ujian: "))

print("Nilai valid:", nilai)