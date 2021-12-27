import requests

import os

import time

import random

os.system("clear")

os.system("figlet Discord Nitro generator")

print("                     made by NacreousDawn596")

def start():

	var = []

	choice = [0, 1]

	random.shuffle(choice)

	string= "a z e r t y u i o p q s d f g h j k l m w x c v b n A Z E R T Y U I O P Q S D F G H J K L M W X C V B N 1 2 3 4 5 6 7 8 9 0"

	string = string.split(" ")

	if choice[0] == 0:

		for you in range(16):

			random.shuffle(string)

			var.append(string[5])

		var = ''.join([str(item) for item in var])

		link = f"https://discord.gift/{var}"

		url = f"https://discord.com/api/v9/entitlements/gift-codes/{var}"

	else:

		for you in range(24):

			random.shuffle(string)

			var.append(string[5])

		var = ''.join([str(item) for item in var])
	
		link = f"https://discord.gift/{var}"

		url = f"https://discord.com/api/v9/entitlements/gift-codes/{var}"

	request = requests.get(url)

	nitro = request.json()

	gift = nitro['message']

	if gift == "Unknown Gift Code":

		print("")

		print("it doesn't works ", link)

		file = open ("links that doesn't work.txt", "a")

		file.write("".join(link))

		file.write("".join("\n"))

		file.close()

	elif gift == "The resource is being rate limited.":

		s = nitro['retry_after']

		while s >= 0:

			print("")

			print("retry after ", s, "seconds")

			time.sleep(1)

			s -= 1

	else: 

		print("")

		print("AVALAIBLE LINK: ", link)

		file = open ("AVALAIBLE LINKS.txt", "a")

		file.write("".join(link))

		file.write("".join("\n"))

		file.close()

	time.sleep(2)

	start()

start()
