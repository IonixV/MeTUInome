#   ____    ____       _________  _____  _____  _____                                     
# |_   \  /   _|     |  _   _  ||_   _||_   _||_   _|                                    
#  |   \/   |  .---.|_/ | | \_|  | |    | |    | |   _ .--.   .--.   _ .--..--.  .---.  
#  | |\  /| | / /__\\   | |      | '    ' |    | |  [ `.-. |/ .'`\ \[ `.-. .-. |/ /__\\ 
# _| |_\/_| |_| \__.,  _| |_      \ \__/ /    _| |_  | | | || \__. | | | | | | || \__., 
#|_____||_____|'.__.' |_____|      `.__.'    |_____|[___||__]'.__.' [___||__||__]'.__.' 
# Created by IonixV, made for Flavortown!!!!

import winsound
from colorama import Fore, Back, Style
# Sorry Linux Users!
from time import sleep
import os
import pyfiglet

beat = 1
measure = 0

def play():
    global beat
    global measure
    if beat == 1:
        winsound.Beep(500, 75)
    else:
        winsound.Beep(400, 75)
    sleep(delay_between_beeps - 0.0075)
    if beat == int(float(timesig)):
        beat = 1
        measure = measure + 1
    else:
        beat = beat + 1
    render()
    
def render():
    os.system("cls")
    print(Fore.MAGENTA + "Current beat")
    if beat == 1:
        print(Fore.RED)
    elif beat % 2:
        print(Fore.GREEN)
    else:
        print(Fore.BLUE)
    print(Style.BRIGHT + "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰")
    print(pyfiglet.figlet_format(str(beat), font='slant') + "out of " + str(timesig) + " beat(s)")
    print("▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰")
    print(Fore.WHITE + Style.NORMAL + "You are on measure " + str(measure))
    print(Fore.RED + "Press CTRL+C to Quit")
    play()

os.system("cls")
print(Fore.CYAN + "MeTUInome by ionixV")
print("""
   ____    ____       _________  _____  _____  _____                                     
 |_   \  /   _|     |  _   _  ||_   _||_   _||_   _|                                    
  |   \/   |  .---.|_/ | | \_|  | |    | |    | |   _ .--.   .--.   _ .--..--.  .---.  
  | |\  /| | / /__\\    | |      | '    ' |    | |  [ `.-. |/ .'`\ \[ `.-. .-. |/ /__\\ 
 _| |_\/_| |_| \__.,  _| |_      \ \__/ /    _| |_  | | | || \__. | | | | | | || \__., 
|_____||_____|'.__.' |_____|      `.__.'    |_____|[___||__]'.__.' [___||__||__]'.__.'
""")
print(Fore.MAGENTA + "https://flavortown.hackclub.com/projects/7404")
print(Fore.WHITE + "made for flavortown by hackclub!!")
print(Fore.GREEN + "a simple metronome TUI app" + Back.YELLOW)
winsound.Beep(700, 100)
winsound.Beep(500, 100)
winsound.Beep(600, 100)
winsound.Beep(400, 100)
bpm = input(Fore.BLACK + "Enter BPM: ")
winsound.Beep(400, 100)
winsound.Beep(600, 100)
timesig = input("Enter NPM (Notes Per Measure): ")
winsound.Beep(400, 100)
winsound.Beep(600, 100)
delay_between_beeps = (60 / int(float(bpm)))
print(Style.RESET_ALL)
render()