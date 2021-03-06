from glob import glob
from threading import local
from turtle import clear, st
import pandas as pd
import openpyxl
from pkg_resources import FileMetadata
import datetime
import numpy as np
import re
import sys
import os


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
            print("Mohon masukkan angka 1/2 : ")
        else:
            if cmu in [1,2]:
                break
            else:
                print("Mohon masukkan angka 1/2 : ")
                pass
        
def cek_login_member():
    global cek_member
    print("============================================")
    while True:
        try:
            cek_member = str(input("Apakah anda memiliki member? Y/N  : ")).upper()
        except:
            print("Mohon ketik Y jika anda memiliki member dan ketik N jika belum mempunyai member. ")
        else:
            if cek_member in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika anda memiliki member dan ketik N jika belum mempunyai member. ")
                pass
    if cek_member == 'Y':
        login_member()
    elif cek_member == 'N':
        register()
    else:
        print("Mohon ketik Y jika anda memiliki member dan ketik N jika belum mempunyai member. ")
        cek_login_member()

def login_member():
    global nama
    global no_ident
    global user
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Member")
    df=pd.DataFrame(database)
    
    print("============================================")
    user = str(input("Username : "))
    password = str(input("Password : "))
    if  user in list(df['Username'].values):
        if password in list(df.loc[df.Username==user,'Password']):
            nama = df.loc[df.Username==user,'Nama'].to_string(index=False)
            no_ident = (df.loc[df.Username==user,'Nomor identitas']).to_string(index=False)
            print("============================================")
            print("\t      Login sukses!")
            menu_member()
        else:
            ("============================================")
            print("\t      Password salah!")
            return login_member()
    else:
        ("============================================")
        print("\t Username tidak terdaftar!")
        return login_member()

def login_admin():
    print("============================================")
    while True:
        admin = str(input("Username : "))
        passadmin = str(input("Password : "))
        if admin == "admin":
            if passadmin == "admin":
                print("============================================")
                print("\t      Login sukses!")
                menu_admin()
                break
            else:
                print("============================================")
                print("Password salah!")
        else:
            print("============================================")
            print("Username salah!")
            print("============================================")

def validasi_nomer(nomor_hp):
    pola = re.compile('(08)?[0-9]\d{9}')
    return pola.match(nomor_hp)

def validasi_nik(nomor_identitas):
    pola = re.compile('[0-9]\d{15}')
    return pola.match(nomor_identitas)

def register():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Member")
    df=pd.DataFrame(database)

    print("============ BUAT MEMBER ANDA =============")
    nama = str(input("Nama\t\t\t\t: "))
    list1 = nama.split()
    real_nama = ""
    for e in list1:
        real_nama = real_nama + e.capitalize() + " "
    alamat = str(input("Alamat\t\t\t\t: "))
    tanggal_lahir = str(input("Tanggal lahir (HH/BB/TTTT)\t: "))
    while True:
        identitas = str(input("Identitas (SIM/KTP)\t\t: ")).upper()
        if identitas == "SIM" or identitas == "KTP":
            break
        else:
            print("Masukkan data dengan benar!")
    while True:
        nomor_identitas = input("Nomor identitas\t\t\t: ")
        if validasi_nik(nomor_identitas):
            nomor_identitas = str(nomor_identitas) + ' '
            break
        else:
            print("Masukkan data dengan benar!")
    while True:
        nomor_hp = input("Nomor HP\t\t\t: ")
        if validasi_nomer(nomor_hp):
            nomor_hp = str(nomor_hp)+ ' '
            break
        else:
            print("Masukkan data dengan benar!")
    while True:
        username = str(input("Username\t\t\t: "))
        if username in (df['Username'].values):
            print("Username tidak tersedia! ") 
        else:
            break
    password = str(input("Password\t\t\t: "))
    
    print("============================================")
    print("Nama\t\t = ", real_nama )
    print("Alamat\t\t = ", alamat)
    print("Tanggal lahir\t = ", tanggal_lahir)
    print("Identitas\t = ", identitas)
    print("Nomor Identitas\t = ", nomor_identitas)
    print("Nomor HP\t = ", nomor_hp)
    print("Username\t = ", username)
    print("Password\t = " , password) 
    print("============================================")

    datamember = ({'Nama': real_nama, 'Alamat' : alamat, 'Tanggal Lahir' : str(tanggal_lahir), 'Identitas' : identitas, 'Nomor identitas' : str(nomor_identitas),'Nomor HP': str(nomor_hp),'Username': username,'Password' : str(password)})
    while True:
        try:
            cekdata = input("Apakah data sudah benar? Y/N : ").upper()
        except:
            print("Mohon ketik Y jika data anda sudah benar dan ketik N jika data salah. ")
        else:
            if cekdata in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika data anda sudah benar dan ketik N jika data salah. ")
                pass
    if cekdata == "Y":
        print("============================================")
        df= df.append(datamember,ignore_index= True)
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl',if_sheet_exists='overlay') as writer:
            df.to_excel(writer,sheet_name="Data Member",index= False)
        print("Registrasi Berhasil") 
        print("============================================")   
        return progam()
    elif cekdata == 'N':
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        return register ()
    else:
        print("============================================")
        print("Mohon ketik Y jika data anda sudah benar dan ketik N jika data salah. ")
        return register ()

