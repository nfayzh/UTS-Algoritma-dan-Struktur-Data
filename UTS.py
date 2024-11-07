from tabulate import tabulate

# Data barang di toko ATK
barang = {
    "Pensil": {"harga": 5000, "stok": 10},
    "Buku": {"harga": 7500, "stok": 5},
    "Penggaris": {"harga": 12000, "stok": 4},
    "Pulpen": {"harga": 5500, "stok": 10},
    "Buku Gambar": {"harga": 4000, "stok": 7},
    "Pensil Warna": {"harga": 15000, "stok": 5}
}

# Fungsi untuk menampilkan daftar barang dalam bentuk tabel
def tampilkan_daftar_barang():
    print("\nDaftar Barang di Toko ATK LN:")
    tabel_data = [[nama, f"Rp. {info['harga']}", info['stok']] for nama, info in barang.items()]
    print(tabulate(tabel_data, headers=["Nama Barang", "Harga Satuan", "Stok"], tablefmt="grid"))

# Variabel untuk menyimpan total belanja
total_belanja = 0  

# Menampilkan daftar barang
tampilkan_daftar_barang()

# Loop untuk melakukan pembelian beberapa barang
while True:
    # Input dari pengguna
    nama_barang = input("\nMasukkan nama barang yang ingin dibeli: ")
    
    if nama_barang not in barang:
        print("Barang tidak ditemukan di toko.")
        continue  # Kembali ke awal loop jika barang tidak ditemukan

    try:
        jumlah = int(input(f"Masukkan jumlah {nama_barang} yang ingin dibeli: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        continue  # Kembali ke awal loop jika input jumlah tidak valid
    
    harga_satuan = barang[nama_barang]["harga"]
    stok_tersedia = barang[nama_barang]["stok"]
    
    # Mengecek stok
    if jumlah <= stok_tersedia:
        total_harga = harga_satuan * jumlah
        total_belanja += total_harga
        barang[nama_barang]["stok"] -= jumlah  # Mengurangi stok setelah transaksi berhasil
        print(f"Anda membeli {jumlah} {nama_barang} dengan total harga Rp. {total_harga}")
        
        # Mengecek apakah stok habis setelah pembelian
        if barang[nama_barang]["stok"] == 0:
            print(f"Stok {nama_barang} habis")
    else:
        print(f"Stok {nama_barang} tidak mencukupi (stok tersedia: {stok_tersedia})")

    # Menanyakan apakah ingin membeli barang lain
    beli_lagi = input("Apakah Anda ingin membeli barang lain? (ya/tidak): ").strip().lower()
    if beli_lagi != 'ya':
        break  # Keluar dari loop jika pengguna tidak ingin membeli lagi

# Menampilkan total belanja setelah selesai
print(f"\nTotal belanja Anda: Rp. {total_belanja}")
print("Terima kasih telah berbelanja di Toko ATK LN!")

# Menampilkan sisa stok barang setelah semua transaksi selesai
tampilkan_daftar_barang()