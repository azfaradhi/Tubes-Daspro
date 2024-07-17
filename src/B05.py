import time
from F12 import *
from F10 import *
from F09 import Arena
from F08 import Battle
from F07 import *
from F05 import owcaDex
from B04 import *
from F11 import *
import colorama
colorama.init()

def peta_danvile(peta:list):
    # Spesifikasi:
    # Prosedur untuk menampilkan peta dari kota danvile

    # parameter input:
    # peta: array of string

    print()
    for i in range(12):
        for j in range(12):
            if peta[i][j] == "#":
                print(" ", end=" ")
            else:
                print(peta[i][j], end=" ")
        print()

def bush(peta:list) -> list:
    # Spesifikasi:
    # Prosedur dan fungsi untuk mendeteksi keberadaan bush

    # parameter input:
    # peta: array of string

    # output:
    # bush: array of string

    bush =[]
    for i in range(12):
        for j in range(12):
            if peta[i][j] == "X" and peta[i][j] not in bush:
                for i2 in range(i-1,i+2):
                    for j2 in range(j-1,j+2):
                        bush.append([i2,j2])
    return bush


def komando(user_id: str, username:str, peta:list, monster_shop: list, item_shop: list, monster: list, monster_inventory: list, item_inventory:str, coin: int) -> list:
    # Spesifikasi:
    # Prosedur dan fungsi untuk user memilih tempat yang akan diakses

    # parameter input:
    # user_id: string, 
    # username:string, 
    # peta: arrray of str, 
    # monster_shop: array, 
    # item_shop: array, 
    # monster: array, 
    # monster_inventory: array, 
    # item_inventory:str, 
    # coin: int

    # output:
    # function_value : array  [monster_shop,item_shop,monster,monster_inventory,item_inventory,coin]

    
    time.sleep(1)
    print(colorama.Fore.YELLOW, """
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   /
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___/   //___/
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)
      """, colorama.Style.RESET_ALL)
    print("============================================== PETUNJUK ==============================================")
    print("Sebelum memulai permainan, anda harus mengetahui beberapa makna lambang di dalam peta nanti.")
    print("1. P adalah posisi anda saat ini")
    print("2. * adalah batas luar pada peta")
    print("3. X, L, S, J, A, dan E secara berturut-turut adalah adalah bush, laboratory, shop, jackpot, arena, dan exit")
    print("Berikut beberapa ketentuan berjalan di dalam Kota Danvile")
    print("1. Anda tidak dapat berjalan menabrak batas luar peta dan obstacle yang ada di dalam Peta.")
    print("2. Untuk mengakses tempat-tempat yang disediakan, anda harus berada di sekitar lokasi tersebut, lalu mengetikkan nama dari lokasi yang ingin anda kunjungi.")
    print("Sebagai contoh, jika anda ingin masuk ke dalam ARENA, maka anda cukup menuliskan 'arena' pada command")
    print("3. Setiap anda mendekati bush, anda dapat memasuki battle.")
    print("4. Untuk berjalan ke (kiri,atas,bawah,kanan), anda cukup menuliskan (a,w,s,d) pada command.")
    print("5. Untuk melihat inventory yang anda miliki, anda dapat menuliskan 'inventory' pada command.")
    print("6. Untuk melihat semua monster, anda dapat menuliskan 'owcadex' pada command.")
    print("======================================================================================================")
    time.sleep(2)
    obstacle = ["*","S","A","L","X","J"]
    battle_bush = bush(peta)
    while True:
        peta_danvile(peta)
        for i in range(12):
            for j in range(12):
                if peta[i][j] == "P":
                    idx_baris = i
                    idx_kolom = j
        print(f"P saat ini berada di posisi ({idx_baris-1},{idx_kolom-1})")
        command = input("Masukkan command: ").lower()
        if command == "a":
            if peta[idx_baris][idx_kolom-1] in obstacle:
                print("\nAgent Purry tidak bisa pindah karena terdapat Obstacle!")
            else:
                peta[idx_baris][idx_kolom],peta[idx_baris][idx_kolom-1] = "#","P"
                idx_kolom -= 1
                print("\nAgent akan pindah ke kiri!")
        elif command == "d":
            if peta[idx_baris][idx_kolom+1] in obstacle:
                print("\nAgent tidak bisa pindah karena terdapat Obstacle!")
            else:
                peta[idx_baris][idx_kolom],peta[idx_baris][idx_kolom+1] = "#","P"
                idx_kolom += 1
                print("\nAgent akan pindah ke kanan!")
        elif command == "w":  
            if peta[idx_baris-1][idx_kolom] in obstacle:
                print("\nAgent tidak bisa pindah karena terdapat Obstacle!")
            else:
                peta[idx_baris][idx_kolom],peta[idx_baris-1][idx_kolom] = "#","P"
                idx_baris -= 1
                print("\nAgent akan pindah ke atas!")
        elif command == "s":
            if peta[idx_baris+1][idx_kolom] in obstacle:
                print("\nAgent tidak bisa pindah karena terdapat Obstacle!")
            else:
                peta[idx_baris][idx_kolom],peta[idx_baris+1][idx_kolom] = "#","P"
                idx_baris += 1
                print("\nAgent akan pindah ke bawah!")
        elif command == "shop":
            if (idx_baris in range(1,4)) and (idx_kolom in range(5,8)):
                print("\nLoading...")
                time.sleep(1)
                function_value = Shop(user_id,monster_shop,item_shop,monster,monster_inventory,item_inventory,coin)
                monster_shop = function_value[0]
                item_shop = function_value[1]
                monster = function_value[2]
                monster_inventory = function_value[3]
                item_inventory = function_value[4]
                coin = function_value[5]
                time.sleep(2)
                print("\nLoading...")
                time.sleep(2)
            else:
                print("\nAgent tidak berada di area Shop!")
        elif command == "battle":
            if [idx_baris,idx_kolom] in battle_bush:
                userMonsters = UserMonsters(user_id,monster,monster_inventory)
                userPotions = UserPotions(user_id,item_inventory)
                print("\nLoading...")
                time.sleep(1)
                (userPotions, bonus) = Battle(monster, userMonsters, userPotions, username)
                coin += bonus
                item_inventory = ItemInventory(user_id,item_inventory,userPotions)
                time.sleep(2)
                print("\nLoading...")
                time.sleep(2)
            else:
                print("\nAgent tidak berada di area Battle!")
        elif command == "laboratory":
            if (idx_baris in range(7,10)) and (idx_kolom in range(1,3)):
                print("\nLoading...")
                time.sleep(1)
                function_value = laboratory(user_id,coin,monster,monster_inventory)
                coin = function_value[0]
                monster_inventory = function_value[1]
                time.sleep(2)
                print("\nLoading...")
                time.sleep(2)
            else:
                print("\nAgent tidak berada di area Laboratory!")
        elif command == "jackpot":
            if (idx_baris in range(9,12)) and (idx_kolom in range(4,7)):
                print("\nLoading...")
                time.sleep(1)
                function_value = jackpot(user_id,monster_inventory,coin)
                monster_inventory = function_value[0]
                coin = function_value[1]
                time.sleep(2)
                print("\nLoading...")
                time.sleep(2)
            else:
                print("\nAgent tidak berada di area JACKPOT!")
        elif command == "arena":
            if (idx_baris in range(7,10)) and (idx_kolom in range(8,11)):
                userMonsters = UserMonsters(user_id, monster, monster_inventory)
                userPotions = UserPotions(user_id, item_inventory)
                print("\nLoading...")
                time.sleep(1)
                (userPotions, bonus) = Arena(userMonsters, userPotions, username, monster)
                coin += bonus
                item_inventory = ItemInventory(user_id, item_inventory, userPotions)
                time.sleep(2)
                print("\nLoading...")
                time.sleep(2)
            else:
                print("\nAgent tidak berada di area Arena!")
        elif command == "inventory":
            userMonsters = UserMonsters(user_id, monster, monster_inventory)
            userPotions = UserPotions(user_id, item_inventory)
            TampilInventoryUser(userMonsters, userPotions, user_id, username, coin)
            time.sleep(2)
            print("\nLoading...")
            time.sleep(2)
        elif command == "owcadex":
            owcaDex(monster)
            time.sleep(2)
            print("\nLoading...")
            time.sleep(2)
        elif command == "exit":
            if (idx_baris in range(1,4)) and (idx_kolom in range(9,12)):
                validasi_keluar = input("Apakah benar anda akan keluar? (y/n): ")
                if validasi_keluar == "y":
                    break
            else:
                print("\nAgent tidak berada di area Exit!")
        else:
            print("Command yang kamu masukkan tidak valid!")
        time.sleep(1)
    function_value = monster_shop,item_shop,monster,monster_inventory,item_inventory,coin
    return function_value