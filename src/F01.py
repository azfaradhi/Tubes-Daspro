import F00
import colorama
colorama.init()

def valid(username: str) -> bool:
    # Spesifikasi:
    # Mengecek jika input username dari user valid
    # Digunakan pada:
        # register -> F01
        
    # parameter input:
        # username: string

    # output:
        # cek : output
    
    # Inisialisasi nilai ascii masing-masing character yang diperbolehkan
    kapital = [i for i in range(65,91)]
    kecil = [i for i in range(97,123)]
    angka = [i for i in range(48,58)]
    underscore = 95
    strip = 45

    # Membuat boolean untuk mengcek apakah input valid sesuai spesifikasi
    cek = True

    # Algoritma pengecekan
    for i in username:
        if (ord(i) not in kapital) and (ord(i) not in kecil) and (ord(i) not in angka) and (ord(i) != underscore) and (ord(i) != strip):
            cek = False
            break
    return cek

def register(user: list, monster: list, monster_inventory: list) -> list:
    # Spesifikasi:
    # Menghasilkan data pengguna baru
    # Digunakan pada:
        # main.py

    # parameter input:
        # user: array of array [id;username;password;role;oc]
        # monster: array of array [id;type;atk_power;def_power;hp]
        # monster_inventory: array of array [user_id;monster_id;level]

    # output:
        # about_user: array of string and integer [id_baru, username, password, "agent", 0]
    

    print(colorama.Fore.CYAN,"""
█▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀▀ █▀█
█▀▄ ██▄ █▄█ █ ▄█ ░█░ ██▄ █▀▄""",colorama.Style.RESET_ALL)
    print("Silahkan mengisi username baru dan password yang aman :D")
    print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")

    # Algoritma membuat akun barus dengan input username dan password
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if valid(username) == True:
            cek = False
            while cek == False:
                for i in range(len(user)):
                    # Jika username yang diinput sudah ada di database
                    if username == user[i][1]:
                        print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
                        username = input("Masukkan username: ")
                        password = input("Masukkan password: ")
                    else:
                        cek = True
            if cek:
                break
        else:
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            
    # Algoritma untuk memilih 1 monster awal
    print("Silahkan pilih salah satu monster sebagai monster awalmu.")
    for i in range(3):
        print(f"{i+1}. {monster[i][1]}")
    monster_pilihan = int(input("Masukkan pilihan Anda: "))
    indeks_pilihan_monster = [i+1 for i in range(3)]
    while True:
        # Jika id monster tidak sesuai yang diberikan
        if str(monster_pilihan) not in str(indeks_pilihan_monster):
            print("Masukkan tidak valid, ayo yang benar!")
            monster_pilihan = int(input("Monster pilihanmu: "))
        else:
            break
    
    print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[monster_pilihan-1][1]}!")

    # Membuat user_id baru untuk pengguna karena telah berhasil register
    id_baru = F00.random_number(([100000,1000000]))
    # Data yang akan dimasukkan ke dalam database user
    masuk_database_user = [str(id_baru),username,password,"agent",str(0)]
    # Data dimasukkan ke dalam database user
    user.append(masuk_database_user)
    # Data yang akan dimasukkan ke dalam database monster_inventory
    masuk_database_monster = [str(id_baru), str(monster_pilihan), str(1)]
    #Data dimasukkan ke dalam database monster_inventory
    monster_inventory.append(masuk_database_monster)
    # Data yang dapat diakses setelah memanggil fungsi register
    about_user = [id_baru, username, password, "agent", 0]
    return (about_user)