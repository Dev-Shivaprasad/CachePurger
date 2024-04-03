import os
import time
import shutil as rm
import os.path as opt

# /----------------------------------------------------------------------------


def iife(fx):
    def exe():
        fx()
    return exe()


def PrintName(text: str):
    print("\n" + "-"*10 + text + "-"*10 + "\n")

# /----------------------------------------------------------------------------


# R"C:\Users\user_pc_name~1\AppData\Local\Temp"
path_Temp = opt.expanduser("~\AppData\Local\Temp")
path_Temp1 = R"C:\Windows\Temp"
path_Prefetch = R"C:\Windows\Prefetch"

# /----------------------------------------------------------------------------


@iife
def FlushDNS():
    os.system("ipconfig /flushdns")
    print("-"*50)

# /----------------------------------------------------------------------------


@iife
def Delete_Temp():
    TempPath = os.listdir(path_Temp)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Temp} (%temp%)")
    for files in TempPath:

        try:
            fpath = os.path.join(path_Temp, files)
            rm.rmtree(fpath)
            print(f"deleted {files} \n")
        except Exception as e:
            print(f"cannot delete {files} because of {e} \n")

        try:
            os.remove(fpath)
        except Exception as e:
            pass
# /----------------------------------------------------------------------------


@iife
def Delete_Temp2():
    TempPath2 = os.listdir(path_Temp1)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Temp1} (temp)")
    for files2 in TempPath2:

        try:
            fpath2 = os.path.join(path_Temp1, files2)
            os.remove(fpath2)
            print(f"deleted {files2} \n")
        except Exception as e:
            print(f"cannot delete {files2} because of {e} \n")

# /----------------------------------------------------------------------------


@iife
def Delete_Prefetch():
    Prefetch = os.listdir(path_Prefetch)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Prefetch} (prefetch)")
    for files3 in Prefetch:

        try:
            fpath3 = os.path.join(path_Prefetch, files3)
            os.remove(fpath3)
            print(f"deleted {files3} \n")
        except Exception as e:
            print(f"cannot delete {files3} because of {e} \n")

# /----------------------------------------------------------------------------


t = "SHIVA PRASAD GAIKWAD"
print("-"*50)
print("\t" + f"App Created By : {t}")
print("-"*50)
print("window will close in 30 seconds")
time.sleep(30)
