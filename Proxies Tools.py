import requests, os, colorama
from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style

URL = "http://google.com"
CMD_CLEAR_TERM = "cls"
TIMEOUT = (3.05,27)

banner = f"""
				██╗     ███████╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
				██║     ██╔════╝██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗
				██║     █████╗  █████╗  ██║     ███████║█████╗  ██████╔╝
				██║     ██╔══╝  ██╔══╝  ██║     ██╔══██║██╔══╝  ██╔══██╗
				███████╗███████╗███████╗╚██████╗██║  ██║███████╗██║  ██║
				╚══════╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


				     [{Fore.CYAN}1{Fore.RESET}] - Proxies Scraper | [{Fore.CYAN}3{Fore.RESET}] - Proxies Checker


                                                        
""".replace('█',Fore.CYAN+'█'+Fore.RESET)

def check_proxy(proxy):
    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        session.get(URL, proxies={'http':'http://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
    except:
    	return e


def proxieschecker():
	os.system('cls')
	print(banner)
	try:
	    file = open("Proxies.txt")
	    proxies = list(file)
	    goods = 0
	    terminal(CMD_CLEAR_TERM)
	    print(Fore.LIGHTCYAN_EX + '===========================================')
	    for proxy in proxies:
	        try:
	            if check_proxy(proxy):
	                print(Fore.LIGHTRED_EX + 'Bad proxy ' + proxy)
	            else:
	                print(Fore.LIGHTGREEN_EX + 'Good proxy ' + proxy)
	                file_with_goods = open('./output/good.txt','a')
	                file_with_goods.write(proxy)
	                goods += 1
	        except:
	        	pass

	    print(Fore.LIGHTCYAN_EX + '===========================================')
	    print(Fore.LIGHTGREEN_EX + 'Total ' + str(goods) + ' good proxies found')
	    print()
	except FileNotFoundError:
	    pass

def proxyscraper():
	os.system('cls')
	print(banner)
	try:
		r = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
		r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
		r3 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
		
		text = r.text
		text2 = r2.text
		text3 = r3.text
		text = text.replace("\n","")
		text2 = text2.replace("\n","")
		text3 = text3.replace("\n","")
		

		with open (f"Proxies.txt","w") as f:
		    f.write(text)
		    f.write(text2)
		    f.write(text3)
		
		lines = 0
		
		with open(f'Proxies.txt', 'r') as f:
		        for line in f:
		            lines = lines + 1
		        f.close()
		        print('[{}SUCCESS{}] - Scraped {} '.format(Fore.GREEN, Fore.RESET, lines) + 'proxies.')
	
	except:
		print('[{}ERROR{}] - O Proxies Scraped '.format(Fore.RED, Fore.RESET))


def menu():
	os.system('title Proxies Tools by Kaneki ^| Leecher - Scraper - Checker ^| Open Source')
	os.system('cls')
	print(banner)
	while True:
		lee = input(Fore.RESET+"[\033[1;31mPROXYS{}] - > ".format(Fore.RESET))

		if lee == "clear" or lee == "cls":
			menu()

		elif lee == "1":
			proxyscraper()

		elif lee == "3":
			proxieschecker()

		else:
			print(f"'{lee}' Command Invalid !")

menu()