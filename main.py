import os
os.system('pip install pynput requests keyboard discord asyncio')
os.system('cls')
print('S5K Made By LionDoesThings\nYouTube: https://www.youtube.com/channel/UCzpt7vwCAola2IJ1c4rD1aQ\n')
print('''Options:
[0] General Spammer
[1] Direct Discord Spammer
''')
a = int(input('> '))
if a == 0:
	if not os.path.isfile('_general.py'):
		os.system('curl -o _general.py https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/_general.py')
	os.system('py _general.py')
elif a == 1:
	if not os.path.isfile('_discord.py'):
		os.system('curl -o _discord.py https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/_discord.py')
	os.system('py _discord.py')
else:
	input('no\n')
	exit()
