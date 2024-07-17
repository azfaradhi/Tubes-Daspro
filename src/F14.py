import os
import argparse
import time

def load(nama_folder):
    # dictionary
    user = []
    monster = []
    monster_shop = []
    monster_inventory = []
    item_shop = []
    item_inventory = []
    peta = []
    # mengecek folder ada atau tidak
    if os.path.exists(nama_folder):
        time.sleep(0.5)
        print("Loading...")
        time.sleep(1)
        for file in os.listdir(nama_folder):
            nama_file = f"{nama_folder}/{file}"
            if nama_file == f"{nama_folder}/user.csv":
                user = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/monster.csv":
                monster = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/monster_shop.csv":
                monster_shop = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/monster_inventory.csv":
                monster_inventory = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/item_shop.csv":
                item_shop = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/item_inventory.csv":
                item_inventory = parse_csv(nama_file)
            elif nama_file == f"{nama_folder}/peta.csv":
                peta = parse_csv(nama_file)
        
        return True,user,monster,monster_shop,monster_inventory,item_shop,item_inventory,peta
    else:
        print(f"Yah, folder \"{nama_folder}\" tidak dapat ditemukan.")
        return [False]

def parse_csv(file_path):
    data = []
    count_line = 1
    with open(file_path, 'r') as file:
        for line in file:
            baris = []
            temp_add = ''
            for char in range(len(line)):
                if line[char] == ";" or line[char] == '\n':
                    baris.append(temp_add)
                    temp_add = ''
                else:
                    temp_add += line[char]
            if temp_add:
                baris.append(temp_add)
            data.append(baris)
    data.pop(0)
    return data

sudah_bisa_login = False
while True:
    parser = argparse.ArgumentParser(description = "OWCA Program - Load")
    parser.add_argument("nama_folder", nargs = "?", help = "Nama folder untuk memuat data")
    args = parser.parse_args()
    # mengecek nama folder
    if not args.nama_folder:
        print("Tidak ada nama folder yang diberikan! Harap masukkan nama folder!")
        break
    else:
        nilai_fungsi = load(args.nama_folder)
        if nilai_fungsi[0] == True:
            user = nilai_fungsi[1]
            monster = nilai_fungsi[2]
            monster_shop = nilai_fungsi[3]
            monster_inventory = nilai_fungsi[4]
            item_shop = nilai_fungsi[5]
            item_inventory = nilai_fungsi[6]
            peta = nilai_fungsi[7]
            sudah_bisa_login = True
            break
        else:
            break