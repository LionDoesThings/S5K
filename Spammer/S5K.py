import keyboard
import yaml
from pynput.keyboard import Key, Controller

print(f'''S5K Made By LionDoesThings
YouTube: https://www.youtube.com/channel/UCzpt7vwCAola2IJ1c4rD1aQ
''')

# yaml
def readYamlFile(arg):
    with open('settings.yaml') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    if arg == "start":
        return data["Hotkeys"]["Start"]
    elif arg == "stop":
        return data["Hotkeys"]["Stop"]
    elif arg == "cooldown":
        return data["Misc"]["SpamCooldown"]


# Variables
start = readYamlFile("start")
stop = readYamlFile("stop")
spamcd = readYamlFile("cooldown")
spamming = False
started = True
ctrl = Controller

# Questions
what_to_spam = input(f'What Do You Want To Spam: ') + f'\n'
times_to_spam = int(input(f'How Many Times Do You Want To Spam: '))
print('')
print(f'Press "{start}" To Start Spamming')
print(f'Press "{stop}" To Emergency Stop')

# Main Code
while not keyboard.is_pressed(stop):

    if started:
        cooldown -= 1

        if times_to_spam <= 0:
            started = False

        if keyboard.is_pressed(start) and not spamming:
            spamming = True
            ctrl.press(Key.backspace)
            ctrl.release(Key.backspace)

        if cooldown <= 0 and spamming:
            ctrl.type(what_to_spam)
            cooldown = spamcd
            times_to_spam -= 1

# End
print(f'')
print(f'')
input(f'Press Enter To Close The Program')
