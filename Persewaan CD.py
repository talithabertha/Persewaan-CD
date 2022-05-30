
from glob import escape
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

def menu_editlist():
    global es
    print("============EDIT LIST============")
    print("1. Menambah ")
    print("2. Mengurang ")
    print("3. Kembali ")
    print("==================================")
    while True:
        try:
            es = int(input("Mohon masukkan angka 1/2/3 :"))
        except:
                print("Mohon masukkan angka 1/2/3 :")
        else:
            if es in [1,2,3]:
                act_menu_editlist()
                break
            else:
                print("Mohon masukkan angka 1/2/3 :")
                pass
    return es, True

def act_menu_editlist():
    global es
    if es == 1:
        pilih_genre()
        nambahCD()
    else:
        pilih_genre()
        ngurangcd()

def act_menu_admin():
    global el
    
    if el == 1:
        menu_editlist()
    elif el == 2:
        pass
    else:
        print("====================")
        print("Berhasil Logout !")
        print("====================")
        pass

def pilih_genre():
    print("============================================")
    print("1.Romance")
    print("2.Horror/Thriller")
    print("3.Comedy")
    print("4.Action")
    print("============================================")

def nambahCD():
    global genre
    while True:
        try:
            genre= int(input("Pilih Genre"))
        except:
            print("Mohon masukkan angka 1/2/3/4 :")
        else:
            if genre in [1,2,3,4]:
                inputcd()
                break
            else:
                print("Mohon masukkan angka 1/2/3/4 :")
                pass

def inputcd():
    global genre
    if genre == 1:
        file = "database.xlsx"
        database= pd.read_excel(file,sheet_name="Genre 1")
        df=pd.DataFrame(database)

        judulcd = str(input("Judul CD :     "))
        stokcd = int(input("Stok :     "))
        print("==========================")
        print("Judul Film :", judulcd)
        print("Stok : ", stokcd)
        print("==========================")
        
        datacd = ({'Judul CD': judulcd, 'Stok' : stokcd})
        
        cekdata = input("Apakah data sudah benar? Y/N : ")
        if cekdata == "Y":
            print("============================================")
            df= df.append(datacd,ignore_index= True)
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Genre 1",index= False)
            print("Input CD berhasil!") 
            print("============================================")
            menu_admin()
        else:
            print("============================================")
            print("Mohon masukkan data dengan benar !")
            return inputcd()
    elif genre == 2:
        file = "database.xlsx"
        database= pd.read_excel(file,sheet_name="Genre 2")
        df=pd.DataFrame(database)

        judulcd = str(input("Judul CD :     "))
        stokcd = int(input("Stok :     "))
        print("==========================")
        print("Judul Film :", judulcd)
        print("Stok : ", stokcd)
        print("==========================")
        
        datacd = ({'Judul CD': judulcd, 'Stok' : stokcd})
        
        cekdata = input("Apakah data sudah benar? Y/N : ")
        if cekdata == "Y":
            print("============================================")
            df= df.append(datacd,ignore_index= True)
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Genre 2",index= False)
            print("Input CD berhasil!") 
            print("============================================")
            menu_admin()
        else:
            print("============================================")
            print("Mohon masukkan data dengan benar !")
            return inputcd()
    elif genre == 3:
        file = "database.xlsx"
        database= pd.read_excel(file,sheet_name="Genre 3")
        df=pd.DataFrame(database)

        judulcd = str(input("Judul CD :     "))
        stokcd = int(input("Stok :     "))
        print("==========================")
        print("Judul Film :", judulcd)
        print("Stok : ", stokcd)
        print("==========================")
        
        datacd = ({'Judul CD': judulcd, 'Stok' : stokcd})
        
        cekdata = input("Apakah data sudah benar? Y/N : ")
        if cekdata == "Y":
            print("============================================")
            df= df.append(datacd,ignore_index= True)
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer,sheet_name="Genre 3",index= False)
            print("Input CD berhasil!") 
            print("============================================")
            menu_admin()
        else:
            print("============================================")
            print("Mohon masukkan data dengan benar !")
            return inputcd()
    else:
        file = "database.xlsx"
        database= pd.read_excel(file,sheet_name="Genre 4")
        df=pd.DataFrame(database)

        judulcd = str(input("Judul CD :     "))
        stokcd = int(input("Stok :     "))
        print("==========================")
        print("Judul Film :", judulcd)
        print("Stok : ", stokcd)
        print("==========================")
        
        datacd = ({'Judul CD': judulcd, 'Stok' : stokcd})
        
        cekdata = input("Apakah data sudah benar? Y/N : ")
        if cekdata == "Y":
            print("============================================")
            df= df.append(datacd,ignore_index= True)
            with pd.ExcelWriter("database.xlsx", mode = "a",engine='openpyxl', if_sheet_exists='overlay') as writer:
                df.to_excel(writer,sheet_name="Genre 4",index= False)
            print("Input CD berhasil!") 
            print("============================================")
            menu_admin()
        else:
            print("============================================")
            print("Mohon masukkan data dengan benar !")
            return inputcd()

