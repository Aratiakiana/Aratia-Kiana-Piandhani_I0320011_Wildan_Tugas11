#nama file: fromimport.py
#mengimpor fungsi luasPersegiPanjang
#dari modul geometri2D
from Matematika.geometri2D import luasPersegiPanjang

#persegi panjang
p = 10
l = 8

luas = luasPersegiPanjang(p,l)

print("Persegi Panjang")
print("Panjang\t:", p)
print("Lebar\t:", l)
print("luas\t:", luas)
