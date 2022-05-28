
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
