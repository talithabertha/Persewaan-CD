
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