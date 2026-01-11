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

def play():
    global beat
    if beat == 1:
        winsound.Beep(500, 100)
    else:
        winsound.Beep(400, 100)
    sleep(delay_between_beeps - 0.01)
    if beat == int(float(timesig)):
        beat = 1
    else:
        beat = beat + 1
    render()
    
def render():
    os.system("cls")
    print(Fore.MAGENTA + "Current Beat")
    if beat == 1:
        print(Fore.RED)
    elif beat % 2:
        print(Fore.GREEN)
    else:
        print(Fore.BLUE)
    print("▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰")
    print(Style.BRIGHT + pyfiglet.figlet_format(str(beat), font='slant') + "out of " + str(timesig) + " beats")
    print("▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰")
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
print(Fore.GREEN + "a simple metronome TUI app" + Back.YELLOW)
bpm = input(Fore.BLACK + "Enter BPM: ")
timesig = input("Enter NPM (Notes Per Measure): ")
delay_between_beeps = (60 / int(float(bpm)))
print(Style.RESET_ALL)
render()