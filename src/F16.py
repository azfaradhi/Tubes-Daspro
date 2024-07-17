def exit():
    pilihan_user = input("Apakah Anda yakin ingin keluar dari program? Semua file yang tidak di save akan terhapus! (y/n): ").lower()
    while True:
        if pilihan_user == 'y':
            return True
        elif pilihan_user == 'n':
            print("Kembali ke program.") #balik ke program
            return False
        else:
            print("Pilihan tidak valid!")
            pilihan_user = input("Apakah Anda yakin ingin keluar dari program? Semua file yang tidak di save akan terhapus! (y/n): ").lower()