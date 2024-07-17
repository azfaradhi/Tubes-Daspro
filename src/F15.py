import os
import time

def save_data(nama_folder, user, monster, monster_shop, monster_inventory, item_shop, item_inventory):
    parent_save = "savedata"
    folder = os.path.join(parent_save, nama_folder)
    # mengecek folder
    if not os.path.exists(folder):
        print("")
        time.sleep(1)
        print(f"Membuat folder {folder}...")
        os.makedirs(folder)
    else:
        print("")
        time.sleep(1)
        print(f"Folder {folder} sudah ada.")
    files_di_folder = os.listdir(folder)
    if files_di_folder:
        print("")
        time.sleep(1)
        print("Saving....")
        time.sleep(1)
        print("Berhasil menyimpan data di folder", folder)
    else:
        print("")
        time.sleep(1)
        print("Saving....")
        time.sleep(1)
        print("Berhasil menyimpan data di folder", folder)

    # Simpan data ke dalam file CSV
    with open(os.path.join(folder, "user.csv"), 'w') as file:
        data_default = "id;username;password;role;oc"
        file.write(data_default)
        for data in user:
            file.write("\n")
            file.write(";".join(map(str, data)))

    with open(os.path.join(folder, "monster.csv"), 'w') as file:
        data_default = "id;type;atk_power;def_power;hp"
        file.write(data_default)

        for data in monster:
            file.write("\n")
            file.write(";".join(map(str, data)))

    with open(os.path.join(folder, "monster_shop.csv"), 'w') as file:
        data_default = "monster_id;stock;price"
        file.write(data_default)
        for data in monster_shop:
            file.write("\n")
            file.write(";".join(map(str, data)))

    with open(os.path.join(folder, "monster_inventory.csv"), 'w') as file:
        data_default = "user_id;monster_id;level"
        file.write(data_default)
        for data in monster_inventory:
            file.write("\n")
            file.write(";".join(map(str, data)))

    with open(os.path.join(folder, "item_shop.csv"), 'w') as file:
        data_default = "type;stock;price"
        file.write(data_default)
        for data in item_shop:
            file.write("\n")
            file.write(";".join(map(str, data)))

    with open(os.path.join(folder, "item_inventory.csv"), 'w') as file:
        data_default = "user_id;type;quantity"
        file.write(data_default)
        for data in item_inventory:
            file.write("\n")
            file.write(";".join(map(str, data)))

def save(user,monster,monster_shop,monster_inventory,item_shop,item_inventory):
    print(">>> Save")
    nama_folder = input("Masukkan nama folder untuk penyimpanan: ")
    save_data(nama_folder, user, monster, monster_shop, monster_inventory, item_shop, item_inventory)
