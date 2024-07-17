from Operations import inputValid

def lvlStat(baseStat: list,lvl: int) -> list:
    # Spesifikasi:
        # menghitung stat monster berdasarkan base stat dan lvl monster
        # Digunakan pada:
            # owcadex -> F05
            # RandomMonster -> F08
            # ...

    # parameter input:
        # baseStat = array[0..2] of int -> stat dasar monster pada lvl 1
            # baseStat[0] -> atk
            # baseStat[1] -> def
            # baseStat[2] -> hp
    # output:
        # stat = array[0..3] of int -> stat berdasarkan level
            # stat[0] -> atk
            # stat[1] -> def
            # stat[2], stat[3] -> hp, dibikin 2 u/ keperluan battle

    stat = [int(baseStat[i] * (1 + 0.1*(lvl-1))) for i in range(3)]
    if (stat[1] > 50):
        stat[1] = 50                                                # def max = 50
    stat.append(stat[2])                                            # ini untuk keperluan HP max saat battle
    return(stat)

def TampilMonsterDetail(monster: list) -> str:
    # Spesifikasi:
        # men-generate tampilan untuk tiap monster
        # Digunakan pada:
            # owcaDex -> F05
            # ...
        
    # parameter input:
        # monster = [id,nama,lvl,baseStat] -> [int,str,int,array of int]
        # baseStat = [atk,def,hp] -> array of int, user hanya dapat melihat 2 digit desimal
    # output:
        # tampilan = string

    id = monster[0]
    nama = monster[1]
    lvl = monster[2]
    stat = lvlStat(monster[3],lvl)
    tampilan = f"""
========== {nama.upper()} LVL {lvl} ==========
Monster id  : {id}
ATK Power   : {stat[0]}
DEF Power   : {stat[1]}
HP          : {stat[2]}"""
    return(tampilan)

def TampilanOwcaDex(monsters: list) -> str:
    # Spesifikasi:
        # men-generate tampilan utama OWCADEX
        # Digunakan pada:
            # owcaDex -> F05
            # ...
    
    # parameter input:
        # monsters = list -> read_csv("monster.csv")
    # output:
        # tampilan = string -> tampilan utama OWCADEX

    # Algoritma:
    tampilan = """
========== OWCA DEX =========="""
    for i in range(len(monsters)):
        tampilan += f"""
{i+1}. {monsters[i][1]}"""
    tampilan += f"""

Ketik 1-{len(monsters)} untuk melihat detail.
Ketik 0 untuk keluar"""
    return(tampilan)

# FUNGSI UTAMA
def owcaDex(monsters: list):
    # Spesifikasi:
        # menampilkan owcadex, library dimana user dapat melihat monster apa saja yang ada dalam game,
        # serta dapat melihat statusnya pada level 1-5
    
    # parameter input:
        # monsters = list -> read_csv("monster.csv")

    # inisialisasi
    tampilan = TampilanOwcaDex(monsters)
    idValid = [str(i) for i in range(len(monsters)+1)]
    lvlValid = [str(i) for i in range(6)]
    # Looping, id = 0 -> keluar
    id = 1
    while (id != 0):
        id = inputValid(tampilan,"",idValid,"int")
        if (id == 0):
            return()
        else:
            # lihat status monster dengan index id
            name = monsters[id-1][1]
            baseStat = [int(monsters[id-1][i+2]) for i in range(3)]
            monster = [id,name,1,baseStat]
            # Looping, lvl - 0 -> keluar
            lvl = 1
            while (lvl != 0):
                monster[2] = lvl
                tampilMonster = TampilMonsterDetail(monster)
                tampilMonster += """

Ketik 1-5 untuk melihat status monster pada level tersebut.
Ketik 0 untuk kembali ke OWCA DEX."""
                lvl = inputValid(tampilMonster,"",lvlValid,"int")
    return()
# end of line