def menu_admin():
    global el
    print("==================MENU======================")
    print("1. Edit ")
    print("2. List penyewa ")
    print("3. Log out ")
    print("============================================")
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

def act_menu_admin():
    global el
    
    if el == 1:
       menu_edit()
    elif el == 2:
        list_penyewa()
    else:
        print("============================================")
        print("\t     Berhasil Logout !")
        print("============================================")
        pass
        return progam()

def list_penyewa():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Sewa")
    df=pd.DataFrame(database)
    print("===================================================================================================================================================================")
    print(df.to_string(index=False))
    print("===================================================================================================================================================================")

    menu_admin()

def menu_edit():
    global me
    print("=================EDIT MENU==================")
    print("1. List CD")
    print("2. Genre ")
    print("3. Kembali ")
    print("============================================")
    while True:
        try:
            me = int(input("Mohon masukkan angka 1/2/3 : "))
        except:
            print("Mohon masukkan angka 1/2/3 :")
        else:
            if me in [1,2,3]:
                act_menu_edit()
                break
            else:
                print("Mohon masukkan angka 1/2/3 :")
                pass
    return me, True

def act_menu_edit():
    global me
    if me == 1:
        menu_editlistCD()
    elif me == 2:
        menu_genre()
    else:
        menu_admin()

def menu_genre():
    global meg
    print("=================EDIT GENRE=================")
    print("1. Tambah Genre")
    print("2. Hapus Genre ")
    print("3. Kembali ")
    print("============================================")
    while True:
        try:
            meg = int(input("Mohon masukkan angka 1/2/3 : "))
        except:
                print("Mohon masukkan angka 1/2/3 : ")
        else:
            if meg in [1,2,3]:
                act_menu_genre()
                break
            else:
                print("Mohon masukkan angka 1/2/3 : ")
                pass
    return meg, True

def act_menu_genre():
    global meg
    if meg == 1:
        tambah_genre()
    elif meg == 2:
        hapus_genre()
    else:
        menu_edit()
    
