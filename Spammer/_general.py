from pynput.keyboard import Key, Controller
import keyboard
import requests
import yaml
import os


ver = 0.1


def new_version_checker():
    version_url = 'https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/version'
    return requests.get(version_url).text


def new_settings_version_checker():
    settings_version_url = 'https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings_version'
    return requests.get(settings_version_url).text


try:
    with open("settings.yaml", 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    start_hk = settings["Hotkeys"]["Start"]
    stop_hk = settings["Hotkeys"]["Stop"]
    spam_cd = int(settings["Misc"]["SpamCooldown"])
    settings_ver = int(settings["Settings_Version"])
except FileNotFoundError:
    print('settings.yaml not found!' + '\n' + 'Downloading settings.yaml')
    os.system("curl -o settings.yaml https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings.yaml")
    with open("settings.yaml", 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    start_hk = settings["Hotkeys"]["Start"]
    stop_hk = settings["Hotkeys"]["Stop"]
    spam_cd = int(settings["Misc"]["SpamCooldown"])
    settings_ver = int(settings["Settings_Version"])

if float(new_version_checker()) > ver:
    print('New version found but not necessary to update right now' + '\n' + 'Would you like to download the new version now? (y/n)')
    ans = input('> ').lower()
    if ans == 'y':
        print('\nDownloading')
        os.system("curl -o _general.py https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/_general.py")
    elif ans == 'n':
        pass
    else:
        print('no?')
        input()
        exit()

if float(new_settings_version_checker()) > settings_ver:
    print('New settings version found\nDownloading now')
    os.system("curl -o settings.yaml https://raw.githubusercontent.com/LionDoesThings/S5K-v3-aka-Yasuo/main/Spammer/settings.yaml")

0s.system('cls')
to_spam = input('What to spam: ') + '\n'

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

print('\n' + 'To start spamming please press "{}"'.format(start_hk) + '\n' + 'To force stop please press "{}"'.format(stop_hk))

ctrl = Controller()
started = False
spam_cd_done = True
spam_cd_ = spam_cd
while not keyboard.is_pressed(stop_hk):
    if keyboard.is_pressed(start_hk):
        started = True
        ctrl.press(Key.backspace)
        ctrl.release(Key.backspace)

    if started and times_to_spam > 0 and spam_cd_done:
        ctrl.type(to_spam)
        times_to_spam -= 1
        spam_cd_done = False

    if started:
        spam_cd_ -= 1

    if spam_cd_ <= 0:
        spam_cd_done = True
        spam_cd_ = spam_cd

    if times_to_spam <= 0:
        input('\n\n' + 'Spam completed\n' + 'Press Enter To Close The Program')
        exit()

input('\n\n' + 'Force stopped\n' + 'Press Enter To Close The Program')
