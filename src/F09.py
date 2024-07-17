from F00 import random_number
from F08 import RandomMonster, PilihUserMonster, KemunculanMonster, BattleTurns
import time

def CekBonus(endedStatus: str, stage: int) -> int:
    # Spesifikasi:
        # menghitung bonus OC coin berdasarkan endedStatus dan stage arena
        # Digunakan pada:
            # Arena -> F09
    
    # parameter input:
        # endedStatus = str (kabur/kalah/menang)

    time.sleep(0.5)
    if (endedStatus != "menang"):
        bonus = 0
        print(f"""
GAME OVER! Sesi latihan berakhir pada stage {stage}""")
    else:
        bonus = int(random_number((30,35))*(0.9 + 0.1*stage))
        print(f"""
STAGE CLEARED! Anda mendapatkan {bonus} OC pada stage ini""")
        
    if (stage == 5) and (endedStatus == "menang"):
        time.sleep(0.5)
        print("""
Selamat, Anda berhasil menyelesaikan seluruh stage arena!""")
    return(bonus)

# FUNGSI UTAMA
def Arena(userMonsters: list, userPotions: list, username: str, monsters: list) -> tuple:
    # Spesifikasi:
        # menjalankan arena: 5 stage, di setiap stage terdapat battle dengan lvl enemy = stage
        # Digunakan pada:
            # main
    
    # parameter input:
        # userMonsters = array of list[id,name,lvl,baseStat]
        # userPotions = array of list[type,qty]
        # monsters = list -> read_csv("monster.csv")
    # output:
        # userPotions = array of list[type,qty]
        # totalBonus = int -> total OC coin yang diperoleh

    # Inisialisasi
    print("""
Selamat datang di Arena!""")
    monster = PilihUserMonster(userMonsters)
    KemunculanMonster(monster, username)

    stage = 1
    clear = 0
    endedStatus = "menang"
    totalBonus = 0
    totalDamageReceived = 0
    totalDamageGiven = 0

    # Looping arena
    while (stage < 6) and (endedStatus == "menang"):
        if (stage != 1):
            time.sleep(1)
            print("""
Memulai stage berikutnya . . .""")
        time.sleep(1)
        print(f"""
=============== STAGE {stage} ===============""")

        enemy = RandomMonster(monsters,stage)
        KemunculanMonster(enemy, "enemy")
        (userPotions, damageReceived, damageGiven, endedStatus) = BattleTurns(monster, enemy, userPotions, username)
        bonus = CekBonus(endedStatus,stage)
        totalBonus += bonus
        totalDamageReceived += damageReceived
        totalDamageGiven += damageGiven

        if endedStatus == "menang":
            clear += 1
        stage += 1

    # writing result
    time.sleep(1)
    print(f"""
=============== STATS ===============
Total hadiah        : {totalBonus}
Jumlah stage        : {clear}
Damage diberikan    : {round(totalDamageGiven,2)}
Damage diterima     : {round(totalDamageReceived,2)}""")
    return(userPotions,totalBonus)
# end of line