def tambah_genre():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Genre")
    df=pd.DataFrame(database)   

    print("============================================")
    genre_baru = str(input("Input genre baru :  "))
    list1 = genre_baru.split()
    real_genre = ""
    for e in list1:
        real_genre = real_genre + e.capitalize() + " "
    n = len(df["Genre"])
    new_id_genre= ord("A") + n
    id_genre= chr(new_id_genre)
    if id_genre in list(df['Kode'].values):
        id_genre=chr(new_id_genre+1)
        data_genre = ({'Kode': id_genre, 'Genre' : real_genre})
        df = df.append(data_genre,ignore_index= True)
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
            df.to_excel(writer,sheet_name="Data Genre",index= False)
        menu_genre()
    else:
        data_genre = ({'Kode': id_genre, 'Genre' : real_genre})
        df = df.append(data_genre,ignore_index= True)
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
            df.to_excel(writer,sheet_name="Data Genre",index= False)
        menu_genre()

def hapus_genre():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Genre")
    df=pd.DataFrame(database)
    

    data = df.loc[:,['Genre','Kode']]
    print("============================================")
    print(data.to_string(index=False))
    print("============================================")
    kode_genre = str(input("Masukkan kode genre yang ingin anda hapus : ")).upper()
    data_genre = df.loc[df.Kode==kode_genre,'Genre']
    print("Apa anda yakin ingin menghapus ", data_genre.to_string(index=False) ,"?")
    while True:
        try:
            validasi_delete = str(input( "Y/N : ")).upper()
        except:
            print("Mohon ketik Y jika anda ingin menghapus genre dan ketik N jika tidak. ")
        else:
            if validasi_delete in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika anda ingin menghapus genre dan ketik N jika tidak. ")
                pass
    if validasi_delete == "Y":
        delete_data_genre = df[df['Kode'] != kode_genre]
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
            delete_data_genre.to_excel(writer,sheet_name="Data Genre",index= False)
        print("Genre telah dihapus!")
        menu_genre()
    else:
        print("============================================")
        print("Mohon masukkan kode genre dengan benar !")
        hapus_genre()

def menu_editlistCD():
    global elc
    print("=================EDIT LIST==================")
    print("1. Tambah judul CD")
    print("2. Hapus judul CD ")
    print("3. Edit stok CD ")
    print("4. Kembali ")
    print("============================================")
    while True:
        try:
            elc = int(input("Mohon masukkan angka 1/2/3 : "))
        except:
                print("Mohon masukkan angka 1/2/3 : ")
        else:
            if elc in [1,2,3,4]:
                act_menu_editlistCD()
                break
            else:
                print("Mohon masukkan angka 1/2/3 : ")
                pass
    return elc, True

def act_menu_editlistCD():
    global elc
    if elc == 1:
        pilih_genre()
        nambahCD()
    elif elc == 2:
        hapus_cd()
    elif elc == 3:
        ubah_stok()
    else:
        menu_edit()

def pilih_genre():
    global kode_genre
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Genre")
    df=pd.DataFrame(database)
    data = df.loc[:,['Genre','Kode']]
    print("============================================")
    print(data.to_string(index=False))
    print("============================================")
    kode_genre= str(input("Pilih kode genre yang ingin anda tambah judul CDnya : ")).upper()
    
