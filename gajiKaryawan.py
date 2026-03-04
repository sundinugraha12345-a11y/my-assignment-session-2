GajiPokok = 5000000
Tunjangan = 750000

GajiKotor = GajiPokok + Tunjangan

PotonganPajak = 5 / 100
PotonganBPJS = 2 / 100
TotalPersen = PotonganPajak + PotonganBPJS

TotalPotongan = GajiKotor * TotalPersen

GajiBersih = GajiKotor - TotalPotongan
print("total gaji karyawan RP: ", GajiBersih)





