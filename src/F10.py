import time
from Operations import inputValid

def Shop(user_id,monster_shop:list, item_shop:list, monster:list, monster_inventory:list, item_inventory: list, coin:int):
    # Spesifikasi:
    # Menambahkan inventory agent dengan membeli monster atau potion (item)
    # Digunakan pada:
        # B05.py

    # parameter input:
        # user_id: int
        # monster_shop: array of array [monster_id;stock;price]
        # item_shop: array of array [type;stock;price]
        # monster: array of array [id;type;atk_power;def_power;hp]
        # monster_inventory: array of array [user_id;monster_id;level]
        # item_inventory: array of array [user_id;type;quantity]
        # coin: int

    # output:
        # function_value: array of array
    
    # Animasi awal
    time.sleep(1)
    print("==========================================")
    time.sleep(1)
    print("""
            █▀ █░█ █▀█ █▀█
            ▄█ █▀█ █▄█ █▀▀""")
    print()
    time.sleep(1)
    print("==========================================")

    time.sleep(1)
    print("Selamat datang di Shop!")
    time.sleep(1)

    switch = 0
    # Algoritma conditional dari amsukkan agent
    while switch == 0:
        linePilih = "Pilih aksi (lihat/beli/keluar)"
        pilihValid = ["lihat","beli","keluar"]
        pilih = inputValid("",linePilih,pilihValid,"str") # Memilih Aksi

        # Jika agent memilih untuk keluar
        if pilih == "keluar": 
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
            print('\nSampai jumpa lagi di Shop!\n')
            switch = 1

        # Jika agent ingin melihat monster atau potion
        elif pilih == "lihat":
            lineLihat = "Mau lihat apa? (monster/potion)"
            lihatValid = ["monster","potion"]
            lihat_apa = inputValid("",lineLihat,lihatValid,"str")
            if lihat_apa == "monster":
                print("\nID        |Type      |ATK Power |DEF Power |HP        |Stok      |Harga     |")
                print("----------|----------|----------|----------|----------|----------|----------|")
                for row in monster:
                        if str(row[0]) in str(monster_shop):
                            for char in row:
                                length_char = len(char)
                                print(str(char) + " "*(10-length_char), end="|")
                            for row2 in monster_shop:
                                if row2[0] == row[0]:
                                    length_row2 = len(str(row2[1]))
                                    length_row3 = len(str(row2[2]))
                                    print(str(row2[1]) + " "*(10-length_row2) + "|" + str(row2[2]) + " "*(10-length_row3) + "|", end="")     
                            print()
            elif lihat_apa == "potion":
                print("\nID |Type           |Stock          |Harga          |")
                print("---|---------------|---------------|---------------|")
                i = 1
                for row in item_shop:
                    print(i, end="  |")
                    i += 1
                    for char in row:
                        length_char = len(char)
                        print(str(char) + " "*(15-length_char), end="|")
                    print()

        # Jika agent ingin membeli monster/potion          
        elif pilih == "beli":
            lineInput = "Mau beli apa? (monster/potion)"
            itemValid = ["monster","potion"]
            item = inputValid("",lineInput,itemValid,"str")

            if item == "monster":
                # Memastikan input sesuai dengan yang tersedia di shop
                idValid = ['0']
                for i in range(len(monster_shop)):
                    idValid.append(str(monster_shop[i][0]))

                textInput = f"""
Koin Anda saat ini: {coin} OC

Ketik id monster untuk membeli
Ketik 0 untuk kembali"""
                id_monster_input = inputValid(textInput,"",idValid,"int")

                # Mengecek Apakah Terdapat id yang sama dalam inventory
                cek_inventory = True
                while cek_inventory:
                    found = False
                    for row in monster_inventory:
                        if (row[0] == user_id):
                            if str(id_monster_input) == str(row[1]):
                                found = True
                                break
                    if found:
                        print(f"\nAnda telah memiliki {monster[id_monster_input-1][1]}")
                        id_monster_input = inputValid(textInput,"",idValid,"int")
                    else:
                        break

                if id_monster_input != 0:
                    # Cek apakah Jumlah item sesuai stock atau tidak
                    for i, row in enumerate(monster_shop):
                        if str(row[0]) == str(id_monster_input):
                            baris = i
                            break
                    if 0 >= int(monster_shop[baris][1]):
                        print("\nPembelian Gagal :( , Stock tidak mencukupi")
                    else:
                        harga_item = int(monster_shop[baris][2])
                        if harga_item > coin:
                            print("\nPembelian Gagal :( , Koin tidak mencukupi")
                        else:
                            # Memasukkan item ke inventory
                            monster_tambah = [str(user_id),str(id_monster_input),str(1)] 
                            monster_inventory.append(monster_tambah)
    
                            # Mengurangi Item pada Shop
                            monster_shop[i][1] = int(monster_shop[i][1]) - 1
    
                            # Mengurangi coin
                            coin -= harga_item

                            for row in monster:
                                if str(row[0]) == str(id_monster_input):
                                    nama_monster = row[1]
                                    break
                            # output
                            print(f"\nSelamat, monster {nama_monster} telah berhasil dibeli!")
                            print(f"\nKoin tersisa: {coin} OC")

            elif item == "potion":
                # Memastikan input sesuai dengan yang tersedia di shop
                idValid = [str(i) for i in range(len(item_shop)+1)]
                textInput = f"""
Koin Anda saat ini: {coin} OC

Ketik id potion untuk membeli
Ketik 0 untuk kembali"""
                id_item_input = inputValid(textInput,"",idValid,"int")

                if id_item_input != 0:
                    # Cek apakah Jumlah item sesuai stock atau tidak
                    for i, row in enumerate(monster_shop):
                        if str(row[0]) == str(id_item_input):
                            baris = i
                            break
                    jumlah_item = int(input("\nMasukkan Jumlah Item yang ingin dibeli : "))
                    if 0 >= int(item_shop[int(id_item_input)-1][1]) or int(jumlah_item) > int(item_shop[int(id_item_input)-1][1]):
                        print("\nPembelian Gagal :( , Stock tidak mencukupi")
                    else:
                        harga_item = int(item_shop[int(id_item_input)-1][2])
                        harga_total = harga_item * jumlah_item
                        item_type = item_shop[int(id_item_input)-1][0]
                        if harga_total>coin:
                            print("\nPembelian Gagal :( , Koin tidak mencukupi")
                        else:
                            # Memasukkan item ke inventory
                            found = False
                            i = 0
                            while (i < len(item_inventory)) and not(found):
                                if (str(item_inventory[i][0]) == str(user_id)): 
                                    if (str(item_inventory[i][0]) == str(item_type)):
                                        item_inventory[i][3] = str(int(item_inventory[i][3]) + jumlah_item)
                                        found = True
                                i += 1
    
                            if not(found):
                                item_tambah = [str(user_id),str(item_type),str(jumlah_item)] 
                                item_inventory.append(item_tambah)
    
                            # Mengurangi Item pada Shop
                            item_shop_integer = int(item_shop[int(id_item_input)-1][1]) - jumlah_item
                            item_shop[int(id_item_input)-1][1] = str(item_shop_integer)
                            print(f"\nSelamat!!! Anda Telah membeli potion {item_type} sebanyak {jumlah_item}")
    
                            # Mengurangi koin
                            coin -= harga_total
                            print(f"\nKoin tersisa: {coin} OC")
    function_value = [monster_shop,item_shop,monster,monster_inventory,item_inventory,coin]
    return function_value
