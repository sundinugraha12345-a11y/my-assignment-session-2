TotalTagihan = 347.500
jumlahOrang = 4
tagihanPerOrang = TotalTagihan / jumlahOrang
pajak=10/100
totalYangDibayarPerorang = tagihanPerOrang + (tagihanPerOrang * pajak)
totalPajak = TotalTagihan * pajak
totalSeluruhYangHarusDibayar = totalPajak + TotalTagihan
print("Total tagihan per orang: Rp", totalYangDibayarPerorang)
print("Total seluruh yang harus dibayar: Rp", totalSeluruhYangHarusDibayar)