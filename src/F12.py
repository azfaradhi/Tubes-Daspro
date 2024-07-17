import time


def is_integer(n: str) -> bool:
    # Spesifikasi:
    # Memvalidasi jika suatu input merupakan bilangan
    # Digunakan pada:
    # F12.py

    # parameter input:
    # n: str

    # output:
    # cek: bool

    # Inisialisasi
    cek = True
    # Algoritma pengecekan
    for char in str(n):
        if ord(char) not in range(48, 58):
            if ord(char) != 45:
                cek = False
    return cek


def validasi_int(n: str, tipe: str) -> str:
    # Spesifikasi:
    # Prosedur dan fungsi yang meminta pengguna untuk memasukkan input yang valid
    # Digunakan pada:
    # F12.py

    # parameter input:
    # n: str
    # tipe: str

    # output:
    # n: str

    while True:
        if is_integer(n) == True:
            break
        else:
            print("Input yang dimasukkan tidak valid!")
            n = input(f"Masukkan {tipe}: ")
    return n


def shop_management(monster_shop: list, item_shop: list, monster: list, item_inventory: list) -> list:
    # Spesifikasi:
    # Prosedur dan fungsi untuk merubah monster dan potion yang ada di shop
    # Digunakan pada:
    # F04.py

    # parameter input:
    # monster_shop: array of array [monster_id;stock;price]
    # item_shop: array of array [type;stock;price]
    # monster: array of array [id;type;atk_power;def_power;hp]
    # item_inventory: array of array [user_id;type;quantity]

    # output:
    # function_values: array of array

    # Animasi awal
    time.sleep(1)
    print("==========================================")
    time.sleep(1)
    print("""

█▀ █░█ █▀█ █▀█   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀
▄█ █▀█ █▄█ █▀▀   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █░▀░█ ██▄ █░▀█ ░█░""")
    print()
    time.sleep(1)
    print("==========================================")

    time.sleep(1)
    print("Konichiwa :D, Selamat datang kembali Admin!")
    time.sleep(1)

    # Meminta admint untuk memilih command
    aksi_user = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")

    while True:
        # Inisialisasi
        list_item = ["strength", "resilience", "healing"]
        id_monster = []
        for i in range(len(monster_shop)):
            id_monster.append(monster_shop[i][0])

        # Jika command yang dipilih adalah lihat
        if aksi_user == "lihat":
            tipe_dilihat = input("Mau lihat apa? (monster/potion/back): ")
            if tipe_dilihat == "monster":
                print(
                    "ID        |Type      |ATK Power |DEF Power |HP        |Stok      |Harga     |")
                print(
                    "----------|----------|----------|----------|----------|----------|----------|")
                for row in monster:
                    if str(row[0]) in str(id_monster):
                        for char in row:
                            length_char = len(str(char))
                            print(str(char) + " "*(10-length_char), end="|")
                        for row2 in monster_shop:
                            if str(row2[0]) == str(row[0]):
                                length_row2 = len(str(row2[1]))
                                length_row3 = len(str(row2[2]))
                                print(str(row2[1]) + " "*(10-length_row2) + "|" +
                                      str(row2[2]) + " "*(10-length_row3) + "|", end="")
                        print()
            elif tipe_dilihat == "potion":
                print("ID |Type           |Stok           |Harga          |")
                print("---|---------------|---------------|---------------|")
                i = 1
                for row in item_shop:
                    print(i, end="  |")
                    i += 1
                    for char in row:
                        length_char = len(str(char))
                        print(str(char) + " "*(15-length_char), end="|")
                    print()
            elif tipe_dilihat == "back":
                pass
            else:
                print("Input yang dimasukkan tidak valid!")
        # Jika command yang dipilih adalah tambah
        elif aksi_user == "tambah":
            tipe_dilihat = input("Mau tambah apa? (monster/potion/back): ")
            if tipe_dilihat == "monster":
                print("ID        |Type      |ATK Power |DEF Power |HP        |")
                print("----------|----------|----------|----------|----------|")
                for row in monster:
                    if str(row[0]) not in str(id_monster):
                        for char in row:
                            length_char = len(str(char))
                            print(str(char) + " "*(10-length_char), end="|")
                        print()
                print("Jika tidak jadi menambahkan, silahkan ketik 'cancel'")
                input_id_ditambah = input("Masukkan id monster: ")
                cek_valid = False
                while cek_valid == False:
                    if is_integer(input_id_ditambah) == True:
                        for row in range(len(monster)):
                            if int(monster[row][0]) == int(input_id_ditambah) and str(input_id_ditambah) not in str(id_monster):
                                cek_valid = True
                        if cek_valid == False:
                            print(
                                "ID yang kamu masukan tidak valid! ayo masukan id lagi!")
                            input_id_ditambah = input("Masukkan id monster: ")
                        elif cek_valid == True:
                            stok_awal_ditambah = input("Masukkan stok: ")
                            stok_awal_ditambah = validasi_int(
                                stok_awal_ditambah, "stok")
                            harga_ditambah = input("Masukkan harga: ")
                            harga_ditambah = validasi_int(
                                harga_ditambah, "harga")
                            data_ditambah = [int(input_id_ditambah), int(
                                stok_awal_ditambah), int(harga_ditambah)]
                            monster_shop.append(data_ditambah)
                            id_monster.append(int(input_id_ditambah))
                            print("Monster berhasil ditambah!")
                    else:
                        if input_id_ditambah == "cancel":
                            break
                        else:
                            print("Input yang dimasukkan tidak valid!")
                            input_id_ditambah = input("Masukkan id monster: ")

            elif tipe_dilihat == "potion":
                idx_i = []
                print("ID |Type           ")
                print("---|---------------")
                for i in range(len(list_item)):
                    if str(list_item[i]) not in str(item_shop):
                        print(f"{i+1}  | {list_item[i]}")
                        idx_i.append(i)
                print("Jika tidak jadi menambahkan, silahkan ketik 'cancel'")
                input_id_tambah_item = input("Masukkan id potion: ")
                cek_valid = False
                while cek_valid == False:
                    if is_integer(input_id_tambah_item) == True:
                        if (int(input_id_tambah_item)-1 in idx_i):
                            cek_valid = True
                            input_stok_tambah_item = input(
                                "Masukkan stok awal: ")
                            input_stok_tambah_item = validasi_int(
                                input_stok_tambah_item, "stok")
                            input_harga_tambah_item = input("Masukkan harga: ")
                            input_harga_tambah_item = validasi_int(
                                input_harga_tambah_item, "harga")
                            data_ditambah = [list_item[int(
                                input_id_tambah_item)-1], int(input_stok_tambah_item), int(input_harga_tambah_item)]
                            item_shop.append(data_ditambah)
                            print("Item berhasil ditambahkan!")
                        else:
                            print(
                                "ID yang kamu masukan tidak valid! ayo masukan id lagi!")
                            input_id_tambah_item = input(
                                "Masukkan id potion: ")
                            input_id_tambah_item = validasi_int(
                                input_id_tambah_item, "id potion")
                    else:
                        if input_id_tambah_item == "cancel":
                            break
                        else:
                            print("Input yang dimasukkan tidak valid")
                            input_id_tambah_item = input(
                                "Masukkan id potion: ")
                            input_id_tambah_item = validasi_int(
                                input_id_tambah_item, "id potion")
            elif tipe_dilihat == "back":
                pass
            else:
                print("Input yang dimasukkan tidak valid!")

        # Jika command yang dipilih adalah ubah
        elif aksi_user == "ubah":
            tipe_diubah = input("Mau ubah apa? (monster/potion/back): ")
            if tipe_diubah == "monster":
                print(
                    "ID        |Type      |ATK Power |DEF Power |HP        |Stok      |Harga     |")
                print(
                    "----------|----------|----------|----------|----------|----------|----------|")
                for row in monster:
                    if str(row[0]) in str(id_monster):
                        for char in row:
                            length_char = len(str(char))
                            print(str(char) + " "*(10-length_char), end="|")
                        for row2 in monster_shop:
                            if str(row2[0]) == str(row[0]):
                                length_row2 = len(str(row2[1]))
                                length_row3 = len(str(row2[2]))
                                print(str(row2[1]) + " "*(10-length_row2) + "|" +
                                      str(row2[2]) + " "*(10-length_row3) + "|", end="")
                        print()
                print("Jika tidak jadi mengubah, silahkan ketik -1")
                input_id_diubah = input("Masukkan id monster: ")
                input_id_diubah = validasi_int(input_id_diubah, "id monster")
                cek_valid = False
                while cek_valid == False:
                    if input_id_diubah == "-1":
                        break
                    else:
                        for row in range(len(monster_shop)):
                            if input_id_diubah == str(monster_shop[row][0]):
                                cek_valid = True
                        if cek_valid == False:
                            print(
                                "ID yang kamu masukan tidak valid! ayo masukan id lagi!")
                            input_id_diubah = input("Masukkan id monster: ")
                        elif cek_valid == True:
                            stok_monster_diubah = input("Masukkan stok baru: ")
                            stok_monster_diubah = validasi_int(
                                stok_monster_diubah, "stok baru")
                            harga_monster_diubah = input(
                                "Masukkan harga baru: ")
                            harga_monster_diubah = validasi_int(
                                harga_item_diubah, "harga baru")
                            for row in range(len(monster_shop)):
                                if str(monster_shop[row][0]) == str(input_id_diubah):
                                    monster_shop[row][1] = int(
                                        stok_monster_diubah)
                                    monster_shop[row][2] = int(
                                        harga_monster_diubah)
                                    print('Monster berhasil diubah!')

            elif tipe_diubah == "potion":
                idx_i = []
                print("ID |Type           |Stok           |Harga          |")
                print("---|---------------|---------------|---------------|")
                i = 1
                for row in item_shop:
                    print(i, end="  |")
                    idx_i.append(i)
                    for char in row:
                        length_char = len(str(char))
                        print(str(char) + " "*(15-length_char), end="|")
                    i += 1
                    print()
                print("Jika tidak jadi menambahkan, silahkan ketik -1")
                input_id_diubah = input("Masukkan id potion: ")
                input_id_diubah = validasi_int(input_id_diubah, "id potion")
                cek_valid = False
                while cek_valid == False:
                    if input_id_diubah == "-1":
                        break
                    else:
                        if (input_id_diubah in str(idx_i)):
                            cek_valid = True
                            stok_item_diubah = input("Masukkan stok baru: ")
                            stok_item_diubah = validasi_int(stok_item_diubah, "stok baru")
                            harga_item_diubah = input("Masukkan harga baru: ")
                            harga_item_diubah = validasi_int(
                                harga_item_diubah, "harga baru")
                            item_shop[int(input_id_diubah)-1][1] = stok_item_diubah
                            item_shop[int(input_id_diubah)-1][2] = harga_item_diubah
                            print("Item telah berhasil diubah!")
                        else:
                            print(
                                "ID yang kamu masukan tidak valid! ayo masukan id lagi!")
                            input_id_diubah = input("Masukkan id potion: ")
                            input_id_diubah = validasi_int(
                                input_id_diubah, "id potion")

            elif tipe_dilihat == "back":
                pass
            else:
                print("Input yang dimasukkan tidak valid!")

        # Jika command yang dipilih adalah hapus
        elif aksi_user == "hapus":
            tipe_dihapus = input("Mau hapus apa? (monster/potion/back): ")
            if tipe_dihapus == "monster":
                print(
                    "ID        |Type      |ATK Power |DEF Power |HP        |Stok      |Harga     |")
                print(
                    "----------|----------|----------|----------|----------|----------|----------|")
                for row in monster:
                    if str(row[0]) in str(id_monster):
                        for char in row:
                            length_char = len(char)
                            print(str(char) + " "*(10-length_char), end="|")
                        for row2 in monster_shop:
                            if str(row2[0]) == str(row[0]):
                                length_row2 = len(str(row2[1]))
                                length_row3 = len(str(row2[2]))
                                print(str(row2[1]) + " "*(10-length_row2) + "|" +
                                      str(row2[2]) + " "*(10-length_row3) + "|", end="")
                        print()
                print("Jika tidak jadi menghapus, silahkan ketik -1")
                input_id_dihapus = input("Masukkan id monster: ")
                input_id_dihapus = validasi_int(input_id_dihapus, "id monster")
                cek_valid = False
                while cek_valid == False:
                    if input_id_dihapus == "-1":
                        break
                    else:
                        for row in range(len(monster_shop)):
                            if str(input_id_dihapus) == str(monster_shop[row][0]):
                                cek_valid = True
                        if cek_valid == False:
                            print(
                                "ID yang kamu masukan tidak valid! ayo masukan id lagi!")
                            input_id_dihapus = input("Masukkan id monster: ")
                            input_id_dihapus = validasi_int(
                                input_id_dihapus, "id monster")
                        elif cek_valid == True:
                            validasi_input_hapus = input(
                                "Apakah anda yakin (y/n)? ")
                            if validasi_input_hapus == "y":
                                for row in range(len(monster_shop)):
                                    if str(monster_shop[row][0]) == str(input_id_dihapus):
                                        monster_shop.pop(row)
                                        print("Monster berhasil dihapus!")
                                        break
                            elif validasi_input_hapus == "n":
                                print("Baik!")
                                pass

            elif tipe_dihapus == "potion":
                idx_i = []
                print("ID |Type           |Stok           |Harga          |")
                print("---|---------------|---------------|---------------|")
                i = 1
                for row in item_shop:
                    print(i, end="  |")
                    idx_i.append(i)
                    for char in row:
                        length_char = len(str(char))
                        print(str(char) + " "*(15-length_char), end="|")
                    i += 1
                    print()
                print("Jika tidak jadi menambahkan, silahkan ketik -1")
                input_id_dihapus = input("Masukkan id potion: ")
                input_id_dihapus = validasi_int(input_id_dihapus, "id potion")
                cek_valid = False
                while cek_valid == False:
                    if input_id_dihapus == "-1":
                        break
                    else:
                        if (input_id_dihapus in str(idx_i)):
                            cek_valid = True
                            validasi_input_hapus = input(
                                "Apakah anda yakin (y/n)? ")
                            if validasi_input_hapus == "y":
                                item_shop.pop(input_id_dihapus-1)
                                print("Berhasil dihapus!")
                            elif validasi_input_hapus == "n":
                                pass
                        else:
                            print(
                                "ID yang kamu masukan tidak valid! Ayo masukan id lagi!")
                            input_id_dihapus = input("Masukkan id potion: ")

            elif tipe_dilihat == "back":
                pass
            else:
                print("Input yang dimasukkan tidak valid!")

        # Jika command yang dipilih adalah keluar
        elif aksi_user == "keluar":
            time.sleep(1)
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
            time.sleep(1)
            print('Sampai jumpa lagi, Admin!\n')
            break
        else:
            print("Input yang dimasukkan salah :( Ayo input yang benar!")

        aksi_user = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
    function_values = [monster_shop, item_shop, monster, item_inventory]
    return function_values