def nambahCD():
    global real_judul_cd
    global kode_genre
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data CD")
    database2= pd.read_excel(file,sheet_name="Data Genre")
    df=pd.DataFrame(database)
    df2=pd.DataFrame(database2)
    print("============================================")
    while True:
        judul_cd = str(input("Judul CD\t: "))
        list1 = judul_cd.split()
        real_judul_cd = ""
        for e in list1:
            real_judul_cd = real_judul_cd + e.capitalize() + " "

        if real_judul_cd in (df['Judul CD'].values):
            print("Judul CD sudah ada! ")
            while True:
                try:
                    ask_nambah_stok = str(input("Apakah anda ingin menambah stok? Y/N : " )).upper()
                except:
                    print("Mohon ketik Y jika anda ingin menambah stok dan ketik N jika tidak. ")
                else:
                    if ask_nambah_stok in ['Y','N']:
                        break
                    else:
                        print("Mohon ketik Y jika anda ingin menambah stok dan ketik N jika tidak. ")
                        pass
            if ask_nambah_stok == 'Y':
                nambah_stok()
            else:
                nambahCD()
        else:
            break

    stok_cd = int(input("Stok CD\t\t: "))
    print("============================================")
    id_cd = kode_genre + str(len(df["ID"]) + 1)
    while True:
        if id_cd in list(df['ID'].values):
            id_cd = kode_genre + str(len(df["ID"])+ 2)
        else:
            break
    genre_cd = df2.loc[df2.Kode==kode_genre,'Genre'].to_string(index=False)
    print("Genre\t\t:", genre_cd)
    print("Judul CD\t:", real_judul_cd)
    print("Stok\t\t:", stok_cd)
    print("============================================")

    data_cd = ({'ID': id_cd, 'Genre': genre_cd, 'Judul CD': real_judul_cd, 'Stok': stok_cd, 'Stok tersedia': stok_cd})
    while True:
        try:
            cekdata = input("Apakah data sudah benar? Y/N : ").upper()
        except:
            print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum benar. ")
        else:
            if cekdata in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum benar. ")
                pass
    if cekdata == "Y":
        print("============================================")
        df= df.append(data_cd,ignore_index= True)
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl',if_sheet_exists='overlay') as writer:
            df.to_excel(writer,sheet_name="Data CD",index= False)
        print("Input CD berhasil!") 
        print("============================================")   
        return menu_edit()
    elif cekdata == "N":
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        return nambahCD()

def hapus_cd():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data CD")
    df=pd.DataFrame(database)

    data = df.loc[:,['ID','Judul CD']].to_string(index=False)
    print("============================================")
    print(data)
    print("============================================")
    
    id_cd = str(input("Masukkan ID CD yang ingin dihapus : ")).upper()
    validasi_delete_cd = df.loc[df.ID==id_cd,'Judul CD'].to_string(index=False)
    print("Apa anda yakin ingin menghapus ", validasi_delete_cd, "?")
    while True:
        try:
            validasi_delete = str(input( "Y/N :")).upper()
        except:
            print("Mohon ketik Y jika anda ingin menghapus", validasi_delete_cd, " dan ketik N jika tidak. ")
        else:
            if validasi_delete in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika anda ingin menghapus", validasi_delete_cd, " dan ketik N jika tidak. ")
                pass
    if validasi_delete == "Y":
        delete_data_cd = df[df['ID'] != id_cd]
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
            delete_data_cd.to_excel(writer,sheet_name="Data CD",index= False)
        print("Judul CD telah dihapus!")
        menu_editlistCD()
    elif validasi_delete == "N":
        print("============================================")
        print("Mohon masukkan ID CD dengan benar !")
        hapus_cd()

def nambah_stok():
    global real_judul_cd
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data CD")
    df=pd.DataFrame(database)

    new_stok = int(input("Masukkan jumlah stok baru : "))
    genre = df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Genre'].to_string(index=False)
    stok_lama = df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok'].to_string(index=False)
    int_stok_lama = df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok']
    stok_tersedia_lama = df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok tersedia']
    print("============================================") 
    print("Genre :", genre)
    print("Judul CD :", real_judul_cd)
    print("Stok lama :", stok_lama)
    print("Stok baru:", new_stok)
    print("============================================")
    while True:
        try:
            cekdata = input("Apakah data sudah benar? Y/N : ").upper()
        except:
            print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
        else:
            if cekdata in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
                pass
    if cekdata == "Y":
        if new_stok > int(int_stok_lama):
            new_stok_tersedia = (new_stok - int_stok_lama) + stok_tersedia_lama 
            df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok'] = new_stok
            df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok tersedia'] = new_stok_tersedia
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Data CD",index= False)
            print("Stok berhasil diubah!")
            menu_editlistCD()
        else:
            new_stok_tersedia = stok_tersedia_lama - (int_stok_lama - new_stok)
            df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok'] = new_stok
            df.loc[df.xs('Judul CD', axis=1)== real_judul_cd,'Stok tersedia'] = new_stok_tersedia
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Data CD",index= False)
            print("Stok berhasil diubah!")
            menu_editlistCD()
    else:
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        ubah_stok()