def ngurangcd():
    global genre
    while True:
        try:
            genre= int(input("Pilih Genre"))
        except:
            print("Mohon masukkan angka 1/2/3/4 :")
        else:
            if genre in [1,2,3,4]:
                removecd()
                break
            else:
                print("Mohon masukkan angka 1/2/3/4 :")
                pass

def removecd():
    global genre
    if genre == 1:
        filedata = "database.xlsx"
        database= pd.read_excel(filedata,sheet_name="Genre 1")
        file = openpyxl.load_workbook("database.xlsx")
        sheet = file['Genre 1']

        print(database)

        deletedata = int(input("Pilih film yang ingin anda hapus (1/2/3/...): "))
        data = database.loc[deletedata,'Judul CD']
        print("Apa anda yakin ingin menghapus ", data ,"?")
        validasi_delete = str(input( "Y/N :"))
        if validasi_delete == "Y":
            real_delete_data = deletedata + 2
            sheet.delete_rows(idx=real_delete_data)
            file.save("database.xlsx")
            print("Judul CD telah dihapus!")
            menu_admin()
        else:
            removecd()
    elif genre == 2:
        filedata = "database.xlsx"
        database= pd.read_excel(filedata,sheet_name="Genre 2")
        file = openpyxl.load_workbook("database.xlsx")
        sheet = file['Genre 2']

        print(database)

        deletedata = int(input("Pilih film yang ingin anda hapus (1/2/3/...): "))
        data = database.loc[deletedata,'Judul CD']
        print("Apa anda yakin ingin menghapus ", data ,"?")
        validasi_delete = str(input( "Y/N :"))
        if validasi_delete == "Y":
            real_delete_data = deletedata + 2
            sheet.delete_rows(idx=real_delete_data)
            file.save("database.xlsx")
            print("Judul CD telah dihapus!")
            menu_admin()
        else:
            removecd()
    elif genre == 3:
        filedata = "database.xlsx"
        database= pd.read_excel(filedata,sheet_name="Genre 3")
        file = openpyxl.load_workbook("database.xlsx")
        sheet = file['Genre 3']

        print(database)

        deletedata = int(input("Pilih film yang ingin anda hapus (1/2/3/...): "))
        data = database.loc[deletedata,'Judul CD']
        print("Apa anda yakin ingin menghapus ", data ,"?")
        validasi_delete = str(input( "Y/N :"))
        if validasi_delete == "Y":
            real_delete_data = deletedata + 2
            sheet.delete_rows(idx=real_delete_data)
            file.save("database.xlsx")
            print("Judul CD telah dihapus!")
            menu_admin()
        else:
            removecd()
    else:
        filedata = "database.xlsx"
        database= pd.read_excel(filedata,sheet_name="Genre 4")
        file = openpyxl.load_workbook("database.xlsx")
        sheet = file['Genre 4']

        print(database)

        deletedata = int(input("Pilih film yang ingin anda hapus (1/2/3/...): "))
        data = database.loc[deletedata,'Judul CD']
        print("Apa anda yakin ingin menghapus ", data, "?")
        validasi_delete = str(input( "Y/N :"))
        if validasi_delete == "Y":
            real_delete_data = deletedata + 2
            sheet.delete_rows(idx=real_delete_data)
            file.save("database.xlsx")
            print("Judul CD telah dihapus!")
            menu_admin()
        else:
            removecd()

def progam():
    global cmu
    global el
    menu_utama()
    if cmu == 1 :
        cek_login_member()
    else:
        login_admin()
        

progam()