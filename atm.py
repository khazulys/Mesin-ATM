import inquirer, re, json
import sys, time
from faker import Faker

nasabah = {
    "details":{
        "nama":"Khazul Yussery Shadiq",
        "pin":123456,
        "bank":"BRI Britama",
        "saldo":1000000
    }
}
u_pin=nasabah["details"]["pin"]
u_saldo=nasabah['details']["saldo"]
f_name = Faker('id_ID')

# Membuat Countdown timer
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print("Tunggu sebentar",timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1

# Membuat Cetak Struk
def transaksi(amount):
    global u_saldo
    total = u_saldo - amount
    return total

def menu_transaksi():
    global u_saldo
    qs = [
        inquirer.List("menu",
        message = "Silahkan pilih transaksi?",
        choices = ["Tarik Saldo","Transfer","Cek Saldo"],
        ),
    ]
    answers = inquirer.prompt(qs)
    if answers["menu"] == "Tarik Saldo":
        amount = int(input("Masukkan jumlah yang ingin di tarik:\n>> "))
        countdown(5)
        print("Silahkan Ambil uang kamu")
        print("Sisa Saldo : %d" % transaksi(amount))
        print("Thank you {0}".format(nasabah["details"]["nama"]))
        u_saldo = transaksi(amount)
    elif answers["menu"] == "Transfer":
        while True:
            no_rek = input("Nomor rekening tujuan\n>> ")
            valid = re.compile(r"\d{10}")
            if re.search(valid, no_rek):
                print("\nDetail Informasi")
                print("="*25)
                print("Nama : %s" % f_name.name())
                print("No.rek tujuan : %s" % no_rek)
                print("="*25)
                ask = input("Apakah data diatas sudah benar? ")
                if ask == "ya":
                    amount = int(input("\nMasukkan jumlah yang ingin di transfer:\n>> "))
                    countdown(5)
                    print("Transaksi Anda telah berhasil")
                    print("Sisa Saldo: %d" % transaksi(amount))
                    u_saldo=transaksi(amount)
                    break
                else:
                    continue
            else:
                continue
    else:
        print("Total Saldo rekening kamu :",u_saldo)

def userValidation(u_input):
    global u_pin
    if u_input == u_pin:
        menu_transaksi()
    else:
        return False
        
if __name__=="__main__":
    print("Selamat Datang di Mesin ATM")
    while True:
        u_input = int(input("Masukkan PIN kamu untuk bertransaksi?\n>> "))
        if not u_input:
            sys.exit(1)
        if userValidation(u_input) is False:
            print("PIN anda salah!")
            continue
        usr = input("\nIngin bertransaksi lagi? ")
        if usr == "ya":
            continue
        else:
            print("Terima Kasih")
            break            
