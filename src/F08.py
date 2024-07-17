from F00 import random_number
from F05 import lvlStat
from F06 import PotionUse
from Operations import inputValid
import time
import colorama
colorama.init()

def RandomMonster(monsters: list, lvl: int) -> list:
    # Spesifikasi:
        # men-generate random monster dengan level yang sudah ditentukan
        # Digunakan pada:
            # Battle -> F08
            # Arena -> F09

    # parameter input:
        # monsters = array of list[id,nama,lvl,baseStat]
    # output:
        # monster = list[id,nama,lvl,baseStat]

    rndmonster = monsters[random_number((1,len(monsters)))]
    id = int(rndmonster[0])
    nama = str(rndmonster[1])
    baseStat = [(int(rndmonster[i+2])) for i in range(3)]

    monster = [id,nama,lvl,baseStat]
    return(monster)

def KemunculanMonster(monster: list, character: str):
    # Spesifikasi:
        # menampilkan intro dan detail monster saat di awal battle
        # Digunakan pada:
            # BattleTurns -> F08
    
    # parameter input:
        # monster = list[id,nama,lvl,baseStat]
        # character = int -> username atau enemy

    name = monster[1]
    lvl = monster[2]
    stat = lvlStat(monster[3],lvl)
    time.sleep(0.5)
    if (character == "enemy"):
        print(colorama.Fore.RED, """
           _/\----//   
          /         \     //
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
""", colorama.Style.RESET_ALL)
        print(f"""
RAAWRRRR!!! Monster {name} telah muncul!!!""")
    else:
        print(f"""
RAAWRRRR!!! {character} mengeluarkan monster {name}!!!""")
    print(f"""
Name        : {name}
ATK Power   : {stat[0]}
Def Power   : {stat[1]}
HP          : {stat[2]}
Level       : {lvl}""")
    return()

def PilihUserMonster(userMonsters: list) -> list:
    # Spesifikasi
        # menghasilkan data monster pilihan user yang telah dimiliki user
        # Digunakan pada:
            # Battle -> F08
            # Arena -> F09

    # parameter input:
        # userMonsters = array of list[id,name,lvl,baseStat]

    NMonster = len(userMonsters)
    pilihanValid = [str(i+1) for i in range(NMonster)]
    tampilan = """
Pilih Monster-mu untuk bertarung!

========== MONSTER LIST =========="""
    for i in range(NMonster):
        tampilan += f"""
{i+1}. {userMonsters[i][1]}"""
    pilih = inputValid(tampilan, "", pilihanValid, "int")
    monster = userMonsters[pilih-1]
    return(monster)

def Skip(statMonster: list, statEnemy: list, turn: int) -> tuple:
    damageReceived = 0
    damageGiven = 0
    while (statMonster[2] > 0) and (statEnemy[2] > 0):
        if (turn % 2 == 1):
            ATKPower = statMonster[0]
            DEFPower = statEnemy[1]
            percent = random_number((-30, 30))
            ATK = int(ATKPower * (1 + percent/100))
            reduced = int(ATK * DEFPower/100)
            damage = ATK - reduced
            HPtarget = (statEnemy[2] - damage)//1
            if (HPtarget) < 0:
                HPtarget = 0
            statEnemy[2] = HPtarget
            damageGiven += damage
            turn += 1
        else:
            ATKPower = statEnemy[0]
            DEFPower = statMonster[1]
            percent = random_number((-30, 30))
            ATK = int(ATKPower * (1 + percent/100))
            reduced = int(ATK * DEFPower/100)
            damage = ATK - reduced
            HPtarget = (statMonster[2] - damage)//1
            if (HPtarget) < 0:
                HPtarget = 0
            statMonster[2] = HPtarget
            damageReceived += damage
            turn += 1
    if (statMonster[2] == 0):
        endedStatus = "kalah"
    else:
        endedStatus = "menang"
    return(endedStatus,damageReceived,damageGiven)
 
