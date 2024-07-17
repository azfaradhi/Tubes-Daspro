import F00
def jackpot(user_id,monster_inventory: list,koin) -> list:
    # Spesifikasi:
    # Prosedur dan fungsi untuk bermain jackpot
    # Digunakan pada:
    # F04.py

    # parameter input:
    # user_id: string
    # monster_inventory: array of array [user_id;monster_id;level]
    # koin: int

    # output:
    # function_values: array of array

    # Inisialisasi
    koin_didapat = 0

    # Animasi awal
    print("""

░░█ ▄▀█ █▀▀ █▄▀ █▀█ █▀█ ▀█▀
█▄█ █▀█ █▄▄ █░█ █▀▀ █▄█ ░█░""")
    print()
    print("===== Daftar Item =====")
    print("1. Topi: 50 OC")
    print("2. Pedang: 100 OC")
    print("3. Koin: 200 OC")
    print("4. Potion: 300 OC")
    print("5. Monster: 500 OC")
    item_jackpot = [["Topi",50], ["Pedang",100], ["Koin",200], ["Potion",300], ["Monster",500]]
    print()

    # Permainan dimulai
    input_user = input("Mulai bermain? (y/n): ")
    while input_user != "n":
        if input_user == "y":
            print()
            print(f"Koin kamu saat ini adalah {koin} OC")
            if koin < 400 :
                print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
                break
            else:
                koin -= 400
                item_satu = ((F00.random_number())**2 + 1) % 5
                item_dua = ((F00.random_number())**3 + 2) % 5
                item_tiga = ((F00.random_number())**5  + 3) % 5
                print(f"$$$$$$$$$$      {item_jackpot[item_satu][0]} | {item_jackpot[item_dua][0]} | {item_jackpot[item_tiga][0]}      $$$$$$$$$$")
                if item_satu == item_dua == item_tiga:
                    print("JACKPOTTT!!! Monster Luffy telah dimasukkan dalam inventory anda!")
                    data_ditambah = [user_id,7,1]
                    monster_inventory.append(data_ditambah)
                    
                else:
                    koin_tambahan = item_jackpot[item_satu][1] + item_jackpot[item_dua][1] + item_jackpot[item_tiga][1]
                    koin_didapat += koin_tambahan
                    koin += koin_tambahan
                    print(f"{koin_tambahan} OC telah ditambahkan ke akun Anda!")
                input_user = input("Lanjut bermain (y/n): ")
        else:
            print("Kamu salah input!")
            input_user = input("Mulai bermain? (y/n): ")
    print(f"Kamu mendapat koin sebesar {koin_didapat} OC")
    print(f"Koin kamu saat ini adalah {koin} OC!")
    print("Selamat tinggal!")
    function_values = [monster_inventory,koin]
    return function_values