def ubah_stok():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data CD")
    df=pd.DataFrame(database)

    data = df.loc[:,'ID':'Stok'].to_string(index=False)
    print("============================================")
    print(data)
    print("============================================")
    id_stok_cd = str(input("Masukkan ID CD yang ingin diubah stoknya : ")).upper()
    new_stok = int(input("Masukkan jumlah stok baru :"))
    judul = df.loc[df.ID==id_stok_cd,'Judul CD'].to_string(index=False)
    genre = df.loc[df.ID==id_stok_cd,'Genre'].to_string(index=False)
    stok_lama = df.loc[df.ID==id_stok_cd,'Stok'].to_string(index=False)
    int_stok_lama = df.loc[df.ID==id_stok_cd,'Stok']
    stok_tersedia_lama = df.loc[df.ID==id_stok_cd,'Stok tersedia']
    print("============================================")
    print("Genre\t: ", genre)
    print("Judul CD\t: ", judul)
    print("Stok lama\t: ", stok_lama)
    print("Stok baru\t: ", new_stok)
    print("============================================")
    while True:
        try:
            cekdata = input("Apakah data sudah benar? Y/N : ").upper()
        except:
            print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
        else:
            if cekdata in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
                pass
    if cekdata == "Y":
        if new_stok > int(int_stok_lama):
            new_stok_tersedia = (new_stok - int_stok_lama) + stok_tersedia_lama
            df.loc[df.ID==id_stok_cd,'Stok'] = new_stok
            df.loc[df.ID==id_stok_cd,'Stok tersedia'] = new_stok_tersedia
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Data CD",index= False)
            print("Stok berhasil diubah!")
            menu_editlistCD()
        else:
            new_stok_tersedia = stok_tersedia_lama- (int_stok_lama - new_stok)
            df.loc[df.ID==id_stok_cd,'Stok'] = new_stok
            df.loc[df.ID==id_stok_cd,'Stok tersedia'] = new_stok_tersedia
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Data CD",index= False)
            print("Stok berhasil diubah!")
            menu_editlistCD()
    else:
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        ubah_stok()

def menu_member():
    global mm
    print("===================MENU=====================")
    print("1. Sewa CD ")
    print("2. Mengembalikan ")
    print("3. Log out ")
    print("============================================")
    while True:
        try:
            mm = int(input("Mohon masukkan angka 1/2/3 : "))
        except:
            print("Mohon masukkan angka 1/2/3 : ")
        else:
            if mm in [1,2,3]:
                act_menu_member()
                break
            else:
                print("Mohon masukkan angka 1/2/3 : ")
                pass
    return mm, True

def act_menu_member():
    global mm
    if mm == 1:
        sewa_cd()
    elif mm == 2:
        pengembalian()
    else:
        print("============================================")
        print("\t     Berhasil Logout !")
        print("============================================")
        pass
        return progam()

