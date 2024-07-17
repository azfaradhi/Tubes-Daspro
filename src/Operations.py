import time

# custom split
def splitter(text):
    hasil = []
    data = ""
    for i in range(len(text)):
        if (text[i] == ";"):
            hasil.append(data)
            data = ""
        else:
            data += text[i]
    hasil.append(data)
    return(hasil)

def read_csv(filename):
    data = []
    with open(filename, "r") as file:
        for row in file:
            data.append(splitter(row))
    return data

# Looping input hingga valid: berdasarkan type dan range input yg valid
# textInput digunakan jika tampilan opsi berupa text (>1 line), tidak digunakan = ""
# lineInput digunakan jika tampilan opsi berupa line          , tidak digunakan = ""
# pilihanValid adalah array dengan setiap macam input yang valid
def inputValid(textInput,lineInput,pilihanValid,typeValid):
    print(textInput)
    if (lineInput == ""):
        pilih = input("""
>>> Pilih: """).lower()
    elif (textInput == ""):
        pilih = input(f">>> {lineInput} ")
    else:
        pilih = input(f"""
>>> {lineInput} """).lower()

    while not(pilih in pilihanValid):
        time.sleep(0.5)
        print(f"""
[Peringatan] Pilihan tidak sesuai!     
{textInput}""")
        if (lineInput == ""):
            pilih = input("""
>>> Pilih: """).lower()
        elif (textInput == ""):
            pilih = input(f">>> {lineInput} ")
        else:
            pilih = input(f"""
>>> {lineInput} """).lower()
        
    if (typeValid == "int"):
        pilih = int(pilih)
            
    return(pilih)