import math
TargetLaptop = (input("Masukkan jenis laptop yang ingin dibeli:"))
HargaLaptop = int(input("Masukkan harga laptop: "))
Tabungan = int(input("Masukkan jumlah tabungan tiap bulan: ")) 
Bulan = math.ceil(HargaLaptop / Tabungan)
print("="*50)
print(f"Jenis laptop yang ingin dibeli: {TargetLaptop}")
print("="*50)

harga= f"Rp {HargaLaptop:,.0f}".replace(",", ".")
tabungan= f"Rp {Tabungan:,.0f}".replace(",", ".")

print(f"Harga laptop: {harga}")
print(f"Tabungan tiap bulan: {tabungan}")
print("-"*50)
print(f"lama waktu yang dibutuhkan untuk membeli laptop: {Bulan} bulan")
print("="*50)


if Bulan > 12:
   print(f"tips:mungkin kamu perlu menambah jumlah tabungan tiap bulan atau mencari laptop dengan harga yang lebih terjangkau")  
else:
    print(f"semangat menabung untuk membeli laptop impianmu!")
