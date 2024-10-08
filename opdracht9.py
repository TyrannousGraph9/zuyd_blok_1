#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 8: Gebruikersinvoer en Interactie
# Purpose:          Programma om Gebruikersinvoer en Interactie te leren
# Author:           Niels Cremers
#
# Created:          7-10-2024  


import random

import msvcrt
import time

def throw_dobbel():

    dobbel = random.randrange(1,6)
    return dobbel


def main_program():

    input("\n Klik op enter om een dobbelsteen te gooien.")
    print(f" \n je hebt {throw_dobbel()} gegooid!")

    get_input_key()

def get_input_key():
    
    print("\n Wil je doorgaan? \n Klik op y om door te gaan en op n om te stoppen.")
    
    pressed_button = msvcrt.getch()

    pressed_button = pressed_button.decode("utf-8")

    if pressed_button == "y":
        main_program()
    
    if pressed_button == "n":
        quit()
    
    else:
        print("\n Dit is geen y of n.")
        time.sleep(2)
        get_input_key()

main_program()

    