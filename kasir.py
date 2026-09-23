produk = {}

def tambah_produk():
    nama = input("Masukkan nama produk: ")
    harga = float(input("Masukkan harga produk: "))

    if nama in produk:
        print("Produk sudah ada!")
    else:
        produk[nama] = harga
        print("Produk berhasil ditambahkan.")


def lihat_produk():
    print("\n=== DAFTAR PRODUK ===")

    if not produk:
        print("Belum ada produk.")
        return

    for nama, harga in produk.items():
        print(f"Produk : {nama}")
        print(f"Harga  : Rp{harga:,.0f}")
        print("-" * 25)


def update_produk():
    nama = input("Masukkan nama produk yang ingin diubah: ")

    if nama in produk:
        harga_baru = float(input("Masukkan harga baru: "))
        produk[nama] = harga_baru
        print("Produk berhasil diubah.")
    else:
        print("Produk tidak ditemukan.")


def hapus_produk():
    nama = input("Masukkan nama produk yang ingin dihapus: ")

    if nama in produk:
        del produk[nama]
        print("Produk berhasil dihapus.")
    else:
        print("Produk tidak ditemukan.")


def hitung_total():
    nama = input("Masukkan nama produk: ")

    if nama not in produk:
        print("Produk tidak ditemukan.")
        return

    jumlah = int(input("Masukkan jumlah: "))

    harga = produk[nama]
    total = harga * jumlah

    print("\n=== TOTAL BELANJA ===")
    print(f"Produk : {nama}")
    print(f"Harga  : Rp{harga:,.0f}")
    print(f"Jumlah : {jumlah}")
    print(f"Total  : Rp{total:,.0f}")


def main():
    while True:
        print("\n=== PROGRAM KASIR SEDERHANA ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Hitung Total Belanja")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            update_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            hitung_total()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


main()