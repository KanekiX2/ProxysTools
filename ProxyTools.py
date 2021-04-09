import os, colorama, threading, sys, json, requests, time
from colorama import Fore, Style
from threading import Thread

def banner():
	print(f"""
						{Fore.LIGHTBLUE_EX}╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔╦╗╔═╗╔═╗╦  ╔═╗{Fore.RESET}
						{Fore.LIGHTBLUE_EX}╠═╝╠╦╝║ ║╔╩╦╝╚╦╝   ║ ║ ║║ ║║  ╚═╗{Fore.RESET}
						{Fore.LIGHTBLUE_EX}╩  ╩╚═╚═╝╩ ╚═ ╩    ╩ ╚═╝╚═╝╩═╝╚═╝{Fore.RESET}

					{Fore.LIGHTMAGENTA_EX}╔═════════════════════════════════════════════╗
					{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}   {Fore.LIGHTBLUE_EX}1 -{Fore.RESET} Proxy Scraper          	      	      {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
					{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}   {Fore.LIGHTBLUE_EX}2 -{Fore.RESET} Proxy Checker  		              {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
					{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}   {Fore.LIGHTBLUE_EX}3 -{Fore.RESET} Exit 		     	              {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}
					{Fore.LIGHTMAGENTA_EX}╚════════════════════════════════ {Fore.RESET}Settings{Fore.LIGHTMAGENTA_EX} ═══╝


"""+Fore.RESET)

def ProxyChecker(prx, site):
    proxy = {'http': 'http://'+prx, 'https': 'http://'+prx}
    try:
        r = requests.get(site, proxies=proxy,timeout=1)

        print(Fore.LIGHTBLUE_EX+"   [!] - "+f"{Fore.RESET}{prx} Added to 'proxies.txt'{Fore.LIGHTBLUE_EX}..."+Fore.RESET)

        with open("proxies.txt","a") as f:
            f.write(prx+"\n")
    
    except:
    	pass


def proxy_sc():
	with open("sources.txt", 'r') as f:
		f = [line.strip('\n') for line in f]

	for link in f:
		r = requests.get(link).text.replace('http://','').replace('socks://','')

		print(link+"  Done !")
		with open('Scraped_proxy.txt', 'a+') as file:
			file.write(r)

	lines = 0
	with open('Scraped_proxy.txt', 'r+') as f:
	    for line in f:
	        lines = lines + 1
	    f.close()

	time.sleep(1)
	os.system('cls||clear')
	banner()
	print(Fore.LIGHTBLUE_EX+"   [!] - "+f"{Fore.RESET}{lines} Proxys scraped successfuly{Fore.LIGHTBLUE_EX}..."+Fore.RESET)

def proxy_ch():
	os.system('cls||clear')
	banner()
	with open('Scraped_proxy.txt', 'r+') as f:
		f = [line.strip('\n') for line in f]
	
	for proxy in f:
		a = True
		while a:
		    Thread(target=ProxyChecker,args=(proxy, "https://google.com")).start()
		    a = False


def main():
	os.system('cls||clear')
	os.system('title Fast Proxy Scraper Checker ^| Author: github.com/KanekiX2 ')
	banner()

	while True:
		option = input("\n" +  Fore.LIGHTBLUE_EX + "   [?] - " + Fore.RESET + "Select Option (" + Fore.LIGHTBLUE_EX  + "1" + Fore.RESET + " or " + Fore.LIGHTBLUE_EX + "2" + Fore.RESET + " or " + Fore.LIGHTBLUE_EX + "3" + Fore.RESET + "): ")

		if option == "1":
			proxy_sc()

		elif option == "2":
			proxy_ch()

		elif option.lower() == "cls" or option.lower() == "clear":
			main()

		elif option == "3":
			print("  ")
			print(Fore.LIGHTBLUE_EX + "   [!] - " + Fore.LIGHTRED_EX + "Thanks, BYE!" + Fore.RESET)
			time.sleep(2)
			sys.exit()

		else:
			print(Fore.LIGHTBLUE_EX + "   [!] - " + Fore.LIGHTRED_EX + "Invalid option.." + Fore.RESET)



main()
