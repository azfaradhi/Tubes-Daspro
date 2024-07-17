from Operations import inputValid

def PeningkatanEfek(opsi: int, potions: list, stat: list) -> tuple:
    # Spesifikasi:
        # menghitung peningkatan efek dan men-generate hasil tampilan berdasarkan opsi pilihan user
        # Batasan:
            # opsi pasti >= 1
            # qty pada potions[opsi-1] bisa saja 0, ini digunakan agar dapat dikembalikan pada userPotion
            # akibatnya jika qty potion sebelum opsi = 0, letak opsi sebenarnya bergeser 1 ke kanan
        # Digunakan pada:
            # PotionUse -> F06

    # parameter input:
        # opsi = integer[1..)
        # potions = array[0..2] of list[type,qty,uses]
            # type = string (ATK/DEF/Heal)
            # qty = integer[0..)
            # uses = integer(0/1)
        # stat = array[0..3] of int -> stat monster berdasarkan level
    # output:
        # i = integer -> letak opsi sebenarnya (dalam bentuk index: i - 1)
        # statID = integer -> id stat yang ditingkatkan
            # statID = 0 -> ATK
            # statID = 1 -> DEF
            # statID = 2 -> HP
        # efek = float -> stat[statID] setelah penggunaan potion
        # tampilan = string -> tampilan efek penggunaan potion, user hanya dapat melihat 2 digit desimal
        
    # Inisialisasi
    NPotion = len(potions)
    i = 0

    # Cek letak opsi sebenarnya
    while (i < NPotion) and (opsi != 0):
        if (potions[i][1] != 0):
            opsi -= 1
        i += 1

    # Cek stat yang ditingkatkan
    if (potions[i-1][0] == "Heal"):
        jenisStat = "HP"
        statID = 2
        efek = stat[2] * 1.25
        if (efek > stat[3]):
            efek = stat[3]
    elif (potions[i-1][0] == "ATK"):
        jenisStat = "ATK Power"
        statID = 0
        efek = stat[0] * 1.05
    else:
        jenisStat = "DEF Power"
        statID = 1
        efek = stat[1] * 1.05
        if (efek > 50):
            efek = 50
    
    efek = int(efek)
    # Generate tampilan
    tampilan = f"""
Efek:
{jenisStat} = {stat[statID]} --> {efek}"""
    
    return(i,statID,efek,tampilan)

def GunakanPotionLain() -> bool:
    # Spesifikasi:
        # menghasilkan statement apakah user akan menggunakan potion lain atau tidak
        # Digunakan pada:
            # PotionUse -> F06

    # Inisialisasi
    pilihanValid = ["y","Y","n","N"]
    lineInput = "Mau gunakan potion lain? (y/n)"

    # Input hingga valid
    pilih = inputValid("",lineInput,pilihanValid,"str").lower()
    if (pilih == "y"):
        return(True)
    else:
        return(False)

def TampilanPotionUse(potions: list) -> str: 
    # Spesifikasi:
        # men-generate tampilan utama untuk PotionUse
        # Digunakan pada:
            # PotionUse -> F06

    # parameter input:
        # potions = array[0..2] of list[type,qty,uses]
            # type = string (ATK/DEF/Heal)
            # qty = integer[0..)
            # uses = integer(0/1)
    # output:
        # tampilan = string -> tampilan utama PotionUse

    # Inisialisasi
    NPotion = len(potions)
    tampilan = f"""
Pilih potion:"""
    
    # Generate tampilan
    number = 1
    for i in range(NPotion):
        if (potions[i][0] == "ATK"):
             namaPotion = "Strength Potion"
        elif (potions[i][0] == "DEF"):
             namaPotion = "Resilience Potion"
        else:
             namaPotion = "Healing Potion"

        if (potions[i][1] != 0):
            tampilan += f"""
{number}. {namaPotion}""" + " "*(20-len(namaPotion)) + f"(Qty: {potions[i][1]}| Uses: {potions[i][2]})"
            number += 1

    tampilan += f"""
{number}. Cancel"""
    
    return(tampilan,number)

# FUNGSI UTAMA
def PotionUse(stat: list,potions: list) -> tuple:
    # Spesifikasi:
        # ditampilkan jika user memilih untuk menggunakan potion dalam battle
        # Digunakan pada:
            # BattleTurns -> F08

    # parameter input:
        # potions = array[0..2] of list[type,qty,uses]
            # type = string (ATK/DEF/Heal)
            # qty = integer[0..)
            # uses = integer(0/1)
        # stat = array[0..3] of int -> stat monster berdasarkan level
    # output:
        # potion -> berubah tergantung penggunaan
        # stat -> berubah tergantung penggunaan
        # used = 0 jika digunakan, 1 jika tidak

    # Inisialisasi
    used = 0
    (tampilan,cancel) = TampilanPotionUse(potions)

    # Range Valid
    optionsValid = [str(i+1) for i in range(cancel)]
    pilihanValid = ["y","Y","n","N"]

    # Looping opsi = cancel -> keluar
    opsi = cancel-1
    while (opsi != cancel):
        opsi = inputValid(tampilan,"",optionsValid,"int")

        if (opsi == cancel):
            return (stat,potions,used)
        else:
            # Cek HP -> penuh gk bisa isi
            if (potions[opsi-1][0] == "Heal") and (stat[2] == stat[3]):
                print("""
[Peringatan] HP masih penuh.
Tidak bisa menggunakan Healing potion.""")
            elif (potions[opsi-1][0] == "DEF") and (stat[1] == 50.0):
                print("""
[Peringatan] DEF monster sudah mencapai batas maksimum.
Tidak bisa menggunakan Resilience potion.""")
            else:
                (i, statID, efek, textInput) = PeningkatanEfek(opsi, potions, stat)
                lineInput = "Yakin ingin menggunakan potion ini? (y/n)"
                pilih = inputValid(textInput,lineInput,pilihanValid,"str").lower()
                if (pilih == "y"):
                    stat[statID] = efek
                    potions[i-1][1] -= 1
                    potions[i-1][2] = 0
                    used = 1
                    return(stat,potions,used) 
        if not(GunakanPotionLain()):
            return (stat,potions,used)
    return(stat,potions,used)
# end of line