def sewa_cd():
    global judul_cd
    global lama_pinjam
    global biaya_sewa
    global no_ident
    global kode_cd

    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Genre")
    database2= pd.read_excel(file,sheet_name="Data CD")
    df=pd.DataFrame(database)
    df2=pd.DataFrame(database2)
    df.index = np.arange(1, len(df)+1)
    df2.index = np.arange(1, len(df2)+1)

    data = df.loc[:,['Genre','Kode']]
    print("=================Pilih Genre================")
    print(data.to_string(index=False))
    print("============================================")
    kode_genre = str(input("Masukkan kode genre yang diinginkan : ")).upper()
    print("============================================")
    id_genre = df.loc[df.Kode==kode_genre,'Genre'].to_string(index=False)
    list_cd = df2.loc[df2.Genre==id_genre, ['ID','Judul CD']].to_string(index=False)
    print(list_cd)
    print("============================================")
    kode_judul = input("Masukkan kode film yang ingin disewa\t: ").upper()
    judul_cd = df2.loc[df2.ID==kode_judul, 'Judul CD'].to_string(index=False)
    kode_cd = df2.loc[df2.ID==kode_judul, 'ID'].to_string(index=False)
    if df2.loc[df2.ID==kode_judul, 'Stok tersedia'].to_string(index=False) == '0':
        print("Stok CD telah habis!")
        sewa_cd()
    lama_pinjam = int(input("Lama peminjamaan (Dalam hari)\t\t: "))
    print("============================================")
    print("Judul\t\t:", judul_cd)
    print("Lama peminjaman\t:", lama_pinjam , "  hari")
    print("============================================")
    while True:
        try:
            validasi_sewa = str(input("Apakah data sudah benar? Y/N  : ")).upper()
        except:
            print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
        else:
            if validasi_sewa in ['Y','N']:
                break
            else:
                print("Mohon ketik Y jika data anda sudah benar dan ketik N jika belum. ")
                pass
    if validasi_sewa == "Y":
        stok_tersedia = df2.loc[df2.xs('Judul CD', axis=1)== judul_cd,'Stok tersedia']
        new_stok_tersedia = stok_tersedia - 1
        df2.loc[df2.xs('Judul CD', axis=1)== judul_cd,'Stok tersedia'] = new_stok_tersedia
        with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl',if_sheet_exists='overlay') as writer:
            df2.to_excel(writer,sheet_name="Data CD",index= False)
        biaya_sewa = lama_pinjam * 5000
        rincian()
        sewa_lagi = str(input("Apakah anda ingin menyewa lagi? Y/N :  ")).upper()
        if sewa_lagi == 'Y':
            sewa_cd()
        else:
            menu_member()
    else:
        print("============================================")
        print("Mohon masukkan data dengan benar !")
        sewa_cd()
                
def rincian():
    global judul_cd
    global lama_pinjam
    global biaya_sewa
    global nama
    global no_ident
    global kode_cd

    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Sewa")
    df=pd.DataFrame(database)

    hari_ini = datetime.date.today()
    tanggal_kembali= hari_ini + datetime.timedelta(days=lama_pinjam)
    while True:
        no = len(df["No"]) + 1
        if no in list(df['No'].values):
            no = no + 1
        else:
            break
    print("==================RINCIAN===================")
    print("Nama Lengkap\t\t: ", nama )
    print("No.Identitas\t\t: ", no_ident )
    print("Judul CD\t\t: ", judul_cd)
    print("Tanggal pinjam\t\t: ",  hari_ini)
    print("Lama peminjaman\t\t: ", lama_pinjam , "  hari")
    print("Tanggal kembali\t\t: ",  tanggal_kembali)
    print("Harga sewa\t\t: ", biaya_sewa)
    print("Kode transaksi\t\t: ", (str(no)+kode_cd))
    print("============================================")
    
    data_sewa = ({'No': no , 'Nama' : nama , 'No Identitas': str(no_ident) + ' ' ,'Kode transaksi' : (str(no)+kode_cd) ,'Judul CD' : judul_cd , "Tanggal Sewa" : str(hari_ini).split(',',1)[0] , "Tanggal Kembali" :str(tanggal_kembali).split(',',1)[0] , 'Status' : "Disewa", "Harga Sewa" : biaya_sewa, 'Tanggal Pengembalian' : '-', 'Denda' : '-', 'Total Harga': '-'})
    df= df.append(data_sewa,ignore_index= True)
    with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl',if_sheet_exists='overlay') as writer:
        df.to_excel(writer,sheet_name="Data Sewa",index= False)
    input("Tekan enter untuk melanjutkan....")
    menu_member()

