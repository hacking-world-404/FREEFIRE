from os import system as c
import time
import random

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'

def logo():
    c("clear")
    print(f"""{G}
██████╗ ██╗███████╗███████╗██╗
██╔══██╗██║██╔════╝██╔════╝██║
██████╔╝██║███████╗█████╗  ██║
██╔═══╝ ██║╚════██║██╔══╝  ██║
██║     ██║███████║███████╗███████╗
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝
{Y}  HACKING WORLD - DIAMOND  VIP TOOL
{A}--------------------------------------------------
""")

def progress(task):
    for i in range(1, 21):
        print(f"{C}[{G}{'=' * i}{' ' * (20 - i)}] {i*5}% {Y}{task}", end='\r')
        time.sleep(0.2)
    print()

def diamond_hack():
    logo()
    cookie = input(f"{C}ENTER YOUR FREE FIRE COOKIE: ")
    uid = input(f"{C}ENTER YOUR FREE FIRE UID: ")
    print(f"{Y}[+] Connecting to Garena Server...")
    time.sleep(2)
    progress("Verifying Cookie")
    print(f"{G}[✓] Cookie Verified!")
    time.sleep(1)
    print(f"{Y}[+] Checking Device Root Permission...")
    time.sleep(2)
    print(f"{G}[X] Root Permission On! Limited Access Mode...\n")
    time.sleep(1)
    print(f"{Y}[+] Injecting 9999 Diamonds to UID: {uid}")
    progress("Transferring Diamonds")
    print(f"{G}\n[✓] 9999 Diamonds Successfully Sent To UID: {uid}")
    print(f"{Y}Note: It may take 8 minit to reflect in your account.\n")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Start Diamond topup ")
    print(f"{A}[0] Exit Tool")
    print(f"{A}--------------------------------------------------")
    choice = input(f"{Y}[?] Select Option: ")
    if choice == '1':
        diamond_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()