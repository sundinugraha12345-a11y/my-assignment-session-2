import math
upah= int (input("Masukkan jumlah upah per jam kerja freelance: "))
jam = int (input("Masukkan jumlah jam kerja freelance: "))
menit = int (input("Masukkan jumlah menit kerja freelance: "))

total_desimal_jam =  (menit / 60) + jam
total_upah = math.ceil (total_desimal_jam  * upah)

print ("-"*50)
print ("durasi kerja freelance: ", jam, "jam", menit, "menit")
print ("total desimal : ", total_desimal_jam, "jam")
print (f"total upah freelance: Rp {total_upah:,.0f}".replace(",", "."))
print ("-"*50)
