import colorama
colorama.init()
def login(user: list) -> list:
    # Spesifikasi:
    # Mengakses data pengguna yang akan digunakan untuk bermain
    # Digunakan pada:
        # main.py

    # parameter input:
        # user: array of array [id;username;password;role;oc]

    # output:
        # about_user: array of bool,string,int of arr [bool,user[idx_row]]

    print(colorama.Fore.CYAN,"""
█░░ █▀█ █▀▀ █ █▄░█
█▄▄ █▄█ █▄█ █ █░▀█""", colorama.Style.RESET_ALL)
    
    # Memberi arahan kepada pengguna untuk login
    print("Halo! Silahkan login dengan username dan password anda! (ketik 'cancel' pada username untuk kembali ke menu awal)")
    username = input("Username: ")
    password = input("Password: ")

    while True:
        # Jika pengguna tidak jadi login
        if username == "cancel":
            berhasil_login = False
            break
        else:
            i = 0
            cek = False
            for i in range(len(user)):
                if user[i][1] == username:
                    cek = True
                    idx_row = i
                    continue
            # Jika username tidak terdaftar dalam database
            if not cek:
                print("Username tidak terdaftar!")
                username = input("Username: ")
                password = input("Password: ")        
            else:
                if password != user[idx_row][2]:
                    print("Password salah!")
                    username = input("Username: ")
                    password = input("Password: ")
                else:
                    # Login berhasil
                    print(f"Selamat datang, {user[idx_row][3]} {username}!")
                    berhasil_login = True
                    break
    
    # Conditional data yang dapat diakses setelah memanggil fungsi login
    if berhasil_login == True:
        return True,user[idx_row]
    else:
        return False,user