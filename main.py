import os, time

## Struktur data
TEMPLATE = {
    "jenis": 30*" ",
    "nopol": 30*" ",
    "waktu": "dd-hh-m",
}

## Fungsi untuk tampilan menu
def view_menu():
    os.system("clear")
    print("SELAMAT DATANG DI")
    print("      PARKIR     ")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Cek Harga")
    print("4. Sort Data")
    print("5. Update Data")
    print("6. Delete Data")

## fungsi untuk membuat data
def create_data():
    os.system("clear")
    jenis_kendaraan = input("Masukkan Jenis Kendaraan\t: ")
    plat_kendaraan = input("Masukkan Nomor Kendaraan\t: ")
    waktu = time.strftime("%d-%H-%M")

    database = TEMPLATE.copy()

    database["jenis"] = jenis_kendaraan + TEMPLATE["jenis"][len(jenis_kendaraan):]
    database["nopol"] = plat_kendaraan + TEMPLATE["nopol"][len(plat_kendaraan):]
    database["waktu"] = waktu

    data = f'{database["jenis"]},{database["nopol"]},{database["waktu"]}\n'

    with open("data.txt","a",encoding="utf-8") as file:
        file.write(data)

## Fungsi untuk membaca data
def read_data():
    os.system("clear")
    with open("data.txt","r") as file:
        data = file.readlines()

        no = "No"
        jenis = "Jenis Kendaraan"
        waktutgl = "Waktu dan Tanggal Masuk"
        plat = "Plat Nomor"

        ### Atas 
        print("="*61)
        print(f"{no:2} | {plat:10} | {jenis:15} | {waktutgl:20} |")
        print("="*61)
        
        ### Kontent
        for index,content in enumerate(data):
            konten = content.split(",")
            
            jenis = konten[0]
            nopol = konten[1]
            waktutgl = konten[2].replace("\n","")

            print(f"{index+1:2} | {nopol:.10} | {jenis:.15} | {waktutgl:.20}\n", end="")    

        ### bawah
        print("="*61) 

        x = input("")

## Fungsi untuk mencari data
def cari_data(no_data):
    with open("data.txt","r") as file:
        content = file.readlines()
        pilih = content[no_data-1]

        return pilih

## Fungsi untuk mengecek harga
def cek_harga():
    read_data()

    no_data = int(input("Masukkan Nomor\t: "))

    pilih = cari_data(no_data)
    pilih = pilih.split(",")
    jenis = pilih[0]
    jenis = jenis.strip()
    
    jam_pelanggan = pilih[2].replace("-", "")
    jam_pelanggan = int(jam_pelanggan.replace("\n",""))

    jam_sekarang = int(time.strftime("%d%H%M"))

    total_waktu = abs(jam_sekarang - jam_pelanggan)

    if total_waktu <= 60 and jenis in ["mobil","truck","pickup"]:
        os.system("clear")
        print("="*30)
        print(f"Lama Parkir    : {total_waktu}")
        print(f"Tagihan Parkir : Rp 1.000.000")
        print("="*30)
    elif total_waktu <= 60 and jenis in ["motor","sepeda"]:
        os.system("clear")
        print("="*30)
        print(f"Lama Parkir    : {total_waktu}")
        print(f"Tagihan Parkir : Rp 2.000.000") 
        print("="*30)

    a = input((""))

## Fungsi untuk sorting
def sorting():
    os.system("clear")
    with open("data.txt","r") as file:
        data = file.readlines()
        data_tuple = [tuple(line.strip().split(',')) for line in data]
        data_sort = sorted(data_tuple, key=lambda x: int(x[1]))

        no = "No"
        jenis = "Jenis Kendaraan"
        waktutgl = "Waktu dan Tanggal Masuk"
        plat = "Plat Nomor"

        ### Atas 
        print("="*61)
        print(f"{no:2} | {plat:10} | {jenis:15} | {waktutgl:20} |")
        print("="*61)
        
        ### Kontent
        for index,content in enumerate(data_sort):
            jenis = content[0]
            nopol = content[1]
            waktutgl = content[2].replace("\n","")

            print(f"{index+1:2} | {nopol:.10} | {jenis:.15} | {waktutgl:.20}\n", end="")    

        ### bawah
        print("="*61) 

        x = input("")

## Fungsi untuk mengupdate data   
def update():
    read_data()
    usr_option = int(input("Masukkan Nomor Data Yang Ingin Di Update\t: "))
    
    data = cari_data(usr_option)
    data = data.split(",")
    jeniskendaraan = data[0]
    jeniskendaraan = jeniskendaraan.replace(" ","")
    platnomor = data[1]
    platnomor = platnomor.replace(" ","")
    waktu = data[2]
    waktu = waktu.replace(" ","")

    print("Pilih Data Yang Ingin Di Update\n1. Jenis Kendaraan\n2. Plat Nomor")
    opsi_update = input("Pilihan [1,2]\t: ")

    match opsi_update:
        case "1" : jeniskendaraan = input("Masukkan Jenis Kendaraan\t: ")
        case "2" : platnomor = input("Masukkan Nomor PLat\t:")

    data_str = f"{jeniskendaraan + ' '*20},{platnomor + ' '*20},{waktu + ' '*20}\n"

    pjng_data = len(data_str * (usr_option - 1))
    print(pjng_data)

    with open("data.txt","r+",encoding="utf-8") as file:
        file.seek(pjng_data*(usr_option-1))
        file.write(data_str)

## Program dimulai
while True:
    os.system("cls")
    view_menu()

    user_option = input("Masukkan Opsi\t: ")

    match user_option:
        case "1" : create_data()
        case "2" : read_data()
        case "3" : cek_harga()
        case "4" : sorting()
        case "5" : pass
        case "6" : pass
        case "7" : exit()