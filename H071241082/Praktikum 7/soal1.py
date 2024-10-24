import os
from datetime import datetime

def generate_ticket_id():
    return "TICK" + datetime.now().strftime("%d%m%Y%H%M%S")

def tampilkan_tiket(id_tiket, film, tanggal):
    garis_atas = "+--------------------------------------------+"
    garis_bawah = "+--------------------------------------------+"
    
    tiket_info = f"""
{garis_atas}
|                  TIKET BIOSKOP                |
{garis_atas}
| ID Tiket  : {id_tiket:<33} |
| Film      : {film:<33} |
| Tanggal   : {tanggal:<33} |
{garis_atas}
|     Terima kasih telah membeli tiket Anda!    |
{garis_bawah}
    """
    print(tiket_info)

# Admin: Tambah Film
def tambah_film():
    while True:
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if nama_film == "":
            break
        
        # Buat file untuk film yang baru ditambahkan
        if not os.path.exists("films"):
            os.makedirs("films")
        
        with open(f"films/{nama_film}.txt", "w") as file:
            file.write(f"Film: {nama_film}\n")
            file.write("Informasi tentang film ini akan ditambahkan kemudian.\n")
        print(f"Film '{nama_film}' berhasil ditambahkan.\n")
        print(f"File untuk film '{nama_film}' telah dibuat: films/{nama_film}.txt\n")

# Admin: Hapus Film
def hapus_film():
    while True:
        # Ambil daftar film dari folder films
        daftar_film = [f[:-4] for f in os.listdir("films") if f.endswith(".txt")]
        if len(daftar_film) == 0:
            print("Tidak ada film yang tersedia.")
            break

        print("--- Daftar Film ---")
        for idx, film in enumerate(daftar_film, 1):
            print(f"{idx}. {film}")
        print("0. Kembali")
        
        pilihan = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(daftar_film):
            film_dihapus = daftar_film[pilihan - 1]
            os.remove(f"films/{film_dihapus}.txt")
            print(f"Film '{film_dihapus}' berhasil dihapus.\n")

# Admin: Menampilkan Daftar Tiket
def daftar_tiket_admin():
    print("--- Daftar Tiket ---")
    if not os.path.exists("tickets") or len(os.listdir("tickets")) == 0:
        print("Belum ada tiket yang dibeli.\n")
    else:
        for idx, tiket_file in enumerate(os.listdir("tickets"), 1):
            with open(f"tickets/{tiket_file}", "r") as file:
                lines = file.readlines()
                id_tiket = lines[1].strip().split(": ")[1]
                film = lines[2].strip().split(": ")[1]
                tanggal = lines[3].strip().split(": ")[1]
                print(f"{idx}. ID Tiket: {id_tiket} | Film: {film} | Tanggal: {tanggal}")

# Admin: Hapus Tiket
def hapus_tiket_admin():
    while True:
        if not os.path.exists("tickets") or len(os.listdir("tickets")) == 0:
            print("Belum ada tiket yang tersedia.")
            break

        print("--- Daftar Tiket ---")
        for idx, tiket_file in enumerate(os.listdir("tickets"), 1):
            with open(f"tickets/{tiket_file}", "r") as file:
                lines = file.readlines()
                id_tiket = lines[1].strip().split(": ")[1]
                film = lines[2].strip().split(": ")[1]
                tanggal = lines[3].strip().split(": ")[1]
                print(f"{idx}. ID Tiket: {id_tiket} | Film: {film} | Tanggal: {tanggal}")

        print("0. Kembali")
        pilihan = int(input("Masukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(os.listdir("tickets")):
            tiket_dihapus = os.listdir("tickets")[pilihan - 1]
            os.remove(f"tickets/{tiket_dihapus}")  
            print(f"Tiket dengan ID '{tiket_dihapus}' berhasil dihapus.\n")

# Pengunjung: Beli Tiket
def beli_tiket():
    if not os.path.exists("films") or len(os.listdir("films")) == 0:
        print("Belum ada film yang tersedia.\n")
        return

    print("--- Daftar Film ---")
    for idx, film_file in enumerate(os.listdir("films"), 1):
        film_name = film_file[:-4]  # Menghapus .txt
        print(f"{idx}. {film_name}")
    print("0. Kembali")
    
    pilihan = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
    if pilihan == 0:
        return
    if 1 <= pilihan <= len(os.listdir("films")):
        film_dipilih = os.listdir("films")[pilihan - 1][:-4]  # Menghapus .txt
        id_tiket = generate_ticket_id()
        tanggal_beli = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        # Simpan tiket ke file teks
        if not os.path.exists("tickets"):
            os.makedirs("tickets")
        
        with open(f"tickets/{id_tiket}.txt", "w") as file:
            file.write(f"TIKET BIOSKOP\n")
            file.write(f"ID Tiket  : {id_tiket}\n")
            file.write(f"Film      : {film_dipilih}\n")
            file.write(f"Tanggal   : {tanggal_beli}\n")
            file.write("Terima kasih telah membeli tiket Anda!\n")
        
        print(f"Tiket berhasil dibeli. ID tiket Anda: {id_tiket}")
        print(f"File tiket telah dibuat: tickets/{id_tiket}.txt\n")
        tampilkan_tiket(id_tiket, film_dipilih, tanggal_beli)

# Sistem Pemesanan Tiket
def sistem_pemesanan_tiket():
    while True:
        print("--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = int(input("Pilih peran (1/2/3): "))
        
        if peran == 1:
            while True:
                print("--- Menu Admin ---")
                print("1. Tambah film")
                print("2. Hapus film")
                print("3. Daftar Tiket")
                print("4. Hapus Tiket")
                print("5. Kembali")
                opsi_admin = int(input("Pilih opsi (1/2/3/4/5): "))
                
                if opsi_admin == 1:
                    tambah_film()  
                elif opsi_admin == 2:
                    hapus_film()
                elif opsi_admin == 3:
                    daftar_tiket_admin()
                elif opsi_admin == 4:
                    hapus_tiket_admin()  
                elif opsi_admin == 5:
                    break
        
        elif peran == 2:
            while True:
                print("--- Menu Pengunjung ---")
                print("1. Lihat daftar film")
                print("2. Beli tiket")
                print("3. Kembali")
                opsi_pengunjung = int(input("Pilih opsi (1/2/3): "))
                
                if opsi_pengunjung == 1:
                    if not os.path.exists("films") or len(os.listdir("films")) == 0:
                        print("Belum ada film yang tersedia.\n")
                    else:
                        print("--- Daftar Film ---")
                        for idx, film_file in enumerate(os.listdir("films"), 1):
                            print(f"{idx}. {film_file[:-4]}")  # Menampilkan nama film tanpa .txt
                        print()
                elif opsi_pengunjung == 2:
                    beli_tiket()
                elif opsi_pengunjung == 3:
                    break
        
        elif peran == 3:
            print("Terima kasih telah menggunakan sistem ini.")
            break

sistem_pemesanan_tiket()
