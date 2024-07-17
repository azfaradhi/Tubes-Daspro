import colorama
import time
import F03
import F12
import F13
import F15
import F16
import B05
colorama.init()

def help_belum_login():

    # Spesifikasi:
    # Menghasilkan deretan command yang dapat diakses ketika pengguna belum login
    # Digunakan pada:
        # F04

    print("============================= HELP =============================")
    print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
    print("1. Register: Membuat akun baru" )
    print("2. Login: Masuk ke dalam akun yang sudah terdaftar")
    print("Footnote: ")
    print("1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("2. Jangan lupa untuk memasukkan input yang valid")
    print("================================================================")

def list_help_admin():

    # Spesifikasi:
    # Menghasilkan deretan command yang dapat diakses ketika pengguna sudah login, dan role nya adalah admin
    # Digunakan pada:
        # F04

    print("============================= HELP =============================")
    print(f"Halo Admin! Berikut adalah hal-hal yang dapat kamu lakukan: ")
    print("1. Logout: Keluar dari akun yang sedang digunakan")
    print("2. Shop Management: Mengatur ketersediaan monster dan potion pada shop")
    print("3. Monster Management: Mengatur monster dalam database")
    print("4. Save data")
    print("5. Selesai")
    print("Footnote: ")
    print("1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("2. Jangan lupa untuk memasukkan input yang valid")
    print("================================================================")

def list_help_agent():

    # Spesifikasi:
    # Menghasilkan deretan command yang dapat diakses ketika pengguna sudah login, dan role nya adalah agent
    # Digunakan pada:
        # F04.py
        
    print("============================= HELP =============================")
    print(f"Halo Agent!. Kamu memanggil command Help. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
    print("1. Logout: Keluar dari akun yang sedang digunakan")
    print("2. Monster: Melihat monster yang dimiliki oleh Agent")
    print("3. Potion: Melihat potion yang dimiliki oleh Agent")
    print("4. Mulai bermain!")
    print("5. Save data")
    print("6. Selesai bermain")
    print("Footnote: ")
    print("1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("2. Jangan lupa untuk memasukkan input yang valid")
    print("================================================================")

def help_sudah_login_admin(user:list,monster:list,monster_shop:list,monster_inventory:list,item_shop:list,item_inventory:list) -> bool:
    # Spesifikasi:
    # Mengakses fungsi yang akan digunakan admin
    # Digunakan pada:
        # main.py

    # parameter input:
        # user: array of array [id;username;password;role;oc]
        # monster: array of array [id;type;atk_power;def_power;hp]
        # monster_shop: array of array [monster_id;stock;price]
        # monster_inventory: array of array [user_id;monster_id;level]
        # item_shop: array of array [type;stock;price]
        # item_inventory: array of array [user_id;type;quantity]

    # output:
        # exit: bool 

    # Memasukkan command yang akan dipilih admin
    print("Command: ")
    input_user = input(">>> ")

    # Algoritma conditional input_user
    while True:
        status_save = False
        # Jika user memilih logout
        if input_user == str(1):
            validasi_logout = F03.logout()
            if validasi_logout == True:
                exit = False
                break
            else:
                pass
        # Jika user memilih shop_management
        elif input_user == str(2):
            hasil_fungsi = F12.shop_management(monster_shop, item_shop, monster, item_inventory)
            # Mengupdate variable dengan hasil dari fungsi yang telah didapat
            monster_shop = hasil_fungsi[0]
            item_shop = hasil_fungsi[1]
            monster = hasil_fungsi[2]
            item_inventory = hasil_fungsi[3]
        
        # Jika user memilih monster_management
        elif input_user == str(3):
            monster = F13.monster_management(monster)

        # Jika user akan meng-save data
        elif input_user == str(4):
            F15.save(user,monster,monster_shop,monster_inventory,item_shop,item_inventory)
            status_save = True
        
        # Jika user akan keluar dari program
        elif input_user == str(5):
            validasi_exit = F16.exit()
            if validasi_exit == True:
                exit = True
                break
            else:
                pass

        # Jika user membutuhkan bantuan dalam memilih command
        elif input_user == "help":
            list_help_admin()

        else:
            pass

        print("Command: ")
        input_user = input(">>> ")
    return exit,status_save,user,monster,monster_shop,monster_inventory,item_shop,item_inventory

def help_sudah_login_agent(user:list,user_id,username:str,peta:list,monster_shop:list,item_shop:list, monster:list, monster_inventory:list, item_inventory:list,coin:int) -> bool:
    # Spesifikasi:
    # Mengakses fungsi yang akan digunakan agent
    # Digunakan pada:
        # main.py

    # parameter input:
        # user: array of array [id;username;password;role;oc]
        # user_id: int
        # username: string
        # peta: array of string of array
        # monster_shop: array of array [monster_id;stock;price]
        # item_shop: array of array [type;stock;price]
        # monster: array of array [id;type;atk_power;def_power;hp]
        # monster_inventory: array of array [user_id;monster_id;level]
        # item_inventory: array of array [user_id;type;quantity]
        # coin: int

    # output:
        # exit: bool 
    
    # Masukkan command yang akan dipilih agent
    print("Command: ")
    input_user = input(">>> ")

    # Algoritma conditional input_user
    status_save = False
    while True:

        # Jika user memilih logout
        if input_user == str(1):
            validasi_logout = F03.logout()
            if validasi_logout == True:
                exit = False
                break
            else:
                pass

        # Jika user memilih Monster
        elif input_user == str(2):
            print("Berikut adalah monster yang anda miliki")
            print("ID        |Type      |ATK Power |DEF Power |HP        |")
            print("----------|----------|----------|----------|----------|")
            for row in range(len(monster_inventory)):
                if str(monster_inventory[row][0]) == str(user_id):
                    for type in range(len(monster)):
                        if str(monster[type][0]) == str(monster_inventory[row][1]):
                            for char in monster[type]:
                                lenchar = len(char)
                                print(str(char) + " "*(10-lenchar), end="|")
                    print()
            
        # Jika user memilih Potion
        elif input_user == str(3):
            print("No |Type           |Kuantitas      |")
            print("---|---------------|---------------|")
            i = 1
            for row in range(len(item_inventory)):
                if str(item_inventory[row][0]) == str(user_id):
                    print(i, end="  |")
                    lenchar1 = len(item_inventory[row][1])
                    lenchar2 = len(item_inventory[row][2])
                    print(str(item_inventory[row][1]) + " "*(15-lenchar1) + "|" + item_inventory[row][2] + " "*(15-lenchar2) + "|")
                    i += 1
        
        # Jika user memilih untuk bermain
        elif input_user == str(4):

            # Menampilkan animasi
            print("Loading...")
            time.sleep(1)
            print("""

▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀ 　 ▒█▀▀▄ ▀█▀ ▒█▀▄▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▀█▀ 
▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀ 　 ▒█░▒█ ▒█░ ▒█▒█▒█ ▒█░▒█ ▒█░░░ ▒█▄▄█ ▒█░ 
▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄ 　 ▒█▄▄▀ ▄█▄ ▒█░░▒█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ▄█▄""")
            print()

            # Mengakses fungsi komando yang diakses adri B05.py
            function_value = B05.komando(user_id,username,peta,monster_shop,item_shop, monster, monster_inventory, item_inventory,coin)
            monster_shop = function_value[0]
            item_shop = function_value[1]
            monster = function_value[2]
            monster_inventory = function_value[3]
            item_inventory= function_value[4]
            coin = function_value[5]

        
        # Jika user memilih untuk meng-save data
        elif input_user == str(5):
            for row in range(len(user)):
                if str(user[row][0]) == str(user_id):
                    idx = row
            user[idx][4] = coin
            F15.save(user,monster,monster_shop,monster_inventory,item_shop,item_inventory)
            status_save = True
        
        # Jika user membutuhkan bantuan dalam memilih command
        elif input_user == "help":
            list_help_agent()

        # Jika user memilih untuk keluar dari permainan
        elif input_user == str(6):
            validasi_exit = F16.exit()
            if validasi_exit == True:
                exit = True
                break
            else:
                pass
        else:
            pass

        print("Command: ")
        input_user = input(">>> ")

    return exit,status_save,user,monster_shop,item_shop, monster, monster_inventory, item_inventory