#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 7: Complexere Functies en Modules
# Purpose:          Programma om Complexere Functies en Modules te leren
# Author:           Niels Cremers
#
# Created:          30-09-2024


import random

import math



def analyseer_worpen(dobbelcombos):

    print(type(dobbelcombos))

    print(type(sum(dobbelcombos)))

    print(type(len(dobbelcombos)))
    gemiddelde_waarde = sum(dobbelcombos) / len(dobbelcombos)
    
    print(gemiddelde_waarde)

    

def gooi_meerdere_dobbelstenen(aantal):
    dobbelcombos = []

    for i in range(0, aantal):
        dobbelsteen = random.randrange(1,6)
        dobbelcombos.append(dobbelsteen)
    
    print(dobbelcombos)
    analyseer_worpen(dobbelcombos)


gooi_meerdere_dobbelstenen(int(input("Hoevaak wil je gooien?")))


def math_opdracht():
    getal = input("Voer hier een nummer in.")
    
    getal = getal.replace("," , ".")
        
    getal = float(getal)

    print(f"Het nummber {getal} word afgerond omhoog tot {math.ceil(getal)} en omlaag als {math.floor(getal)} ")





math_opdracht()