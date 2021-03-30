import requests, os, colorama, sys, time, re, json, bs4
from colorama import Fore
from threading import Thread
from bs4 import BeautifulSoup

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

def RFile(file,method):
    with open(file,method) as file:
        a = [line.strip('\n') for line in file]
        return a

def ProxyChecker(prx, site):

    proxy = {'http': 'http://'+prx, 'https': 'http://'+prx}
    try:
        r = requests.get(site, proxies=proxy,timeout=1)

        print(Fore.GREEN+prx+Fore.RESET+f"\t\t- Valid".replace("Valid",Fore.GREEN+"Valid"+Fore.RESET))

        with open("good_proxy.txt","a") as f:
            f.write(prx+"\n")
    
    except:
    	print(Fore.RED+prx+Fore.RESET+f"\t\t- Invalid".replace("Invalid",Fore.RED+"Invalid"+Fore.RESET))

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

	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
	    text = r.text.replace('\n','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
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

	    
	except:
	     print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
		r = requests.get("https://www.sslproxies.org/")
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
		lines = 0

		for match in matches:
			proxy = (match[0]+":"+match[1])

			with open(output, 'a+') as f:
				f.write(proxy+"\n")
				lines += 1

		pass

		
	
	except:
		pass

	try:
		r = requests.get("https://free-proxy-list.net/")
		html = r.text
		matches = re.findall(r"(\d+?\.\d+?\.\d+?\.\d+).*?(\d{1,5}).*?(no)", html)
		lines = 0

		for match in matches:
			proxy = (match[0]+":"+match[1])

			with open(output, 'a+') as f:
				f.write(proxy+"\n")
				lines += 1

		

	except:
		pass

	try:
	    r = requests.get("http://rootjazz.com/proxies/proxies.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("http://ab57.ru/downloads/proxylist.txt")
	    text = r.text.replace('\n','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("http://alexa.lr2b.com/proxylist.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt")
	    text = r.text.replace('</body>','').replace('</html>','').replace('<body bgcolor="white">','').replace('<center><h1>522 Origin Connection Time-out</h1></center>','').replace('<head><title>522 Origin Connection Time-out</title></head>','').replace('<hr><center>cloudflare-nginx</center>','').replace('<html>','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt")
	    text = r.text.replace('</body>','').replace('</html>','').replace('<body bgcolor="white">','').replace('<center><h1>522 Origin Connection Time-out</h1></center>','').replace('<head><title>522 Origin Connection Time-out</title></head>','').replace('<hr><center>cloudflare-nginx</center>','').replace('<html>','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1

	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
		r = requests.get('https://proxy-daily.com/')
		data = r.text
		soup = BeautifulSoup(data, 'lxml')
		
		alist = soup.find("div", class_="centeredProxyList freeProxyStyle").text.strip()
		
		with open(output, 'a+') as f:
			f.write(alist)

		lines = 0
		with open(output, 'r') as f:
		    for line in f:
		        lines = lines + 1
		    f.close()
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("http://www.proxylists.net/http_highanon.txt")
	    text = r.text

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://webanetlabs.net/freeproxy/proxylist_at_24.05.2016.txt")
	    text = r.text.replace('\n','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)


	try:
	    r = requests.get("https://files.a-parser.com/Proxy/alive_public_proxy_200615.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://www.proxyscan.io/download?type=http")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://www.proxyscan.io/download?type=https")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://multiproxy.org/txt_all/proxy.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("http://rootjazz.com/proxies/proxies.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("http://ab57.ru/downloads/proxyold.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)

	try:
	    r = requests.get("https://proxy-spider.com/api/proxies.example.txt")
	    text = r.text.replace('http://','').replace('socks://','')

	    lines = 0
	    with open(output, 'a+') as f:
	        f.write(text)
	        lines += 1
	    
	
	except:
	    print(Fore.MAGENTA+f"[{Fore.RED}!{Fore.MAGENTA}] - 0 Proxies Scraped"+Fore.RESET)


	lines = 0
	with open(output, 'r') as f:
	    for line in f:
	        lines = lines + 1
	    f.close()

	print(Fore.MAGENTA+f"\n\n[{Fore.RESET}+{Fore.MAGENTA}] - {Fore.RESET}{lines}{Fore.MAGENTA} Total proxy scraped !"+Fore.RESET)


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