def Attack(statAtk: list, statDef: list, nameAtk: str, nameDef: str, chrAtk: str, chrDef: str) -> tuple:
    # Spesifikasi:
        # menghitung damage dan menampilkan serangan monster
        # Digunakan pada:
            # BattleTurns -> F08

    # parameter input:
        # Atk -> penyerang, Def -> bertahan
        # statAtk, statDef = array[0..3] of int
            # stat[0] -> atk
            # stat[1] -> def
            # stat[2], stat[3] -> hp, hp max
        # nameAtk, nameDef = str -> nama monster
        # chrAtk, chrDef = str -> username atau enemy

    # Kalkulasi
    ATKPower = statAtk[0]
    DEFPower = statDef[1]

    percent = random_number((-30,30))
    if percent >= 0:
        percentage = f"+{percent}%"
    else:
        percentage = f"{percent}%"

    ATK =  int(ATKPower * (1 + percent/100))
    reduced = int(ATK * DEFPower/100)
    result = ATK - reduced
    damage = result

    HPtarget = (statDef[2] - result)//1
    if (HPtarget) < 0:
        HPtarget = 0

    # Printing
    time.sleep(1)
    print(f"""
({chrAtk.upper()}) {nameAtk} menyerang!!!

({chrDef.upper()}) {nameDef}'s HP = {HPtarget}
    
===== Attack Detail =====
Attack Power : {ATK} ({percentage})
Reduced by   : {reduced} (-{int(DEFPower)}%)
Result       : {result}""")
    return(HPtarget,damage)

def CanUsePotion(battlePotion: list, monsterStat: list) -> bool:
    # Spesifikasi:
        # menentukan apakah user dapat menggunakan potion saat battle atau tidak
        # Digunakan pada:
            # BattleTurns -> F08

    # parameter input:
        # battlePotion = array of list[type,qty,uses]
        # uses = 0 atau qty = 0 untuk setiap potion maka user tidak dapat menggunakan

    can = False
    i = 0
    while (i < len(battlePotion)) and (not(can)):
        if (battlePotion[i][1] != 0) and (battlePotion[i][2] != 0):
            if (battlePotion[i][0] == "ATK"):
                can = True
            elif (battlePotion[i][0] == "DEF") and (monsterStat[1] < 50):
                can = True
            elif (battlePotion[i][0] == "Heal") and (monsterStat[2] < monsterStat[3]):
                can = True
        i += 1
    return(can) 

