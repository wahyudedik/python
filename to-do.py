daftar_tugas = []

def tambah_tugas():
    nama_tugas = input("Masukkan nama tugas baru: ")
    # Menyimpan tugas dalam bentuk dictionary ke dalam list
    daftar_tugas.append({
        "nama": nama_tugas, 
        "selesai": False
    })
    print("Tugas berhasil ditambahkan.")

def lihat_tugas():
    print("\n=== DAFTAR TO-DO LIST ===")
    
    if not daftar_tugas:
        print("Belum ada tugas saat ini.")
        return

    for index, tugas in enumerate(daftar_tugas):
        status = "[X]" if tugas["selesai"] else "[ ]"
        print(f"{index + 1}. {status} {tugas['nama']}")
    print("-" * 25)

def tandai_selesai():
    lihat_tugas()
    if not daftar_tugas:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang sudah selesai: "))
        
        if 1 <= nomor <= len(daftar_tugas):
            # Mengubah status 'selesai' menjadi True
            daftar_tugas[nomor - 1]["selesai"] = True
            print("Tugas berhasil ditandai sebagai selesai.")
        else:
            print("Nomor tugas tidak ditemukan.")
    except ValueError:
        print("Error: Input harus berupa angka!")

def hapus_tugas():
    lihat_tugas()
    if not daftar_tugas:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        
        if 1 <= nomor <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor - 1)
            print(f"Tugas '{tugas_dihapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak ditemukan.")
    except ValueError:
        print("Error: Input harus berupa angka!")

def main():
    while True:
        print("\n=== APLIKASI MANAJEMEN TUGAS ===")
        print("1. Tambah Tugas")
        print("2. Lihat Semua Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            tandai_selesai()
        elif pilihan == "4":
            hapus_tugas()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")

if __name__ == "__main__":
    main()