import sys
sys.path.append('src')

import colorama
colorama.init()
from do_csv import *
import F01
import F02
import F04
from F14 import *


if sudah_bisa_login == True:
    status_save = False
    temp_user = user[:]
    temp_monster = monster[:]
    temp_monster_shop = monster_shop[:]
    temp_monster_inventory = monster_inventory[:]
    temp_item_shop = item_shop[:]
    temp_item_inventory = item_inventory[:]
    temp_peta = peta[:]
    status_exit = False

    while status_exit == False:
        if status_save == False:
            user = temp_user[:]
            monster = temp_monster[:]
            monster_shop = temp_monster_shop[:]
            monster_inventory = temp_monster_inventory[:]
            item_shop = temp_item_shop[:]
            item_inventory = temp_item_inventory[:]
            peta = temp_peta[:]

        print(colorama.Fore.BLUE, """
        ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
        ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
        ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
        ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
        ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
        ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝""", colorama.Style.RESET_ALL)

        print("SELAMAT DATANG DI KOTA DANVILE")
        print("Masukkan command 'help' untuk melihat list command")

        input_user = input(">>> ")

        while True:
            if input_user == "help":
                F04.help_belum_login()
                input_user = input(">>> ")
            if input_user == str(1):
                about_user = F01.register(user,monster,monster_inventory)
                status_login = True
                user_id = about_user[0]
                user_username = about_user[1]
                user_role = about_user[3]
                user_coin = int(about_user[4])
                break
            elif input_user == str(2):
                about_user = F02.login(user)
                if about_user[0] == True:
                    status_login = True
                    user_id = about_user[1][0]
                    user_username = about_user[1][1]
                    user_role = about_user[1][3]
                    user_coin = int(about_user[1][4])
                    break
                else:
                    print("Silahkan masukkan command kembali")
                    input_user = input(">>> ")
            else:
                print("Input yang dimasukkan salah!")
                input_user = input(">>> ")

        while status_login == True:
            if user_role == "admin":
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                function_value = F04.help_sudah_login_admin(user,monster,monster_shop,monster_inventory,item_shop,item_inventory)
                if function_value[0] == True:
                    status_exit = True
                status_save = function_value[1]
                user = function_value[2]
                monster = function_value[3]
                monster_shop = function_value[4]
                monster_inventory = function_value[5]
                item_shop = function_value[6]
                item_inventory = function_value[7]
                status_login = False

            elif user_role == "agent":
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                function_value = F04.help_sudah_login_agent(user,user_id,user_username,peta,monster_shop,item_shop, monster, monster_inventory, item_inventory,user_coin)
                if function_value[0] == True:
                    status_exit = True
                status_save = function_value[1]
                user = function_value[2]
                monster_shop = function_value[3]
                item_shop = function_value[4]
                monster = function_value[5]
                monster_inventory = function_value[6]
                item_inventory = function_value[7]
                status_login = False
        print("SAMPAI JUMPA KING!")
else:
    pass