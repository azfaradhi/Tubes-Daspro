import time
import F00


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


def monster_management(monster: list) -> list:
    # Spesifikasi:
    # Prosedur dan fungsi untuk merubah monster dan potion yang ada di database monste
    # Digunakan pada:
       # F04.py

    # parameter input:
       # monster: list

    # output:
       # monster: list

    # Animasi awal
    time.sleep(1)
    print("""

█▀▄▀█ █▀█ █▄░█ █▀ ▀█▀ █▀▀ █▀█   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀
█░▀░█ █▄█ █░▀█ ▄█ ░█░ ██▄ █▀▄   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █░▀░█ ██▄ █░▀█ ░█░""")
    print()

    time.sleep(1)
    print()
    print("========== SELAMAT DATANG DI MENU DATA MONSTER MANAGEMENT ==========")

    # Variable pengganti fungsi break
    switch = 1
    while switch == 1:
        print()
        print("====== SILAHKAN PILIH FITUR ======")
        print("1. Tampilkan Monster yang anda miliki")
        print("2. Tambahkan Monster Baru")
        print("3. Keluar")
        print()
        input_fitur = input("Pilih fitur diatas (1/2/3) :")
        print()

        # Jika user ingin melihat monster yang dimiliki
        if input_fitur == "1":
            print("="*26 + str(" Menampilkan semua monster! ") + "="*26)
            for row in monster:
                for char in row:
                    length_char = len(char)
                    print(str(char) + " "*(15-length_char), end="|")
                print()

        # Jika user ingin menambahkan monster baru
        elif input_fitur == "2":
            input_nama_monster = input("\nMasukkan Nama Monster barumu : ")
            cek_file = True
            while cek_file:
                found = False
                for row in monster:
                    if str(input_nama_monster) == str(row[1]):
                        found = True
                        cek_file = False
                        break
                if found:
                    print("Nama Sudah Terdaftar, Silahkan Coba Lagi!!")
                    input_nama_monster = input(
                        "Masukkan Nama Monster lainnya : ")
                else :
                    break
                
            input_atk_power = input("Masukkan ATK Power : ")
            input_atk_power = validasi_int(input_atk_power, "ATK Power")

            input_def_power = input("Masukkan DEF Power (0-50) : ")
            input_def_power = validasi_int(input_def_power, "DEF Power")

            Cek_Rentang = True
            while Cek_Rentang == True:
                if not(0 <= int(input_def_power) <= 50):
                    print("INPUT SALAH!! DEF Power harus bernilai 0-50, coba lagi!")
                    input_def_power = input("Masukkan DEF Power Baru (0-50): ")
                else :
                    Cek_Rentang = False

            input_HP = input("Masukkan HP Monster : ")
            input_HP = validasi_int(input_HP, "HP Monster")

            print("BERHASIL, Monster Baru Telah Dibuat!!")
            print(f"Type      : {input_nama_monster}")
            print(f"ATK Power : {input_atk_power}")
            print(f"DEF Power : {input_def_power}")
            print(f"HP        : {input_HP}")
            id_monster = F00.random_number([100000, 1000000])
            print("Apakah Monster baru akan dimasukkan ke database? (Y/N)")
            validasi_database = input(">>> ").lower()
            if validasi_database == "y":
                monster_baru = [str(id_monster), str(input_nama_monster),str(input_atk_power),str(input_def_power),str(input_HP)]
                monster.append(monster_baru)
                print("Monster berhasil dimasukkan ke database!\n")
            elif validasi_database == "n":
                print("Penambahan Monster Dibatalkan!!\n")
            else :
                print("Input tidak valid , Penambahan dibatalkan\n")

        # Jika user ingin keluar dari program
        elif input_fitur == "3":
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
            switch = 0
    return monster