def BattleTurns(monster: list, enemy: list, userPotions: list, username: str) -> tuple:
    # Spesifikasi:
        # menampilkan giliran-giliran pada battle hingga berakhir
        # Digunakan pada:
            # Battle -> F08
            # Arena -> F09
    
    # parameter input:
        # monster, enemy = list[id,name,lvl,baseStat]
        # userPotions = array of list[type,qty]
    # output:
        # userPotions
        # totalDamageReceived, totalDamageGiven = float -> damage diterima dan diberikan
        # endedStatus = str (kabur/kalah/menang)

    # Inisialisasi
    ended = False
    turn = 1
    enemyName = enemy[1]
    enemyStat = lvlStat(enemy[3],enemy[2])
    monsterName = monster[1]
    monsterStat = lvlStat(monster[3],monster[2])

    battlePotion = userPotions
    for i in range(len(battlePotion)):
        battlePotion[i].append(1)

    textPilihan = """
1. Attack
2. Use Potion
3. Skip Battle
4. Quit"""
    pilihanValid = ["1","2","3","4"]

    totalDamageGiven = 0
    totalDamageReceived = 0

    # Turns
    while not(ended):
        time.sleep(1)
        if (turn % 2 == 1): # user turn
            textInput = f"""
========== TURN {turn} ({monsterName.upper()} - {username.upper()}) ==========""" + textPilihan
            pilih = inputValid(textInput,"",pilihanValid,"int")

            if (pilih == 1):
                (enemyStat[2],damageGiven) = Attack(monsterStat,enemyStat,monsterName,enemyName,username,"enemy")
                totalDamageGiven += damageGiven
                turn += 1
            elif (pilih == 2):
                if not(CanUsePotion(battlePotion,monsterStat)):
                    print("""
Tidak ada potion yang dapat digunakan.
Tidak dapat memilih potion.""")
                else:
                    (monsterStat,battlePotion,used) = PotionUse(monsterStat,battlePotion)
                    if (used == 1):
                        turn += 1
            elif (pilih == 3):
                textInput = """
Dengan memilih skip battle, monster dengan otomatis dalam keadaan menyerang"""
                lineInput = "Yakin ingin skip battle? (y/n)"
                opsiValid = ["y","Y","n","N"]
                opsi = inputValid(textInput,lineInput,opsiValid,"str")
                if (opsi.lower() == "y"):
                    (endedStatus, damageReceived, damageGiven) = Skip(monsterStat, enemyStat, turn)
                    totalDamageReceived += damageReceived
                    totalDamageGiven += damageGiven
            else:
                print("""
Anda melarikan diri dari pertarungan""")
                ended = True
                endedStatus = "kabur"
        else:   # enemy turn
            print(f"""
========== TURN {turn} ({enemyName.upper()} - {"enemy".upper()}) ==========""")
            (monsterStat[2], damageReceived) = Attack(enemyStat,monsterStat,enemyName,monsterName,"enemy",username)
            totalDamageReceived += damageReceived
            turn += 1

        # Cek HP monster dan enemy
        if not(ended):
            if (monsterStat[2] == 0):
                time.sleep(0.5)
                ended = True
                endedStatus = "kalah"
                print(f"""
Yahhh, Anda dikalahkan monster {enemyName}. Jangan menyerah, coba lain kali!!!""")
            elif (enemyStat[2] == 0):
                time.sleep(0.5)
                ended = True
                endedStatus = "menang"
                print(f"""
Selamat, Anda berhasil mengalahkan monster {enemyName}!!!""")

    # Kembalikan userPotions dari battlePotion 
    userPotions = [[battlePotion[i][j] for j in range(2)] for i in range(len(userPotions))]
    return (userPotions, totalDamageReceived, totalDamageGiven, endedStatus)

# FUNGSI UTAMA
def Battle(monsters: list, userMonsters: list, userPotions: list, username: str) -> tuple:
    # Spesifikasi:
        # men-generate lawan, memilih monster, dan melakukan battle
        # Digunakan pada:
            # main
    
    # parameter input:
        # monsters = list -> read_csv("monster.csv")
        # userMonsters = array of list[id,name,lvl,baseStat]
        # userPotions = array of list[type,qty]
    # output:
        # userPotions = array of list[type,qty]
        # bonus = int -> OC coin yang didapat

    print(colorama.Fore.CYAN,"""
██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗██╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██║
██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░██║
██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░╚═╝
██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗██╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═╝""", colorama.Style.RESET_ALL)
    print("Battle akan dimulai dalam...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    # Lawan Random Monster
    enemyLvl = random_number((1,5))
    enemy = RandomMonster(monsters, enemyLvl)
    KemunculanMonster(enemy, "enemy")

    # Pilih User Monster untuk bertarung
    monster = PilihUserMonster(userMonsters)
    KemunculanMonster(monster, username)

    # Battle
    (userPotions, damageReceived, damageGiven, endedStatus) = BattleTurns(monster, enemy, userPotions, username)

    # Cek bonus
    if (endedStatus != "menang"):
        bonus = 0
    else:
        bonus = random_number((30,50))
    
    time.sleep(1)
    print(f"""
=============== STATS ===============
Hadiah              : {bonus} OC
Damage diberikan    : {round(damageGiven,2)}
Damage diterima     : {round(damageReceived,2)}""")
    return(userPotions,bonus)