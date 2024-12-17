def hitung_diskon():
    print("Apakah Anda punya kartu member? (ya/tidak)")
    kartu_member = input().strip().lower()

    if kartu_member == "ya":
        belanja = float(input("Masukkan total belanjaan Anda: "))

        if belanja > 500000:
            diskon = 50000
        elif belanja > 100000:
            diskon = 15000
        else:
            diskon = 0

    elif kartu_member == "tidak":
        belanja = float(input("Masukkan total belanjaan Anda: "))

        if belanja <= 100000:
            diskon = 10000
        else:
            diskon = 0

    else:
        print("Input tidak valid. Silakan mulai ulang.")
        return

    print(f"Total belanja Anda: {belanja}")
    print(f"Diskon yang Anda dapatkan: {diskon}")
    print(f"Total yang harus dibayar: {belanja - diskon}")

# Mmenghitung diskon
hitung_diskon()
def hitung_diskon():
    print("Apakah Anda punya kartu member? (ya/tidak)")
    kartu_member = input().strip().lower()

    if kartu_member == "ya":
        belanja = float(input("Masukkan total belanjaan Anda: "))

        if belanja > 500000:
            diskon = 50000
        elif belanja > 100000:
            diskon = 15000
        else:
            diskon = 0

    elif kartu_member == "tidak":
        belanja = float(input("Masukkan total belanjaan Anda: "))

        if belanja <= 100000:
            diskon = 10000
        else:
            diskon = 0

    else:
        print("Input tidak valid. Silakan mulai ulang.")
        return

    print(f"Total belanja Anda: {belanja}")
    print(f"Diskon yang Anda dapatkan: {diskon}")
    print(f"Total yang harus dibayar: {belanja - diskon}")

# print diskon
hitung_diskon()
