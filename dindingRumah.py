import math
panjang = int(input("Masukkan panjang dinding kamar(dalam meter): "))
lebar = int(input("Masukkan lebar dinding kamar (dalam meter): "))
tinggi = int(input("Masukkan tinggi dinding kamar (dalam meter): "))

dayaSebar=10 
ukuranCat = 1.5

luasDinding = panjang * tinggi * lebar 
jumlah_cat_liter = luasDinding / dayaSebar
jumlahKalengCat = math.ceil(jumlah_cat_liter / ukuranCat)   

print("-"*50)
print(f"luas dinding kamar: {luasDinding} m2")
print(f"jumlah cat yang dibutuhkan: {jumlah_cat_liter:.0f} liter")
print(f"jumlah kaleng cat yang dibutuhkan: {jumlahKalengCat} kaleng")
print("-"*50)

