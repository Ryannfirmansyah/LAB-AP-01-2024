def cek_bahaya(langkah):
    if langkah > 20:
        return True #bhya
    return False

def main():
    total_jarak = 0
    ada_bahaya = False    
    print("Selamat datang di permainan berburu harta karun !")
    
    while True:
        try:
            langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")

            langkah = int(langkah)

            if langkah <= 0:
                break

            if cek_bahaya(langkah):
                ada_bahaya = True
                

            # Menambah jarak ke total jarak yang telah ditempuh
            total_jarak += langkah
            print(f"Total jarak: {total_jarak} meter")

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    print(f"Total jarak: {total_jarak} meter")
    if ada_bahaya:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Ada bahaya: Tidak")
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
main()