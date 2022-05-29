
import pandas as pd
import openpyxl
from pkg_resources import FileMetadata

def menu_utama():
    global cmu
    print("============================================")
    print(" Selamat datang di progam persewaan CD ")
    print("============================================")
    print("1. Login Member ")
    print("2. Login Admin  ")
    print("============================================")
    while True:
        try:
            cmu = int(input("Mohon masukkan angka 1/2 : "))
        except:
            print("Mohon masukkan angka 1/2 :")
        else:
            if cmu in [1,2]:
                break
            else:
                print("Mohon masukkan angka 1/2 :")
                pass
        
def cek_login_member():
    global cek_member
    print("============================================")
    cek_member = str(input("Apakah anda memiliki member? Y/N  :"))
    if cek_member == 'Y':
        login_member()
    else:
        register()

def login_member():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Member")
    df=pd.DataFrame(database)
    
    print("============================================")
    user = str(input("Username: "))
    password = str(input("Password: "))
    if  user in list(df['Username'].values):
        if password in list(df['Password'].values):
            print("============================================")
            print("Login sukses")
        else:
            ("============================================")
            print("Password salah")
            return login_member()
    else:
        ("============================================")
        print("Username tidak terdaftar")
        return login_member()

def login_admin():
    print("============================================")
    while True:
        admin = str(input("Username : "))
        passadmin = str(input("Password : "))
        if admin == "admin":
            if passadmin == "admin":
                print("============================================")
                print("Login sukses!")
                menu_admin()
                break
            else:
                print("============================================")
                print("Password salah!")
        else:
            print("============================================")
            print("Username salah!")
            print("============================================")

def register():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Member")
    df=pd.DataFrame(database)

    print("============ BUAT MEMBER ANDA ============")
    nama = str(input("Nama :     "))
    alamat = str(input("Alamat :      "))
    tanggal_lahir = str(input("Tanggal lahir :     "))
    identitas = str(input("Identitas (SIM/KTP):  "))
    nomor_identitas = str(input("Nomor identitas :     "))
    nomor_hp = str(input("Nomor HP :      "))
    while True:
        username = str(input("Username :      "))
        if username in (df['Username'].values):
            print("Username tidak tersedia! ") 
        else:
            break
    password = str(input("Password :      "))
    
    print("============================================")
    print("Nama = ", nama )
    print("Alamat = ", alamat)
    print("Tanggal lahir = ", tanggal_lahir)
    print("Identitas = ", identitas)
    print("Nomor Identitas = ", nomor_identitas)
    print("Nomor HP = ", nomor_hp)
    print("Username = ", username)
    print("Password =" , password) 
    print("============================================")

    datamember = ({'Nama': nama, 'Alamat' : alamat, 'Tanggal Lahir' : tanggal_lahir, 'Identitas' : identitas, 'Nomor identitas' : nomor_identitas,'Nomor HP': nomor_hp,'Username': username,'Password' : password})

    cekdata = input("Apakah data sudah benar? Y/N : ")
    if cekdata == "Y":
        print("============================================")
        df= df.append(datamember,ignore_index= True)
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl',if_sheet_exists='overlay') as writer:
            df.to_excel(writer,sheet_name="Data Member",index= False)
        print("Registrasi Berhasil") 
        print("============================================")   
        return progam()
    else:
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        return register ()
    
def menu_admin():
    global el
    print("================MENU==================")
    print("1. Edit list CD ")
    print("2. List penyewa ")
    print("3. Log out ")
    print("======================================")
    while True:
        try:
            el = int(input("Mohon masukkan angka 1/2/3 : "))
        except:
            print("Mohon masukkan angka 1/2/3 :")
        else:
            if el in [1,2,3]:
                act_menu_admin()
                break
            else:
                print("Mohon masukkan angka 1/2/3 :")
                pass
    return el, True            