from F05 import lvlStat, TampilMonsterDetail
from Operations import inputValid

def ItemInventory(user_id: str,items_inv: list, userPotions: list) -> list:
    n = len(userPotions)
    m = len(items_inv)
    j = 0
    for i in range(m):
        if (items_inv[i][0] == user_id):
            type = userPotions[j][0]
            if (type == "ATK"):
                type = "strength"
            elif (type == "DEF"):
                type = "resilience"
            else:
                type = "healing"
            qty = str(userPotions[j][1])
            items_inv[i][1] = type
            items_inv[i][2] = qty
            j += 1

    for i in range(j,n):
        type = userPotions[j][0]
        if (type == "ATK"):
            type = "strength"
        elif (type == "DEF"):
            type = "resilience"
        else:
            type = "healing"
        qty = str(userPotions[j][1])
        items_inv.append([user_id,type,qty])
    return(items_inv)

def UserMonsters(user_id: str,monsters: list,monsters_inv: list) -> list:
    # Spesifikasi:
        # mengumpulkan data monster yang dimiliki user dan disimpan di userMonsters
        # Digunakan pada:
            # main
    
    # parameter input: 
        # user_id = int -> id user
        # monsters = list -> read_csv("monster.csv")
        # monsters_inv = list -> read_csv("monster_inventory.csv")
    # output:
        # userMonsters: array of list[id,name,lvl,baseStat] -> data tiap monster yang dimiliki user

    userMonsters = []
    for i in range(len(monsters_inv)):
        if (int(monsters_inv[i][0]) == int(user_id)):
            # data dari monster_inventory.csv
            id = int(monsters_inv[i][1])
            lvl = int(monsters_inv[i][2])
            # data dari monster.csv
            name = str(monsters[id-1][1])
            baseStat = [float(monsters[id-1][j+2]) for j in range(3)]
            userMonsters.append([id,name,lvl,baseStat])
    return(userMonsters)
    
def UserPotions(user_id: str,items_inv: list) -> list:
    # Spesifikasi:
        # mengumpulkan data potion yang dimiliki user dan disimpan pada userPotions
        # Digunakan pada:
            # main

    # parameter input:
        # user_id = int -> id user
        # items_inv = list -> read_csv("item_inventory.csv")
    # output:
        # userPotions = array of list[type,qty]
            # type = str (ATK/DEF/Heal)

    userPotions = []
    for i in range(len(items_inv)):
        if (int(items_inv[i][0]) == int(user_id)):
            type = items_inv[i][1]
            if (type == "strength"):
                type = "ATK"
            elif (type == "resilience"):
                type = "DEF"
            else:
                type = "Heal"
            qty = int(items_inv[i][2])
            userPotions.append([type,qty])
    return(userPotions)

def KembaliKeInventory() -> bool:
    # Spesifikasi:
        # menghasilkan statement apakah user ingin kembali ke inventory atau keluar
        # Digunakan pada:
            # TampilInventoryUser -> F07

    pilihanValid = ["0","1"]
    textInput = """
Ketik 1 untuk kembali ke inventory
Ketik 0 untuk keluar"""
    pilih = inputValid(textInput,"",pilihanValid,"int")

    if (pilih == 0):
        return(False)
    else:
        return(True)

def TampilPotionDetail(userPotions: list, pilih: int) -> str:
    # Spesifikasi:
        # men-generate tampilan detail mengenai potion
        # Digunakan pada:
            # TampilInventoryUser -> F07

    # parameter input:
        # potion = list[type,qty]
            # type = str (ATK/DEF/Heal)
            # qty = int
    # output:
        # tampilan = str
    
    i = 0
    while (i < len(userPotions)) and (pilih >= 1):
        if (userPotions[i][1] != 0):
            pilih -= 1
        i += 1
        
    potion = userPotions[i-1]

    type = potion[0]
    qty = potion[1]
    if (type == "ATK"):
        nama = "strength"
    elif (type == "DEF"):
        nama = "resilience"
    else:
        nama = "healing"
    tampilan = f"""
========================= {nama.upper()} POTION =========================
(Dimiliki: {qty})
                """

    if (type == "HP"):
        tampilan += f"""
Potion ini memberikan efek peningkatan HP monster sebesar 25% dari base HP.
Item ini hanya dapat digunakan sekali dalam battle. Tidak dapat digunakan
jika HP monster masih penuh."""
    elif (type == "DEF"):
        tampilan += f"""
Potion ini memberikan efek peningkatan DEF Power sebesar 5%. Item ini
hanya dapat digunakan sekali dalam battle. Tidak dapat digunakan jika
DEF Power monster sudah mencapai maksimum (50)."""
    else:
        tampilan += f"""
Potion ini memberikan efek peningkatan ATK Power sebesar 5%. Item ini
hanya dapat digunakan sekali dalam battle."""
    return(tampilan)

def TampilanInv(userMonsters: list, userPotions: list, user_id: str, username: str, userOC: int) -> str:
    # Spesifikasi:
        # men-generate tampilan utama untuk inventory user
        # Digunakan pada:
            # TampilInventoryUser -> F07

    # parameter input:
        # userMonsters = array of list[id,name,lvl,baseStat]
        # userPotions = array of list[type,qty]
        # userOC = int -> OC coin yang dimiliki user    
    # output:
        # tampilan = str

    NMonster = len(userMonsters)
    NPotion = len(userPotions)
    tampilan = f"""
========== {username.upper()}'S INVENTORY (User ID: {user_id}) ==========
Jumlah O.W.C.A Coin mu sekarang adalah {userOC}"""
    number = 0
    for i in range(NMonster):
        number += 1
        name = userMonsters[i][1]
        lvl = userMonsters[i][2]
        baseStat = userMonsters[i][3]
        stat = lvlStat(baseStat,lvl)
        tampilan += f"""
{number}. Monster       (Name: {name}, Lvl: {lvl}, HP: {stat[3]})"""
    for i in range(NPotion):
        if (userPotions[i][1] != 0):
            number += 1
            tampilan += f"""
{number}. Potion        (Type: {userPotions[i][0]}, Qty: {userPotions[i][1]})"""
        
    tampilan += """

Ketik id untuk melihat detail
Ketik 0 untuk keluar"""
    return(tampilan,number)

# FUNGSI UTAMA
def TampilInventoryUser(userMonsters: list, userPotions:list, user_id: str, username: str, userOC: int):
    # Spesifikasi:
        # menampilkan isi inventory user
        # Digunakan pada:
            # main

    # parameter input:
        # userMonsters = array of list[id,name,lvl,baseStat]
        # userPotions = array of list[type,qty]
        # userBalls = array of list[type,qty]
        # userOC = int -> OC coin yang dimiliki user    

    # Inisialisasi
    NMonster = len(userMonsters)
    (tampilan,number) = TampilanInv(userMonsters, userPotions, user_id, username, userOC)
    
    # Range Valid
    pilihanValid = [str(i) for i in range(number+1)]
    rangeMonster = range(1,NMonster+1)
    rangePotion = range(NMonster+1, number+1)
    # Looping, pilih = 0 -> keluar
    pilih = 1
    while (pilih != 0):
        pilih = inputValid(tampilan,"",pilihanValid,"int")
        if (pilih == 0):
            return()
        elif (pilih in rangeMonster):
            monster = userMonsters[pilih-1]          
            print(TampilMonsterDetail(monster))
        elif (pilih in rangePotion):
            pilih = pilih-NMonster
            print(TampilPotionDetail(userPotions,pilih))

        if not(KembaliKeInventory()):
            return ()
    return()
# end of line