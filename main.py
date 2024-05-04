import time
import Fisika
import Fisika.JualBeli
import Fisika.JualBeli.jualbeli
import Fisika.MassaJenis
import Fisika.Usaha
import Fisika.energi
import Fisika.energi.energiPotensial

def batas():
    print("-"*15)
waktu_awal = time.time()
print(f"Massa Jenis = {Fisika.MassaJenis.MassaJenis(10, 2)}")
print(f"Massa = {Fisika.MassaJenis.Massa(10, 2)}")
print(f"Volume = {Fisika.MassaJenis.Volume(10, 2)}")
 

waktu_akhir = time.time()
print(f"Waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()
print(f"Usaha = {Fisika.Usaha.Usaha(12, 3)}")
print(f"Gaya = {Fisika.Usaha.Gaya(6, 2)}")
print(f"Jarak = {Fisika.Usaha.Jarak(9, 3)}")

batas()
print(f"Hasil Energi Potensial : {Fisika.energi.energiPotensial.EnergiPotensial(4, 7, 4)}")
batas()

diskon10 = Fisika.JualBeli.jualbeli.Diskon(10)
print(f"diskon 10% dari 100 adalah = {diskon10(100)}")