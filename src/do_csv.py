def read_csv(csv_file):
    data = []
    count_line = 1
    with open(csv_file, 'r') as file:
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
    return data


def add_csv(file_path, data):
    with open(file_path,'a') as csvfile:
        add = '\n' + ';'.join(map(str,data))
        csvfile.write(add)

def edit_csv(csv_file, index_baris, indeks_kolom, data_baru):
    data = read_csv(csv_file)
    databaru = str(data_baru)
    data[index_baris][indeks_kolom] = databaru

    with open(csv_file, 'w') as csvfile:
        for row in range(len(data)):
            if row == 0:
                baris = ';'.join(data[row])
                csvfile.write(baris)
            else:
                baris = '\n' + ';'.join(data[row])
                csvfile.write(baris)

def remove_csv(csv_file, indeks_baris):
    data = read_csv(csv_file)
    del data[indeks_baris]

    with open(csv_file, 'w') as csvfile:
        for row in range(len(data)):
            if row == 0:
                baris = ';'.join(data[row])
                csvfile.write(baris)
            else:
                baris = '\n' + ";".join(data[row])
                csvfile.write(baris)