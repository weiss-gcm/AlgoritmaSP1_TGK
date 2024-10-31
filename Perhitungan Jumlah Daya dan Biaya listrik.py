
#DAYA SAMA TOTAL WAKTU DIGUNAKAN LAMPU
daya_tv = int(input("Jumlah Penggunaan Daya TV (dalam Watt): "))
waktu_tv = int(input("Jumlah waktu digunakan TV (jam/hari): "))
#DAYA SAMA TOTAL WAKTU DIGUNAKAN LAMPU
daya_kipas = int(input("Jumlah Penggunaan Daya Kipas (dalam Watt): "))
waktu_kipas = int(input("Jumlah waktu digunakan Kipas (jam/hari): "))
#DAYA SAMA TOTAL WAKTU DIGUNAKAN LAMPU
daya_lampu = int(input("Jumlah Penggunaan Daya Lampu (dalam Watt): "))
waktu_lampu = int(input("Jumlah waktu digunakan lampu (jam/hari): "))

#HARGA LISTRIK PER KWH
hrg = int(input("Harga per kWh: "))

#HITUNGAN DAYA BARANG DIKALI DENGAN JUMLAH WAKTU DIGUNAKAN PER JAM
hasil1 = daya_tv * waktu_tv
hasil2 = daya_kipas * waktu_kipas
hasil3 = daya_lampu * waktu_lampu

# DIGUNAKAN UNTUK MENJUMLAKAN KESELURUHAN KWH DARI TIAP BARANG ELEKTRONIK
hasil = hasil1 + hasil2 + hasil3

#KONVERSI DARI WATT KE KILOWATT
kwh = hasil / 1000   
tv_kwh = hasil1 / 1000
kipas_kwh = hasil2 / 1000
lampu_kwh = hasil3 / 1000

#JUMLAH PENGGUNAAN KWH DIKALI DENGAN HARGA
harga_total_1hari = kwh * hrg

#HARGA TOTAL PER HARI DIKALI 30 UNTUK MENENTUKAN JUMLAH BIAYA DALAM 1 BULAN
harga_total_1bulan = harga_total_1hari * 30  

#PENGGUNAAN 2F AGAR HASIL INTERGER DI OUTPUT AKAN DIRUBAH MENJADI FLOATING POINT DENGAN PRESISI 2 DESIMAL
print()
print("Apabila dihitung perhari")
print(f"Penggunaan daya TV per hari: {tv_kwh:.2f} kWh")
print(f"Penggunaan daya Kipas per hari: {kipas_kwh:.2f} kWh")
print(f"Penggunaan daya Lampu per hari: {lampu_kwh:.2f} kWh")
print(f"Biaya listrik TV per hari:Rp {tv_kwh * hrg:.2f}")
print(f"Biaya listrik Kipas per hari: Rp {kipas_kwh * hrg:.2f}")
print(f"Biaya listrik Lampu per hari: Rp {lampu_kwh * hrg:.2f}")
print(f"Harga total penggunaan daya eletronik keseluruhan jika dihitung per hari: Rp {harga_total_1hari:.2f}")
print()
print("Apabila dihitung perbulan")
print(f"Total daya Barang TV per bulan: {tv_kwh * 30:2f} kWh")
print(f"Total daya Barang Kipas per bulan: {kipas_kwh * 30:2f} kWh")
print(f"Total daya Barang Lampu per bulan: {lampu_kwh * 30:2f} kWh ")
print(f"Biaya listrik TV per bulan: Rp {lampu_kwh * 30:2f}")
print(f"Biaya listrik Kipas per bulan: Rp {lampu_kwh * 30:2f}")
print(f"Biaya listrik Lampu per bulan: Rp {lampu_kwh * 30:2f}")
print(f"Harga total penggunaan daya elektronik keseluruhan per bulan: Rp {harga_total_1bulan:.2f}")

