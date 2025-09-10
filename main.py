import os
import time
import shutil as rm
from platform import system

import os.path as opt
# /----------------------------------------------------------------------------


def PrintName(text: str):
    print("\n" + "\033[34m-" * 10 + text + "-" * 10 + "\033[0m" + "\n")


def PrintException(e: Exception):
    print(f"\033[31mcannot delete : \033[0m \n\t {e}\n")


def PrintSuccess(Path: str):
    print(f"\033[32mdeleted : \033[0m \t \033[33m{Path}\033[0m \n")


def PrintFooter(name: str, sleeptimer: int):
    print("\033[35m-" * 50)
    print("\t" + f"App Created By : \033[32m{name.title()}\033[0m")
    print("\033[35m-" * 50)
    print(f"window will close in {sleeptimer} seconds \033[0m")
    time.sleep(sleeptimer)


# /----------------------------------------------------------------------------

# R"C:\Users\user_pc_name~1\AppData\Local\Temp"
# path_Temp = opt.expanduser(r"~\AppData\Local\Temp")
# path_Temp1 = r"C:\Windows\Temp"
# path_Prefetch = r"C:\Windows\Prefetch"
# path_SoftwareDistribution = r"C:\Windows\SoftwareDistribution\Download"

paths: list[dict[str, str]] = [
    {
        "path": opt.expanduser(r"~\AppData\Local\Temp"),
        "message": "DELETING TEMPROARY FILES FROM (%temp%) : ",
    },
    {
        "path": r"C:\Windows\Temp",
        "message": "DELETING TEMPROARY FILES FROM (temp) : ",
    },
    {
        "path": r"C:\Windows\Prefetch",
        "message": "DELETING TEMPROARY FILES FROM (prefetch) : ",
    },
    {
        "path": r"C:\Windows\SoftwareDistribution\Download",
        "message": "DELETING TEMPROARY FILES FROM (SoftwareDistribution) : ",
    },
]

# /----------------------------------------------------------------------------


def FlushDNS():
    os.system("ipconfig /flushdns")
    print("-" * 50)


# /----------------------------------------------------------------------------


def Delete_Temp_files(path: str, message: str):
    TempPaths = os.listdir(path)
    PrintName(f"{message}{path}")
    if len(TempPaths) <= 0:
        PrintName("Nothing to clear")
    for tempfilename in TempPaths:
        try:
            joinedpath = os.path.join(path, tempfilename)
            if os.path.isdir(joinedpath):
                rm.rmtree(joinedpath)
                PrintSuccess(joinedpath)
            else:
                os.remove(joinedpath)
                PrintSuccess(joinedpath)

        except Exception as e:
            PrintException(e)

    print("-" * 150)


# /----------------------------------------------------------------------------


if __name__ == "__main__":
    if system() == "Windows":
        FlushDNS()
        for data in paths:
            Delete_Temp_files(path=data["path"], message=data["message"])
        PrintFooter("shivaprasad. m. g", 30)
    else:
        print("\033[31mNOT RUNNING WINDOWS OS\033[0m")
