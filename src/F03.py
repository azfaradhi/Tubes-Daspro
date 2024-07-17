def logout() -> bool:
    # Spesifikasi:
    # Memastikan jika pengguna akan logout dari permainan
    # Digunakan pada:
        # F04

    # parameter input:
        # TIDAK ADA

    # output:
        # bool
    
    # Validasi apakah user akan logout
    pilihan_user = input("Apakah Anda yakin ingin logout? Semua file yang tidak di save akan terhapus! (y/n): ").lower()
    while True:
        if pilihan_user == 'y':
            return True
        elif pilihan_user == 'n':
            print("Kembali ke program.") # kembali ke program sebelumnya
            return False
        else:
            print("Pilihan tidak valid!")
            pilihan_user = input("Apakah Anda yakin ingin keluar dari program? Semua file yang tidak di save akan terhapus! (y/n): ").lower()