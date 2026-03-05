perjalanan= int(input("Masukkan jarak perjalanan (dalam km): "))
hargaBensin = int(input("Masukkan harga bensin per liter: "))
konsumsiBensin = int(input("Masukkan konsumsi bensin kendaraan (km per liter): "))

totalBensin = perjalanan / konsumsiBensin
totalBiaya = totalBensin * hargaBensin

print("-"*50)
print(f"Jarak perjalanan: {perjalanan} km")
print(f"Total bensin yang dibutuhkan: {totalBensin:.0f} liter")
print(f"Total biaya perjalanan: Rp {totalBiaya:,.0f}".replace(",", "."))
print("-"*50)
