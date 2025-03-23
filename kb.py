import random
import datetime

# Daftar barang yang tersedia
daftar_barang = {
    "1": {"nama": "Beras", "harga": 12000},
    "2": {"nama": "Gula", "harga": 15000},
    "3": {"nama": "Minyak Goreng", "harga": 18000},
    "4": {"nama": "Susu", "harga": 25000}
}

keranjang = []

def tampilkan_menu():
    print("\nDaftar Barang:")
    for key, barang in daftar_barang.items():
        print(f"{key}. {barang['nama']} - Rp{barang['harga']}")

def tambah_ke_keranjang():
    kode = input("Masukkan kode barang yang ingin dibeli: ")
    if kode in daftar_barang:
        jumlah = int(input(f"Masukkan jumlah {daftar_barang[kode]['nama']}: "))
        keranjang.append({"nama": daftar_barang[kode]["nama"], "harga": daftar_barang[kode]["harga"], "jumlah": jumlah})
        print(f"{daftar_barang[kode]['nama']} berhasil ditambahkan ke keranjang.")
    else:
        print("Kode barang tidak ditemukan!")

def tampilkan_keranjang():
    if not keranjang:
        print("Keranjang belanja kosong.")
    else:
        print("\nKeranjang Belanja:")
        total = 0
        for barang in keranjang:
            subtotal = barang['harga'] * barang['jumlah']
            total += subtotal
            print(f"{barang['nama']} - {barang['jumlah']} x Rp{barang['harga']} = Rp{subtotal}")
        print(f"Total Belanja: Rp{total}")

def lakukan_pembayaran():
    if not keranjang:
        print("Tidak ada barang di keranjang untuk dibayar.")
        return
    
    tampilkan_keranjang()
    uang = int(input("Masukkan jumlah uang: "))
    total = sum(barang['harga'] * barang['jumlah'] for barang in keranjang)
    if uang >= total:
        kembalian = uang - total
        print(f"Pembayaran berhasil! Kembalian Anda: Rp{kembalian}")
        transaksi_id = random.randint(1000, 9999)
        waktu_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"ID Transaksi: {transaksi_id} | Waktu: {waktu_transaksi}")
        keranjang.clear()
    else:
        print("Uang tidak mencukupi! Silakan coba lagi.")

while True:
    print("\nMenu:")
    print("1. Tampilkan daftar barang")
    print("2. Tambah barang ke keranjang")
    print("3. Lihat keranjang belanja")
    print("4. Bayar")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_menu()
    elif pilihan == "2":
        tambah_ke_keranjang()
    elif pilihan == "3":
        tampilkan_keranjang()
    elif pilihan == "4":
        lakukan_pembayaran()
    elif pilihan == "5":
        print("Terima kasih telah berbelanja!")
        break
    else:
        print("Pilihan tidak valid!")
