import requests
import discord
import asyncio
import yaml
import os
client = discord.Client()
channel_id = None
started = False


ver = 1


def new_version_checker():
	url = 'https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/_discord.py'
	text = requests.get(url).text
	return float(text[text.find('ver')+6:text.find('a',text.find('ver')+6)])

def new_settings_version_checker():
	url = 'https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings.yaml'
	text = requests.get(url).text
	return float(text[text.find('Settings_Version')+18:-1])


try:
	with open("settings.yaml", 'r') as f:
		settings = yaml.load(f, Loader=yaml.FullLoader)
	TOKEN = settings["TOKEN"]
	settings_ver = int(settings["Settings_Version"])
except FileNotFoundError:
	print('settings.yaml not found!' + '\n' + 'Downloading settings.yaml')
	os.system("curl -o settings.yaml https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings.yaml")

if not new_version_checker() <= ver:
    print('New version found but not necessary to update right now' + '\n' + 'Would you like to download the new version now? (y/n)')
    ans = input('> ').lower()
    if ans == 'y':
        print('\nDownloading')
        os.system("curl -o _discord.py https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/_discord.py")
    elif ans == 'n':
        pass
    else:
        print('no?')
        input()
        exit()

if not new_settings_version_checker() <= settings_ver:
	print('New settings version found\nDownloading now')
	os.system("curl -o settings.yaml https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings.yaml")

to_spam = input('What to spam: ')

try:
	times_to_spam = int(input('Times to spam: '))
	if times_to_spam <= 0:
		print('not funny stop it')
		input()
		exit()
except ValueError:
	print('no not funny bruh')
	input()
	exit()

@client.event
async def on_ready():
	print('Ready')
	print('Say "{0}" In The Place You Want To Spam'.format(to_spam))

@client.event
async def on_message(message):
	global started
	global channel_id
	global times_to_spam
	if message.author == client.user:
		if message.content.startswith(to_spam):
			if channel_id is None:
				channel_id = message.channel.id
			started = True
	if started and message.channel.id == channel_id and times_to_spam > 0:
		await message.channel.send(to_spam)
		times_to_spam -= 1
	if times_to_spam <= 0:
		print('Close The Terminal To Exit')
		input()




client.run(TOKEN, bot=False)
