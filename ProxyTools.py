import requests, os, colorama, sys, time
from colorama import Fore
from threading import Thread

esp = " " * 50

def banner(args1,args2,args3):
    print(Fore.MAGENTA+f'''
                          .-'-.
                        /`     |__
                      /`  _.--`-,-`    `     ╔═══╗                    ╔════╗        ╔╗     
                      '-|`   a '<-.    `     ║╔═╗║                    ║╔╗╔╗║        ║║     
                        \     _\__) \=`      ║╚═╝║╔═╗╔══╗╔╗╔╗╔╗ ╔╗    ╚╝║║╚╝╔══╗╔══╗║║ ╔══╗
                         C_  `    ,_/        ║╔══╝║╔╝║╔╗║╚╬╬╝║║ ║║      ║║  ║╔╗║║╔╗║║║ ║══╣
                           | ;----'          ║║   ║║ ║╚╝║╔╬╬╗║╚═╝║     ╔╝╚╗ ║╚╝║║╚╝║║╚╗╠══║
                      _.---| |--._           ╚╝   ╚╝ ╚══╝╚╝╚╝╚═╗╔╝     ╚══╝ ╚══╝╚══╝╚═╝╚══╝
                    .'  _./' '\._ '.                         ╔═╝║  
                   /--'`  `-.-`  `'-\\                        ╚══╝  
                  |         o        \\                               [{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} - {args1}{Fore.MAGENTA}
                  |__ .             / )    -.   .-.                  [{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} - {args2}{Fore.MAGENTA}
                 (___)|     o     \/ /     `.`-' .'                  [{Fore.RESET}3{Fore.MAGENTA}]{Fore.RESET} - {args3}{Fore.MAGENTA}
                  | | |           |-'\      ' .-'
                 /  |_.-\"""-.-'=_ |   '--.'  ,'
                <   `  =-->    _= /        __/
                 '._     _.-"-.= /`"-...-"` 
                    `;\"""`     __/



'''+Fore.RESET)

valid = 0
invalid = 0

def RFile(file,method):
    with open(file,method) as file:
        a = [line.strip('\n') for line in file]
        return a

def ProxyChecker(prx, site):
    global valid
    global invalid

    proxy = {'http': 'http://'+prx, 'https': 'http://'+prx}
    try:
        r = requests.get(site, proxies=proxy,timeout=500)

        print(Fore.GREEN+prx+Fore.RESET+"\t\t- Valid".replace("Valid",Fore.GREEN+"Valid"+Fore.RESET))
        valid += 1

        with open("good_proxy.txt","a") as f:
            f.write(prx+"\n")
    
    except:
        invalid += 1

def proxycheck():
    input_file = input(Fore.MAGENTA+f"\n\n[{Fore.RESET}?{Fore.MAGENTA}] - Proxy file (default: proxies.txt): "+Fore.RESET)

    if input_file == "":
        input_file = "proxies.txt"

    site = input(Fore.MAGENTA+f"[{Fore.RESET}?{Fore.MAGENTA}] - Website (default: https://google.com): "+Fore.RESET)

    if site == "":
        site = "https://google.com/"

    proxy_list = RFile(input_file,'r')

    for proxy in proxy_list:
        a = True
        while a:
            Thread(target=ProxyChecker,args=(proxy, site)).start()
            a = False
        


def scrap_http():
    output = input(Fore.MAGENTA+f"\n\n[{Fore.RESET}?{Fore.MAGENTA}] - Output file (default: proxies.txt): "+Fore.RESET)

    if output == "":
        output = "proxies.txt"

    with open(output, 'w+') as f:
            f.write("")

    try:      
        r = requests.get("https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json")
        data = r.json()

        fst = data['proxies']
        lines = 0
        for p in fst:
            ip = p['ip']
            port = p['port']
            proxies = ip+":"+port

            with open(output, 'a+') as f:
                lines += 1
                f.write(proxies+"\n")

        print(Fore.MAGENTA+f"\n\n[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        text = r.text.replace('\n','')

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:      
        r = requests.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json")
        data = r.json()

        fst = data['proxynova']
        lines = 0
        for p in fst:
            ip = p['ip']
            port = p['port']
            proxies = ip+":"+port

            with open(output, 'a+') as f:
                lines += 1
                f.write(proxies+"\n")

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    except:
         print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

    try:
        r = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt")
        text = r.text

        with open(output, 'a+') as f:
            f.write(text)

        lines = 0
        with open(output, 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        print(Fore.MAGENTA+f"[{Fore.RESET}+{Fore.MAGENTA}] - Successfuly scraped and saved {lines} proxys !"+Fore.RESET)
    
    except:
        print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

def Main():
    global esp
    os.system('mode con cols=119 lines=33')
    os.system('cls')
    os.system('title Proxy Tools Made By Github.com/KanekiX2')
    banner(args1="Proxy Scraper", args2="Proxy Checker", args3="Exit")
    while True:
        c = input(esp+Fore.MAGENTA+"> "+Fore.RESET)

        if c.lower() == "clear" or c.lower() == "cls":
            Main()

        elif c == "1":
            scrap_http()

        elif c == "2":
            proxycheck()

        elif c == "3":
            sys.exit()


Main()