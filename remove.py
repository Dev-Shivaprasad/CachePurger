import os
import time
import shutil as rm
from platform import system
import os.path as opt
# /----------------------------------------------------------------------------


def PrintName(text: str):
    print("\n" + "\033[34m-"*10 + text + "-"*10 + "\033[0m" + "\n")


def PrintException(e: Exception):
    print(f"\033[31mcannot delete : \033[0m \n\t {e}\n")


def PrintSuccess(Path: str):
    print(f"\033[32mdeleted : \033[0m \t \033[33m{Path}\033[0m \n")


def PrintFooter(name: str, sleeptimer: int):
    print("\033[35m-"*50)
    print("\t" + f"App Created By : \033[32m{name.title()}\033[0m")
    print("\033[35m-"*50)
    print(f"window will close in {sleeptimer} seconds \033[0m")
    time.sleep(sleeptimer)


# /----------------------------------------------------------------------------

# R"C:\Users\user_pc_name~1\AppData\Local\Temp"
path_Temp = opt.expanduser("~\AppData\Local\Temp")
path_Temp1 = r"C:\Windows\Temp"
path_Prefetch = r"C:\Windows\Prefetch"

# /----------------------------------------------------------------------------


def FlushDNS():
    os.system("ipconfig /flushdns")
    print("-"*50)

# /----------------------------------------------------------------------------


def Delete_Temp():
    TempPath = os.listdir(path_Temp)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Temp} (%temp%)")
    for files in TempPath:

        try:
            fpath = os.path.join(path_Temp, files)
            if os.path.isdir(fpath):
                rm.rmtree(fpath)
                PrintSuccess(fpath)
            else:
                os.remove(fpath)
                PrintSuccess(fpath)

        except Exception as e:
            PrintException(e)

# /----------------------------------------------------------------------------


def Delete_Temp2():
    TempPath2 = os.listdir(path_Temp1)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Temp1} (temp)")
    for files2 in TempPath2:

        try:
            fpath2 = os.path.join(path_Temp1, files2)
            if os.path.isdir(fpath2):
                rm.rmtree(fpath2)
                PrintSuccess(fpath2)
            else:
                os.remove(fpath2)
                PrintSuccess(fpath2)
        except Exception as e:
            PrintException(e)


# /----------------------------------------------------------------------------


def Delete_Prefetch():
    Prefetch = os.listdir(path_Prefetch)
    PrintName(f"DELETING TEMPROARY FILES FROM {path_Prefetch} (prefetch)")
    for files3 in Prefetch:

        try:
            fpath3 = os.path.join(path_Prefetch, files3)
            if os.path.isdir(fpath3):
                rm.rmtree(fpath3)
                PrintSuccess(fpath3)
            else:
                os.remove(fpath3)
                PrintSuccess(fpath3)
        except Exception as e:
            PrintException(e)


# /----------------------------------------------------------------------------


if __name__ == "__main__":

    if system() == "Windows":
        FlushDNS()
        Delete_Prefetch()
        Delete_Temp()
        Delete_Temp2()
        PrintFooter("shivaprasad. m. g", 30)
    else:
        print("\033[31mNOT RUNNING WINDOWS\033[0m")
