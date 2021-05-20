# Nama file : import.py
# Mengimport modul geometri2D

from Matematika import geometri2D

#persegi panjang
p = 10
l = 8

luas = geometri2D.luasPersegiPanjang(p, l)
kel = geometri2D.kelilingPersegiPanjang(p, l)

print("PERSEGI PANJANG")
print("Panjang\t:", p)
print("lebar\t:", l)
print("Luas\t:", luas)
print("Keliling\t=", kel)

#lingkaran
jarijari = 3

luas = geometri2D.luasLingkaran(jarijari)
kel = geometri2D.kelilingLingkaran(jarijari)

print("\nLINGKARAN")
print("jari-jari\t:", jarijari)
print("Luas\t:", luas)
print("Keliling\t:", kel)
