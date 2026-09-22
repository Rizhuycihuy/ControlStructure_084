a = int(input("Masukkan Angka Pertama : "))
b = int(input("Masukkan Angka kedua : "))
c = int(input("Masukkan Angka Ketiga : "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Angka Terbesar Adalah:", largest)