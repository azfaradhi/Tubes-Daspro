import time


def upgrade_cost(level: int) -> int:
    # Spesifikasi:
    # Banyak koin OC yang dibutuhkan untuk meng-upgrade sesuai dengan levelnya
    # Digunakan pada:
    # B05.py

    # parameter input:
    # level: int

    # output:
    # cost: int

    if level == 1:  # upgrade ke level 2
        cost = 200
    elif level == 2:  # upgrade ke level 3
        cost = 300
    elif level == 3:  # upgrade ke level 4
        cost = 600
    elif level == 4:  # upgrade ke level 5
        cost = 800
    return cost


def laboratory(user_id, user_coin: int, monster: list, monster_inventory: list):
    # Spesifikasi:
    # Meng-upgrade level dari monster yang dimiliki oleh monster
    # Digunakan pada:
    # B05.py

    # parameter input:
    # user_id: int
    # user_coin: int
    # monster: array of array [id;type;atk_power;def_power;hp]
    # monster_inventory: array of array [user_id;monster_id;level]

    # output:
    # function_value: array of array

    # Animasi awal
    print("""
█░░ ▄▀█ █▄▄ █▀█ █▀█ ▄▀█ ▀█▀ █▀█ █▀█ █▄█
█▄▄ █▀█ █▄█ █▄█ █▀▄ █▀█ ░█░ █▄█ █▀▄ ░█░""")
    print()
    time.sleep(1)
    print("Selamat datang di Lab Agent!!")
    time.sleep(1)
    print("""                   ,
                   |'.             ,
                   |  '-._        / )
                 .'  .._  ',     /_'-,
                '   /  _'.'_\   /._)')
               :   /  '_' '_'  /  _.'
               |E |   |Q| |Q| /   /
              .'  _\  '-' '-'    /
            .'--.(S     ,__` )  /
                  '-.     _.'  /
                __.--'----(   /
            _.-'     :   __\ /
           (      __.' :'  :Y
            '.   '._,  :   :|
              '.     ) :.__:|
                \    \______/
                 '._L/_H____]
                  /_        /
                 /  '-.__.-')
                :      /   /
                :     /   /
              ,/_____/----;
              '._____)----'
              /     /   /
             /     /   /
           .'     /    \ 
          (______(-.____)""")
    print("Perkenalkan, namaku Mark! Disini aku akan membantu kamu untuk meng-upgrade monster yang kamu miliki!")
    time.sleep(1)
    print("Pertama-tama, aku akan menampilkan semua monster yang kamu miliki!")
    time.sleep(1)

    # Menampilkan daftar monster yang dimiliki agent
    print("======= MONSTER LIST =======")
    list_index = []
    list_id_monster = []
    enumerate = 1
    for row in range(len(monster_inventory)):
        if str(monster_inventory[row][0]) == str(user_id):
            idx_monster = str(monster_inventory[row][1])
            for i in range(len(monster)):
                if str(monster[i][0]) == idx_monster:
                    list_id_monster.append(idx_monster)
                    list_index.append(enumerate)
                    print(
                        f"{enumerate}. {monster[i][1]} (Level: {monster_inventory[row][2]})")
            enumerate += 1
    print()

    # Algoritma conditional masukkan pengguna
    while True:
        print(f"Koinmu saat ini: {user_coin}")
        print()
        print("Silahkan pilih monster yang ingin di Upgrade!")
        print("Pilih monster: ")
        selected_monster_index = input(">>> ")
        print()
        cek_valid = False
        while cek_valid == False:
            time.sleep(0.5)
            if selected_monster_index not in str(list_index):
                print("Pilihan monster tidak valid. Silakan pilih lagi.")
                print("Pilih monster: ")
                selected_monster_index = input(">>> ")
            else:
                cek_valid = True
                selected_monster = list_id_monster[int(
                    selected_monster_index) - 1]
                for index in range(len(monster_inventory)):
                    if str(monster_inventory[index][0]) == str(user_id) and str(monster_inventory[index][1]) == str(selected_monster):
                        idx_monster_di_inventory = index
                for index2 in range(len(monster)):
                    if str(monster[index2][0]) == str(selected_monster):
                        idx_monster_di_database = index2
        # Jika monster belum mencapai level maksimum 5
        if int(monster_inventory[idx_monster_di_inventory][2]) < 5:
            next_level = int(
                monster_inventory[idx_monster_di_inventory][2]) + 1
            print(
                f'{monster[idx_monster_di_database][1]} akan di-upgrade ke level {next_level}')
            level = int(monster_inventory[idx_monster_di_inventory][2])
            # memanggil fungsi harga_upgrade untuk menampilkan harga
            cost = upgrade_cost(level)
            print(f'Harga untuk melakukan upgrade adalah {cost} OC.\n')

            while True:
                upgrade = input('>>> Lanjutkan upgrade (Y/N): ').lower()
                if upgrade == 'y':
                    if user_coin >= cost:
                        # menambahkan level monster
                        monster_inventory[idx_monster_di_inventory][2] = str(next_level)
                        user_coin -= cost  # memotong O.W.C.A Coin setelah melakukan upgrade
                        print()
                        print(
                            f"Selamat, {monster[idx_monster_di_database][1]} berhasil di-upgrade ke level {next_level}!")
                        print()
                        break
                    else:
                        print(
                            "Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.\n")
                        break
                elif upgrade == 'n':
                    print("Upgrade dibatalkan.\n")
                    break
                else:
                    print("Input tidak valid. Upgrade dibatalkan.\n")

        else:  # jika monster yang dipilih sudah mencapai level 5 (maks)
            print(f"Maaf, monster yang Anda pilih sudah memiliki level maksimum.\n")

        print("Apakah kamu ingin melanjutkan upgrade?")
        print('Ketik nomor dari pilihan berikut')
        print('1. Lanjut upgrade')
        print('2. Keluar\n')

        opt = input('>>> ')
        while opt != '1' and opt != '2':
            print('Perintah tidak dikenal!')
            print('1. Lanjut upgrade')
            print('2. Keluar\n')
            opt = input('>>> ')

        if opt == '2':
            print("""
               ________________
              |                |
              |   Thankyou...  |
              |________________|
                  /
     _.-----._
   _'    '    '_
  '_____________'
      | +_+ |
  ==--'_D__,'---==.
 /    > \_/ <     |
/  >__\o_| o/     |
|      | |_/    , |
\,_____/_)  o   | |
   |   o '  o   | |
   |   o |  o   |_/|
   '   o |  o   '  |
   |   o |  o   |_/
   |   o |  o   |))
   |     |      |
   |     \      |
   |___o/ \_____|
     |   |   |
   __)  >|<  (__
  (____,_|_,____) """)
            print(f"Koinmu saat ini: {user_coin}")
            print('Sampai jumpa lagi di Lab!\n')
            break
    function_value = [user_coin, monster_inventory]
    return function_value