def kelebihanhari():
    from datetime import datetime
    global hari_pengembalian
    global lebih_hari
    global tanggal_sewa

    lebih_hari = hari_pengembalian-tanggal_sewa.date()

def datesewa():
    global tanggal_sewa
    global str_tanggal_sewa
    from datetime import datetime
    tanggal_sewa = datetime.strptime(str_tanggal_sewa, '%Y-%m-%d')

def datekembali():
    global tanggal_kembali
    global str_tanggal_kembali
    from datetime import datetime
    tanggal_kembali = datetime.strptime(str_tanggal_kembali, '%Y-%m-%d')

def pengembalian ():
    file = "database.xlsx"
    database= pd.read_excel(file,sheet_name="Data Genre")
    database2= pd.read_excel(file,sheet_name="Data CD")
    database3= pd.read_excel(file,sheet_name="Data Sewa")
    df=pd.DataFrame(database)
    df2=pd.DataFrame(database2)
    df3=pd.DataFrame(database3)
    df.index = np.arange(1, len(df)+1)
    df2.index = np.arange(1, len(df2)+1)
    df3.index = np.arange(1, len(df3)+1)
    global str_tanggal_sewa
    global str_tanggal_kembali
    global hari_pengembalian
    global lebih_hari
    global tanggal_sewa
    global no_ident
    global user 
    print("============================================")
    status = "Dikembalikan"
    list2 = user.split()
    real_user = ""
    for e in list2:
        real_user = real_user + e.capitalize() + " "
    hari_pengembalian = datetime.date.today()
    while True:
        kode_transaksi = str(input("Masukkan kode transaksi (Apabila anda lupa kode transaksi, ketik 0) :  ")).upper()
        if kode_transaksi == '0':
            print("============================================")
            list_sewa_user = df3.loc[df3.xs('Nama', axis=1)==real_user,['Kode transaksi','Judul CD','Status']].to_string(index=False)
            print(list_sewa_user)
            print("============================================")
            input("Tekan enter untuk melanjutkan....")
            pengembalian()
        else:
            if kode_transaksi in list(df3.loc[df3.Nama==real_user,'Kode transaksi']):
                status_sewa = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Status'].to_string(index=False)
                if status_sewa == 'Dikembalikan':
                    print("============================================")
                    print("\tCD telah dikembalikan!")
                    menu_member()
                else:
                    break
            else:
                print("============================================")
                print("Transaksi sewa tidak dapat ditemukan!")
                lupa_kodesewa = input("Apakah anda lupa kode transaksi anda? Y/N : ").upper()
                if lupa_kodesewa == "Y":
                    print("============================================")
                    list_sewa_user = df3.loc[df3.xs('Nama', axis=1)==real_user,['Kode transaksi','Judul CD','Status']].to_string(index=False)
                    print(list_sewa_user)
                    input("Tekan enter untuk melanjutkan....")
                    print("============================================")
                else:
                    pengembalian()

    cd_disewa = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Judul CD'].to_string(index=False)
    nama_penyewa = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Nama'].to_string(index=False)
    str_tanggal_sewa = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Tanggal Sewa']
    str_tanggal_sewa = str_tanggal_sewa.to_string(index=False)
    str_tanggal_kembali = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Tanggal Kembali']
    str_tanggal_kembali = str_tanggal_kembali.to_string(index=False)
    harga_sewa = df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Harga Sewa']
    datekembali()
    datesewa()
    lama_sewa = (tanggal_kembali-tanggal_sewa)
    if nama_penyewa == nama:
        kelebihanhari()
        str_lebih_hari = str(lebih_hari).split(',',1)[0]
        str_lama_sewa = str(lama_sewa).split(',',1)[0]
        str_lebih_hari = str_lebih_hari.replace('days','')
        str_lebih_hari = str_lebih_hari.replace('day','')
        str_lama_sewa = str_lama_sewa.replace('days','')
        str_lama_sewa = str_lama_sewa.replace('day','')
        x = int(str_lebih_hari)
        y = int(str_lama_sewa)
        
        if x > y:
            denda = 5000* int(str_lebih_hari) 
            print("===================STRUK====================")
            print("Nama Lengkap\t\t: ", nama )
            print("No.Identitas\t\t: ", no_ident )
            print("Judul CD\t\t: ", cd_disewa)
            print("Kode transaksi\t\t: ", kode_transaksi)
            print("Tanggal sewa\t\t: ",  tanggal_sewa.date())
            print("Lama peminjaman\t\t: ", y , "hari")
            print("Tanggal pengembalian\t: ",  hari_pengembalian)
            print("Harga sewa\t\t: ", harga_sewa.to_string(index=False))
            print("Denda\t\t\t: ", denda)
            total_harga = int(harga_sewa) + int(denda)
            print("Total harga\t\t: ", total_harga )
            print("============================================")

            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Status'] = status
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Tanggal Pengembalian'] =str(hari_pengembalian).split(',',1)[0]
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Denda'] = denda
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Total Harga'] = total_harga
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df3.to_excel(writer,sheet_name="Data Sewa",index= False)
            stok_tersedia = df2.loc[df2.xs('Judul CD', axis=1)==cd_disewa,'Stok tersedia'].to_string(index=False)
            stok_baru = int(stok_tersedia) + 1
            df2.loc[df2.xs('Judul CD', axis=1)==cd_disewa,'Stok tersedia'] = stok_baru
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df2.to_excel(writer,sheet_name="Data CD",index= False)
            input("Tekan enter untuk melanjutkan....")
            menu_member()
        else:
            print("===================STRUK====================")
            print("Nama Lengkap\t\t: ", nama )
            print("No.Identitas\t\t: ", no_ident )
            print("Judul CD\t\t: ", cd_disewa)
            print("Kode transaksi\t\t: ", kode_transaksi)
            print("Tanggal sewa\t\t: ",  tanggal_sewa.date())
            print("Lama peminjaman\t\t: ", y  , "hari")
            print("Tanggal pengembalian\t: ",  hari_pengembalian)
            print("Harga sewa\t\t: ", harga_sewa.to_string(index=False))
            print("Denda\t\t\t: - ")
            print("Total harga\t\t: ", harga_sewa.to_string(index=False))
            print("============================================")
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Status'] = status
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Tanggal Pengembalian'] = str(hari_pengembalian).split(',',1)[0]
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Denda'] = "-"
            df3.loc[df3.xs('Kode transaksi', axis=1)==kode_transaksi,'Total Harga'] = harga_sewa
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df3.to_excel(writer,sheet_name="Data Sewa",index= False)
            stok_tersedia = df2.loc[df2.xs('Judul CD', axis=1)==cd_disewa,'Stok tersedia'].to_string(index=False)
            stok_baru = int(stok_tersedia) + 1
            df2.loc[df2.xs('Judul CD', axis=1)==cd_disewa,'Stok tersedia'] = stok_baru
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df2.to_excel(writer,sheet_name="Data CD",index= False)
            input("Tekan enter untuk melanjutkan....")
            menu_member()
    else:
        print("Transaksi sewa tidak dapat ditemukan!")
        lupa_kodesewa = input("Apakah anda lupa kode transaksi anda? Y/N : ").upper()
        if lupa_kodesewa == "Y":
            list_sewa_user = df3.loc[df3.xs('Nama', axis=1)==real_user,['Kode transaksi','Judul CD','Status']].to_string(index=False)
            print(list_sewa_user)
            input("Tekan enter untuk melanjutkan....")
            pengembalian()

        else:
            pengembalian()

def progam():
    global cmu
    global el
    menu_utama()
    if cmu == 1 :
        cek_login_member()
    else:
        login_admin()

if __name__ == '__main__':
    progam()