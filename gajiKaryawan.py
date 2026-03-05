gajiPokok  = 5000000
tunjangan  = 750000

gajiKotor = gajiPokok + tunjangan

potonganPajak = 5 / 100
potonganBPJS = 2 / 100
persen = potonganPajak + potonganBPJS

totalPotongan =  gajiKotor * persen

gajiBersih = gajiKotor - totalPotongan
print("-"*50)
print(f"total bersih gaji karyawan: RP {gajiBersih:,.0f}".replace(",", "."))
print("-"*50)