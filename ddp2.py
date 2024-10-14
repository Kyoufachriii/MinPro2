# Loginn
def Login():
    while True:
        print("Ingin login sebagai apa?")
        print("Pilih Role Anda")
        print("---------------")
        print("[1] Admin")
        print("[2] Pelanggan")
        print("[3] Keluar")
        Role1 = input("Role: ")
        if Role1 == "1" :
            ladmin()
        elif Role1 == "2" :
            luser()
        elif Role1 == "3" :
            print("Terima Kasih Telah Menggunakan Layanan Ini")
            break
        else:
            print ("Angka Tidak Valid")


def ladmin():
    while True: 
        print("Hi Mimin!! Login Dulu Yak")
        print("Masukkan Nama Anda dan Sandi Dengan Benar")
        nama = input("Nama : ")
        sandi = int(input("Sandi : "))

        if nama == "pari" and sandi == 256 :
            print("Nama dan Sandi Benar, Hi Mimin!!")
            minmenu()
            break
        else :
                print("Nama atau Sandi Salah, Coba Lagi")
            


def luser():
    print ("------------------------------")
    print ("Hii Capell!! Selamat Datang!!")
    print ("Masukkan nama kamu ya!")
    print ("------------------------------")
    namapel = input("Nama : ")
    tanggapel = (input("Tanggal Login : "))
    keperluan = input("mau apa nihhh? : ")
    print ("------------------------------")
    capelmenu()


datapanggung = {
    1: {"Jenis Panggung": "Standar", "Ukuran": "4x6", "Price": "Rp450.000", "Status": "Tersedia"},
    2: {"Jenis Panggung": "VIP", "Ukuran": "6x8", "Price": "Rp650.000", "Status": "Tersedia"},
    3: {"Jenis Panggung": "Legend", "Ukuran": "8x10", "Price": "Rp900.000", "Status": "Tersedia"},
    4: {"Jenis Panggung": "Mythic", "Ukuran": "10x10", "Price": "Rp1.050.000", "Status": "Tersedia",}
}

# Tambah panggung baru
def tlpanggung():
    print("----------Tambah Panggung-----------")
    jenis = input("Masukkan Jenis Panggung: ")
    ukuran = input("Masukkan Ukuran Panggung (meter): ")
    harga = input("Masukkan Harga Panggung: ")
    status = input("Masukkan Status Panggung: ")
    # Menentukan kunci baru
    databaru = max(datapanggung.keys()) + 1
    datapanggung[databaru]= {"Jenis Panggung": jenis, "Ukuran": ukuran, "Price": harga, "Status": status}

    print(f"Panggung '{jenis}' berhasil ditambahkan.")

# Tampilkan list panggung
def ll():
    print("--------------------------------------------")
    print("Daftar Panggung:")
    for databaru, value in datapanggung.items():
        print(f"[{databaru}] Jenis: {value['Jenis Panggung']}, Ukuran: {value['Ukuran']}, Harga: {value['Price']}, Status: {value['Status']}")
    print("--------------------------------------------")

# perbarui status panggung
def plpanggung():
    ll()  # Tampilkan daftar panggung
    try:
        print("----------Perbarui Panggung----------")
        pilih = int(input("Masukkan nomor panggung yang ingin diperbarui: "))
        if pilih in datapanggung:
            jenis = input("Masukkan Jenis Panggung: ")
            ukuran = input("Masukkan Ukuran Panggung: ")
            harga = input("Masukkan Harga Panggung: ")
            status = input("Masukkan Status Panggung: ")
            # Perbarui data panggung 
            datapanggung[pilih] = {"Jenis Panggung": jenis, "Ukuran": ukuran, "Price": harga,"Status": status}
            print("Panggung berhasil diperbarui.")
        else:
            print("Nomor panggung tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
# panggung rusak, hapuss
def hlpanggung():
    ll()
    try:
        print("-----------Hapus Panggung------------")
        pilih = int(input("Masukkan nomor panggung yang ingin dihapus: "))
        if pilih in datapanggung:
            del datapanggung[pilih]
            print("Panggung berhasil dihapus.")
        else:
            print("Nomor panggung tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# menu mimin
def minmenu():
    while True:
        print("--------------------------------------------")
        print("Welcome back min!!")
        print("[1] Tambah list Panggung")
        print("[2] Lihat list")
        print("[3] Perbarui list panggung")
        print("[4] Hapus list panggung")
        print("[5] Keluar (⁠っ⁠˘̩⁠╭⁠╮⁠˘̩⁠)⁠っ")
        print("--------------------------------------------")

        minnu = input("Mau ngapain min? : ")
        if minnu == "1":
            tlpanggung()
        elif minnu == "2":
            ll()
        elif minnu == "3":
            plpanggung()
        elif minnu == "4":
            hlpanggung()
        elif minnu == "5":
            print("Bye min!! <⁠(⁠￣⁠︶⁠￣⁠)⁠>")
            Login()
            break
        else:
            print("Daftar Layanan Tidak Tersedia (⁠っ⁠˘̩⁠╭⁠╮⁠˘̩⁠)⁠っ ")
            print("-----------------------------------------------------")


#program pelanggan

def ldp():
    print("Hii Capel!!, Ini Dia List Panggung Yang Tersedia")
    print("---------------------------------------------------------------------")
    print("Daftar Panggung:")
    for databaru, value in datapanggung.items():
        print(f"[{databaru}] Jenis: {value['Jenis Panggung']}, Ukuran: {value['Ukuran']}, Harga: {value['Price']}, Status: {value['Status']}")
    print("---------------------------------------------------------------------")

def sewa():

    print("---------------------------------------------------------------------")
    ldp()  
    print("---------------------------------------------------------------------")

    # Input data diri
    nama = input("Nama        : ")
    alamat = input("Alamat      : ")
    tanggal = input("Tanggal     : ")
    lama_sewa = input("Lama Sewa : ")
    pilihan = input("Jenis Panggung :")
    print("Pesanan Telah Dibuat dan Akan Diproses ")
    print("-------------------------TERIMA KASIH-------------------------")
    

def capelmenu():
    while True:
        print("------------------------------------------------------------")
        print("Hi Capelll!! Ini Dia Daftar Layanan Kami!!")
        print("[1] List Daftar Panggung")
        print("[2] Sewa Panggung")
        print("[3] Keluar (⁠っ⁠˘̩⁠╭⁠╮⁠˘̩⁠)⁠っ")
        print("------------------------------------------------------------")

        playanan = input("Mau Pilih Layanan Apa Nihhh? : ")
        if playanan == "1":
            ldp()
        elif playanan == "2":
            sewa()                                                         
        elif playanan == "3":
            print("Terima Kasih Telah Menggunakan Layanan Ini!! <⁠(⁠￣⁠︶⁠￣⁠)⁠>")
            break 
        else:
            print("Daftar Layanan Tidak Tersedia (⁠っ⁠˘̩⁠╭⁠╮⁠˘̩⁠)⁠っ ")
            print("--------------------------------------------------------")
            print(" ")
            print("--------------------------------------------------------")
            print("Pilih Layanan Yang Tersedia (⁠╯⁠°⁠□⁠°⁠）⁠╯⁠︵⁠ ⁠┻⁠━⁠┻")

Login()