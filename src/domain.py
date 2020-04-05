import os
import sys,shutil

# choice = input("input: ")
# choice2 =  "/home/ybenel/Projects/Projects17/" #input("input: ")
# choice3 = input("input: ")
def create_dir(path, path1, filename):
    try:
        dirname = os.path.dirname(path)
        dirname2 = dirname+"/"
        # print(dirname)
        if os.path.isdir(dirname) == True:
            if os.path.isdir(path) == True:
                if os.path.isfile((path+"/"+filename)) == True:
                    print(f"[+] Directory {path} and filename {filename} Exists\n")
                    choice = input("[+] Consider Removing it: ")
                    if choice in ['y','Y']:
                        os.remove((path+"/"+filename))
                        print(f"File Removed {filename} \n")
                        # print(os.listdir(path))
                    elif choice in ['n','N']:
                        print("[!] Not Removing ... \n Quiting...\n")
                        return
                    else:
                        print("[!] Unknown Options")
                        return
                    print("[+] Moving Files From Home")
                    # path1 =  os.getcwd()+"/"
                    shutil.move((path1+filename), path)
                    # dirlist = os.listdir(path)
                    # print(f"[+] Listing Files in {path} \n{dirlist} ")           
                else:
                    print(f"[+] Directory {path} Exists But Filename {filename} Does Not \n")
                    # path1 = os.getcwd()+"/"
                    print(f"[+] Moving Files From Home Directory {path1} to {path}")
                    # print((path1+filename))
                    shutil.move((path1+filename), path)
                    # dirlist = os.listdir(path)
                    # print(f"[+] Listing Files in {path} \n{dirlist}")
            else:
                if os.path.isfile((dirname2+filename)) == True:
                    print(f"[+] filename Exists Inside {dirname2} \n")
                    # print(f"[!] Removing {filename} Inside {dirname2} \n")
                    # os.remove((dirname2+filename))
                    name = os.path.basename(path)
                    print(f"[+] Creating folder {name} inside of {dirname2}\n")
                    os.mkdir(path)
                    # path1 = os.getcwd()+"/"
                    print(f"[+] Moving File {filename} From Home Directory {path1} To {path} \n")
                    shutil.move((path1+filename), path)
                    # dirlist = os.listdir(path)
                    # print(f"[+] Listing Files in {path} \n{dirlist}")
                else:
                    print(f"[+] filename {filename} does not exists inside {dirname2} \n")
                    name = os.path.basename(path)
                    print(f"[+] Creating folder {name} inside of {dirname2}\n")
                    os.mkdir(path)
                    # path1 = os.getcwd()+"/"
                    print(f"[+] Moving File {filename} From Home Directory {path1} To {path} \n")
                    shutil.move((path1+filename), path)
                    # dirlist = os.listdir(path)
                    # print(f"[+] Listing Files in {path} \n{dirlist}")        
        else:
            print("Main Directory Does Not Exists")    
    except(KeyboardInterrupt,OSError,PermissionError):
        print("Error Occured")

