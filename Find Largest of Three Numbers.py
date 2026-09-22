a = int(input("Masukkan Angka Pertama : "))
b = int(input("Masukkan Angka kedua : "))
c = int(input("Masukkan Angka Ketiga : "))

if a > b and a > c:
    largest = a
    print("Angka Terbesar Adalah:", largest)
elif b > a and b > c:
    largest = b
    print("Angka Terbesar Adalah:", largest)
elif c > a and c > b:
    largest = c
    print("Angka Terbesar Adalah:", largest)
else:
    print("tidak ada angka terbesar")