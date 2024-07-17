import os
import time

def LCG(seed = None) -> int:
    # Spesifikasi:
    # men-generate angka secara acak
    # Digunakan pada:
        # random_number -> F00
        
    # parameter input:
        # None, memakai os.getpid dan time

    # output:
        # number = integer
    
    a = 1103515245
    c = 12345
    m = 2**31
    # membuat angka secara acak dengan LCG
    seed = int(os.getpid() + time.time()* 231)
    number = (a*seed + c) % m
    return number

def random_number(range:list = None) -> int:
    # Spesifikasi:
    # men-generate angka secara acak, namun dengan range tertentu
    # Digunakan pada:
        # register -> F01
        # CekBonus -> F09
        # monster_management -> F13
        
    # parameter input:
        # range: arr [1..2] of int

    # output:
        # number = integer
    
    a = 1103515245
    c = 12345
    m = 2**31
    x_n = (a * LCG() + c) % m
    if range is None:
        return x_n
    else:
        # membuat angka random, tetapi dengan batas interval
        return int((x_n/m) * (range[1] - range[0]) + range[0])