import os
from languages import game_es

def clear_screen():
	if os.name == "nt":
	    os.system("cls")
	else:
	    os.system("clear")

while True:
	clear_screen()
	print("1. English (not implemented)")
	print("2. Español")
	print("")
	gameSelection=int(input("Option: "))
	
	if gameSelection==1:
		clear_screen()
		input("The english version has not been implemented yet.")
	elif gameSelection==2:
		clear_screen()
		game_es.play()
		break