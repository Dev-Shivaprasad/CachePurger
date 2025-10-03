import ctypes
import os
import subprocess
import time
import shutil as rm
from platform import system
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import random
import re

# /----------------------------------------------------------------------------
console = Console(record=True)
console.clear()


# /----------------------------------------------------------------------------
def CustomProgressbar(message: str, Time: int):
    with Progress() as progress:
        # Add a new task with a total of 30 steps
        task = progress.add_task(f"[cyan]{message}[/cyan]", total=Time)

        # Loop for the total number of seconds
        while not progress.finished:
            # Update the progress bar, advancing it by one step
            progress.update(task, advance=1)
            # Pause for one second to time the progress
            time.sleep(1)


def PrintName(text: str):
    console.print(("\n[bold yellow]" + "- " * 5 + text + " -" * 5 + "[/bold yellow]\n"))


def PrintException(e: Exception):
    console.print(
        (f"[bold bright_red]cannot delete : [/bold bright_red] \n\t [red] {e}\n")
    )


def PrintSuccess(Path: str):
    console.print(
        (f"[bright_green]deleted : [bright_green] \t [green]{Path}[green] \n")
    )


def printseprator(size: int = 25):
    console.print(("[bold yellow]- " * size))


def PrintFooter(name: str, sleeptimer: int):
    console.print("[orange1]- " * 25)
    console.print(
        "\t" + f"[orange1]App Created By : [bright_yellow]{name.title()}[bright_yellow]"
    )
    console.print("[orange1]- " * 25)
    CustomProgressbar(
        message=f"window will close in {sleeptimer} seconds", Time=sleeptimer
    )


def focus_terminal():
    # Get the handle of the console window
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        # Restore and bring to front
        ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
        ctypes.windll.user32.SetForegroundWindow(hwnd)


# /----------------------------------------------------------------------------

# R"C:\Users\user_pc_name~1\AppData\Local\Temp"
# path_Temp = os.path.expanduser(r"~\AppData\Local\Temp")
# path_Temp1 = r"C:\Windows\Temp"
# path_Prefetch = r"C:\Windows\Prefetch"
# path_SoftwareDistribution = r"C:\Windows\SoftwareDistribution\Download"
# path_ChromeCache = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data")


paths: list[dict[str, str]] = [
    {
        "path": os.path.expanduser(r"~\AppData\Local\Temp"),
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

ChromiumProfilePattern = r"^Profile\s\d+$"
FragilePaths: list[dict[str, str]] = [
    {
        "path": os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data"),
        "message": "DELETING Cache FROM (ChromeCache) : ",
    },
    {
        "path": os.path.expanduser(
            r"~\AppData\Local\BraveSoftware\Brave-Browser\User Data"
        ),
        "message": "DELETING Cache FROM (BravesCache) : ",
    },
]

# /----------------------------------------------------------------------------


def FlushDNS():
    subprocess.run(
        "ipconfig /flushdns",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    console.print("[bold indian_red1] Successfully flushed the DNS Resolver Cache.")
    printseprator()


def FindSpecficFolderByREGEX(RegexPattern: str, Path: str) -> list[str] | None:
    if os.path.exists(Path):
        pattern = re.compile(RegexPattern)
        folderpath = os.listdir(Path)
        ListOfFoldersWithSameREGEXPattern = []
        for foldername in folderpath:
            if pattern.match(foldername):
                ListOfFoldersWithSameREGEXPattern.append(foldername)
        return ListOfFoldersWithSameREGEXPattern
    else:
        console.print()


def DeleteBrowserCache(Path: str, message: str):
    if os.path.exists(path=Path):
        FoldersToDelete = [
            "Cache",
            "Code Cache",
            "DawnGraphiteCache",
            "DawnWebGPUCache",
            "GPUCache",
        ]
        Listofprofiles = FindSpecficFolderByREGEX(ChromiumProfilePattern, Path) or []
        Listofprofiles.append("Default")
        for profilefoldername in Listofprofiles:
            for foldersname in FoldersToDelete:
                Delete_Temp_files(
                    os.path.join(Path, profilefoldername, foldersname), message
                )


def Delete_Temp_files(path: str, message: str):
    if os.path.exists(path):
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


# /----------------------------------------------------------------------------
if __name__ == "__main__":
    if system() == "Windows":
        FlushDNS()
        for data in paths:
            Delete_Temp_files(path=data["path"], message=data["message"])
        focus_terminal()
        op = Prompt.ask(
            case_sensitive=False,
            choices=["Y", "N"],
            default="Y",
            prompt="[bold yellow]Clear Browser CACHE ? \n if yes CLOSE all BROWSERS",
        )
        if op == "Y":
            for data in FragilePaths:
                DeleteBrowserCache(data["path"], data["message"])

        with open("CachePurgerLog.txt", "+w") as file:
            file.write("".join(console.export_text()))

        console.print(
            f"[bold underline italic red] Logs have Been Genereted [/] {(random.choice(['😛', '🤧', '😝']))}"
        )
        PrintFooter("shivaprasad. m. g", 10)
    else:
        console.print("[bold red]NOT RUNNING WINDOWS OS")
