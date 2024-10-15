
inventory = []

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))
    barang = {"nama": nama, "jumlah": jumlah, "harga": harga}
    inventory.append(barang)
    print(f"Barang '{nama}' berhasil ditambahkan.\n")

def hapus_barang():
    nama = input("Masukkan nama barang yang akan dihapus: ")
    for barang in inventory:
        if barang["nama"].lower() == nama.lower():
            inventory.remove(barang)
            print(f"Barang '{nama}' berhasil dihapus.\n")
            return
    print(f"Barang '{nama}' tidak ditemukan.\n")

def tampilkan_barang():
    if len(inventory) == 0:
        print("Tidak ada barang dalam inventory.\n")
    else:
        print("Daftar Barang:")
        for idx, barang in enumerate(inventory, start=1):
            print(f"{idx}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
        
def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    for barang in inventory:
        if barang["nama"].lower() == nama.lower():
            print(f"Barang ditemukan: Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}\n")
            return
    print(f"Barang '{nama}' tidak ditemukan.\n")

def update_barang():
    nama = input("Masukkan nama barang yang akan diupdate: ")
    for barang in inventory:
        if barang["nama"].lower() == nama.lower():
            barang["jumlah"] = int(input("Masukkan jumlah baru: "))
            barang["harga"] = float(input("Masukkan harga baru: "))
            print(f"Data barang '{nama}' berhasil diupdate.\n")
            return
    print(f"Barang '{nama}' tidak ditemukan.\n")

def tampilkan_menu():
    print("=== Program Inventory Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
main()