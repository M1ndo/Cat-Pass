import os,sys
from colors1 import get_colors
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from colorama import Fore
from domain import create_dir
from time import sleep as sl
from banner import banner
class Pass_key():
    def get_filename():
        filename = input(Fore.CYAN + "[+] Enter Filename: ") 
        key_file = filename+'.key'
        return filename,key_file
    def gen_key(path, key_file):
        key = Fernet.generate_key()
        if key_file.endswith(".key"):
            key_file = key_file
        else:
            key_file = key_file+".key"    
        with open((path+key_file), 'wb') as key_file2:
            key_file2.write(key)     
    def get_path():
        user_input = input(Fore.LIGHTBLUE_EX +
            "[+] Do you wanna use a custom path or a default one [c/d]: ")
        if user_input in ['c', 'C']:
            path = input(Fore.MAGENTA + "[+] Enter Path: ")
            isdir = os.path.isdir(path)
            if isdir == True:
                pass
            else:
                print(Fore.RED + "[!] That's Not a directory")
        elif user_input in ['d', 'D']:
            path = os.getcwd()
        # print(path)
        else:
            print(get_colors.red() + "[!] Unknown Choice!")
            Pass_key.get_path()
        return path   
    def encrypt(filename, key):
        key = open(key, 'rb').read()
        f = Fernet(key)
        data = open(filename, 'rb').read()
        encrypted = f.encrypt(data)
        break_line = b'\n'
        with open((filename+".enc"), 'wb') as writed:
            writed.write(encrypted + break_line)
    def save_creds(path, filename, username, password):
        if path[:4] != "/":
            path = path+"/"
        with open((path+filename), 'w') as saved:
            saved.write("[+] Username|Email: " + username +
                        "\n" + "[+] Password: " + password + "\n")
    def save_app(path, filename, username, password):
        if path[:4] != "/":
            path = path+"/"
        with open((path+filename), 'a') as saved:
            saved.write("\n[+] Username|Email: " + username +
                        "\n" + "[+] Password: " + password + "\n")                    
    def encrypt_file(path, file):
        try:
            if path.endswith("/"):
                path = path
            else:
                path = path+"/"
            filename = file #os.path.basename(file)
            # print(filename)
            file = open(file, 'rb').read()
            path2 = path+".keys"
            # path3 = path2+"/"
            Pass_key.gen_key(path, filename)
            create_dir(path2, path, (filename+".key"))
            os.system('clear')
            sl(5)
            print(Fore.YELLOW + "[+] Generated Key-File " + Fore.WHITE + Fore.GREEN + f"{filename}" + Fore.WHITE + " In " + Fore.RED + f"{path2}"+Fore.WHITE)
            key = open((path2+"/"+filename+".key"), 'rb').read()
            # print(key)
            key = Fernet(key)
            enc = key.encrypt(file)
            print(Fore.GREEN + "[+] Encrypting "+ Fore.LIGHTMAGENTA_EX + f"[{filename}] ..." + Fore.WHITE)
            sl(5)
            # print(enc)
            with open((filename+".enc"), 'wb') as saved:
                saved.write(enc)
                saved.close()
            print(Fore.RED + "Data Saved In " + Fore.WHITE + f"[{filename}.enc]")
            os.remove((path+filename))                    
        except FileNotFoundError:
            print(get_colors.red() + "[+] File " + get_colors.white() + f"{filename}" + get_colors.red() + " Not Found !")
            sl(3)
            os.system('clear')
            Pass_key.run()
    def get_creds():
        username = input(Fore.YELLOW + "[+] Enter username|email: ")
        password = input(Fore.LIGHTGREEN_EX + "[+] Enter password: ")
        path = Pass_key.get_path()
        if path.endswith('/') == True:
            path = path
        else:
            path = path+"/"    
        # check_path = check_path+"/"
        # check_path = os.getcwd()
        filename, key_file = Pass_key.get_filename()
        Pass_key.save_creds(path, filename, username, password)
        option = input(get_colors.randomize2() + '[+] Do you want to encrypt data [Y/N]: ')
        if option in ['y', 'Y']:
            print(Fore.GREEN + "[+] Encrypting "+ Fore.LIGHTMAGENTA_EX + f"[{filename}] ..." + Fore.WHITE)
            sl(5)
            Pass_key.gen_key(path, key_file)
            path2 = path+".keys"
            path3 = path2+"/"
            # print(path + "\n" + path2 + "\n" + path3)
            key_file2 = path3+key_file
            create_dir(path2, path, key_file)
            Pass_key.encrypt((path+filename), key_file2)
            os.remove((path+filename))
            os.system('clear')
            sl(1)
            print(get_colors.pink() + "[+] File "+ get_colors.yellow() + f"{filename}" + get_colors.pink() + " Encrypted View With " + get_colors.sharp_orange()+ "[View Method]")
            sl(3)
            os.system('clear')
            Pass_key.run()
        elif option in ['N', 'n']:
            print(get_colors.white()  + "[+] Created File "+get_colors.randomize2()+f"[ {filename} ]" + get_colors.white() + " Encrypt "+get_colors.randomize()+f"[ {filename} ]"+get_colors.white() + " With " + get_colors.red() + "[Encrypt File Method]" + get_colors.white())
            sl(5)
            Pass_key.run()
        else:
            print(Fore.RED + '[!] Unknown Option')
            os.remove((path+filename))
            Pass_key.get_creds()    
    def creds_append():
        files = input(Fore.GREEN + "[+] Enter data filename: ")
        if files.endswith(".enc"):
            files = files
        else:
            files=files+".enc"
        key_files = os.path.splitext(files)[0] 
        # print(key_files)       
        username = input(Fore.LIGHTBLUE_EX + "[+] Enter username|email: ")
        password = input(Fore.LIGHTYELLOW_EX + "[+] Enter password: ")
        path = os.getcwd()+"/"
        if os.path.isfile((path+files)):
            # print("File was Found.")
            key_path = path+".keys/"
            key_file = key_path+key_files+".key"
            # print(key_file)
            if os.path.isfile(key_file):
                # print("Key File was Found")
                pass
            else:
                # print("Key File was not found")
                exit(1)
            key_data = open(key_file, 'rb').read()
            # print(key_data)
            key = Fernet(key_data)
            data = open(files, 'rb').read()
            dec = key.decrypt(data)
            # print(dec)
            with open(key_files, 'wb') as new_file:
                new_file.write(dec)
                new_file.close()
            print(get_colors.white() + "[+] Adding { Username: "+get_colors.red()+f"{username}"+ get_colors.white() + " Password:"+ get_colors.red() +f" {password}"+get_colors.white()+" } To "+get_colors.pink()+f"{key_files}")    
            sl(3)
            Pass_key.save_app(path, key_files, username, password) 
            print(get_colors.white() + get_colors.sharp_green() + "[+] Encrypting "+get_colors.sharp_orange()+f"{key_files}")
            sl(5)
            Pass_key.encrypt(key_files, key_file)
            # print("Encrypted")
            # print(f"removing {key_files}")
            os.remove(key_files)
            # print(os.listdir(path))
            print(Fore.CYAN + "[+] Username: "+ get_colors.red() + f"[{username}] " + get_colors.cyan()+ "Password: " + get_colors.red() + f"[{password}] " + get_colors.cyan() + "Saved In: " + get_colors.red() + f"{key_files}")
        else:
            print(get_colors.yellow() + '[!] File Was not found')
            # print(key_files) 
            choose = input(Fore.GREEN + "[+] Wanna Continue? [Y/N]: ")
            if choose in ['y','Y']:
                print(get_colors.white() + "[+] Creating A New File " + get_colors.green() + f"{key_files}" + get_colors.white() + " With The Following Data\n[+] Username||Email: " + get_colors.randomize2() + f"{username}" + get_colors.white() + " Password: " + get_colors.randomize2() + f"{password}") 
                sl(2)
                Pass_key.save_creds(path, key_files, username, password)
                print(Fore.GREEN + "[+] Encrypt "+ Fore.LIGHTMAGENTA_EX + f"[{key_files}] " + Fore.WHITE + "With "+get_colors.randomize2()+"[Encrypt Method]")
                sl(5)
                Pass_key.run()
            elif choose in ['n','N']:
                print(Fore.RED + "[!] Return ...")
                # exit(1)
                sl(2)
                Pass_key.run()
            else:
                print(Fore.RED + "[!] Unknown Choice!\n[+] returning!")
                sl(2)
                Pass_key.run()                   
    def decrypt():
        try:
            iview = input(Fore.CYAN + "[+] Enter Filename: ")
            if iview.endswith(".enc") == True:
                iview = iview
            else:
                iview = iview+".enc" 
            niview = iview       
            check_file = os.path.isfile(iview)
            if check_file == True:
                iview = open(iview, 'rb').read()
            else:
                path = Pass_key.get_path()
                if path.endswith("/") == True:
                    path = path
                else:
                    path = path+"/"
                basename = os.path.basename(iview)
                if os.path.isfile((path+basename)) == True:
                    iview = path+basename
                    iview = open(iview, 'rb').read()
                else:
                    print(Fore.RED +"[+] File Not Found "+get_colors.bright_megento()+"\n[+] Only '.enc' Encrypted Files Accepted")
                    exit(1)                                 
            ikey = input(Fore.YELLOW + "[+] Enter Key filename: ")
            if ikey.endswith(".key") == True:
                ikey = ikey
            else:
                ikey = ikey+".key"    
            nikey = ikey    
            check = os.path.isfile(ikey)
            if check == True:
                key_ex = open(ikey, 'rb').read()
                dec = Fernet(key_ex)
            else:
                path = Pass_key.get_path()
                if path.endswith('/') == True:
                    path = path
                else:
                    path = path+"/"
                path2 =path+".keys"
                if path2.endswith("/"):
                    path2 = path2
                else:
                    path2 = path2+"/"
                ikey = os.path.basename(ikey)    
                ikey = path2+ikey
                if ikey.endswith(".key"):
                    ikey = ikey
                else:
                    ikey = ikey+".key"
                if os.path.isfile(ikey):
                    key_ex = open(ikey, 'rb').read()
                    dec = Fernet(key_ex)
                else:                
                    print(Fore.RED+ "[!] Key-File Not Found"+get_colors.sharp_green()+"\n[+] Check Your Key File")
                    exit(1)
            print(Fore.WHITE+f"[+] Decrypting {iview} ...")
            sl(10)    
            data_user = dec.decrypt(iview)           
            data_user = bytes.decode(data_user)
            print("\n" + data_user)
        except InvalidToken:
            print(get_colors.yellow() +"[!] An Exceptions Occured "+ get_colors.orange() + f"\n[+] {niview}" + get_colors.yellow() + " Was Corrupted ! Or" + get_colors.sharp_megento() + f" [{nikey}]" + get_colors.yellow() + " Is Not The Correct Key !")
    def run():
        banner()
        user_option = input(Fore.CYAN + "[+] Do you want to "+Fore.LIGHTGREEN_EX +" [view] "+Fore.CYAN+"or"+Fore.LIGHTMAGENTA_EX+" [add data] "+Fore.CYAN+"or"+Fore.LIGHTYELLOW_EX+" [encrypt a data file] "+Fore.CYAN+"[V/A/E]: ")
        if user_option in ["A",'a']:
            def input1():
                input2 = input(Fore.RED + 
                    "[+] Do you want to create a "+ get_colors.sharp_green() +"new database"+ get_colors.bright_megento() +" or"+ get_colors.orange() +" use previous one"+ get_colors.yellow() + get_colors.white() +" [N/O]: ")
                if input2 in ['n','N']:
                    Pass_key.get_creds()
                    sl(5)
                    os.system('clear')
                elif input2 in ['O','o']:
                    Pass_key.creds_append()
                else:
                    print(Fore.RED+"[!] Unknown Options")
                    input1()
            input1()
        elif user_option in ['V','v']:
            Pass_key.decrypt() 
            sl(2)   
        elif user_option in ['E','e']:
            filename = Pass_key.get_filename()[0]
            path = Pass_key.get_path()
            Pass_key.encrypt_file(path, filename)
        else:
            print(Fore.RED  +"[!] Unknown Option")
            Pass_key.run()