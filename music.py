#!/usr/bin/python
#!/usr/local/bin/python
#coding: latin-1
#By SK OFFICIALL TM
#https://github.com/skshohid
#https://sk-officialltm.weebly.com/
import os
import sys
import time
os.system('pkg install play-audio')
os.system('cls' if os.name == 'nt' else 'clear')
def Logo():
	os.system('figlet -f slant MR. SHOHID')
	os.system('lolcat /sdcard/Termux/Play_music/logo.txt')
Logo()
def Time():
	localTime = time.localtime()
	current_time = time.strftime("%I:%M:%S", localTime)
	print(f'''\r\033[31m Play—Timeᗒ\033[33m{current_time}
''',end="")
	time.sleep(0.10)
def play():
	pil = input("\033[34m[\033[31m+\033[34m]\033[96;1mSelect:> \033[32m") 
	Time()
	if pil in ["01", "1"]:
		os.system('play-audio Boyfriend.xml')
		os.system('clear')
	if pil in ["02", "2"]:
		os.system('play-audio Let_Me.xml')
		os.system('clear')
	if pil in ["03", "3"]:
		os.system('play-audio Lut_Gaye.xml')
		os.system('clear')
	if pil in ["04", "4"]:
		os.system('play-audio Nachange.xml')
		os.system('clear')
	if pil in ["05", "5"]:
		os.system('play-audio DILBAR.xml')
		os.system('clear')
	if pil in ["07", "6"]:
		os.system('play-audio Meri_Aashiqui.xml')
		os.system('clear')
	if pil in ["07", "7"]:
		os.system('play-audio Mile_Ho.xml')
		os.system('clear')
	if pil in ["08", "8"]:
		os.system('play-audio Vaaste.xml')
		os.system('clear')
	if pil in ["09", "9"]:
		os.system('play-audio Bom_Diggy.xml')
		os.system('clear')
	if pil in ["10"]:
		os.system('play-audio Arijit_Singh.xml')
		os.system('clear')
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
Logo()
play()
os.system('clear')
os.system('figlet  THANK')
os.system('lolcat /sdcard/Termux/Play_music/logo.txt')
os.system('xdg-open https://www.facebook.com/skshohids0337')