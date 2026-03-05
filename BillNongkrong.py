
totalTagihan = 347500
jumlahOrang = 4
tagihanPerOrang = totalTagihan / jumlahOrang
pajak=10/100

total_yang_dibayar_perorang = tagihanPerOrang + (tagihanPerOrang * pajak)
totalPajak = totalTagihan * pajak
total_seluruh_yang_harus_dibayar = totalPajak + totalTagihan

print("="*50)
print(f"Total tagihan per orang: Rp {total_yang_dibayar_perorang:,.0f}".replace(",", "."))
print(f"Total seluruh yang harus dibayar: Rp {total_seluruh_yang_harus_dibayar:,.0f}".replace(",", "."))
print("="*50)