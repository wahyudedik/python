# kalkulator.py

def kalkulator():
    print("=== KALKULATOR SEDERHANA ===")

    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "5":
            print("Program selesai.")
            break

        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid!")
            continue

        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == "1":
                hasil = angka1 + angka2
            elif pilihan == "2":
                hasil = angka1 - angka2
            elif pilihan == "3":
                hasil = angka1 * angka2
            elif pilihan == "4":
                if angka2 == 0:
                    print("Error: Tidak bisa membagi dengan nol!")
                    continue
                hasil = angka1 / angka2

            print(f"Hasil: {hasil}")

        except ValueError:
            print("Input harus berupa angka!")


kalkulator()
