from colorama import init
from os import system
from time import sleep 
from files.Writer import writer

init()

def whatsapp():
    writer("\033[32;1mOpening Whatsapp...")
    url = "https://chat.whatsapp.com/Ha3goS71RamKMeCq2CJLwe"
    sleep(3)
    system(f"termux-open {url}")

def instagram():
    writer("\033[35;1mOpening Instagram...")
    url_insta = "https://www.instagram.com/hackers_colony_official?igsh=Ym42ZnVnY3JjbHp0"
    sleep(3)
    system(f"termux-open {url_insta}")

def youtube():
    writer("\033[31;1mOpening YouTube...")
    url_yt = "https://youtube.com/@hackers_colony_tech?si=Dy6hDgWH5rnONP9a"
    sleep(3)
    system(f"termux-open {url_yt}")


if __name__ == "__main__":
    youtube()
    instagram()
    whatsapp()
    
