import math
jumlahOrang = int(input("Masukkan jumlah orang yang di dalam rumah: "))

galonBerisi = 19
minumPerhari = 2.5
hargaGalon = 19000
perminggu = 7

total_Liter_Perminggu = minumPerhari * perminggu * jumlahOrang
jumlah_galon_Perminggu =  math.ceil(total_Liter_Perminggu / galonBerisi)
totalBiaya= jumlah_galon_Perminggu * hargaGalon

print("-"*50)
print("Total liter yang dikonsumsi per minggu: ", total_Liter_Perminggu, "liter")
print("Jumlah galon yang dibutuhkan per minggu: ", jumlah_galon_Perminggu, "galon")
print(f"Total biaya yang harus dikeluarkan per minggu: Rp {totalBiaya:,.0f}".replace(",", "."))
print("-"*50)
