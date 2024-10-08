#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 5: Dictionaries
# Purpose:          Programma om dictionaries te leren
# Author:           Niels Cremers
#
# Created:          17-09-2024 

# import random voor de dobbelsteen values te pakken en random nummers te generaten
import random


# functie voor de dobbelsteen te rollen met parameter voor hoevaak je wilt rollen

def throw_dice(roll_amount):
    dice_dict =  {}

    # for loop om te dobellen op basis van de waarde van roll_amount

    for i in range(0,int(roll_amount)):
        dice_value = random.randrange(1,6)
        dice_value_1 = random.randrange(1,6)
        dice_dict.update({str(dice_value) + "," + str(dice_value_1) : dice_value + dice_value_1})
    
    # run de functie search_dice_combination met als parameter de dictionary van de combinaties.
    search_dice_combination(dice_dict)

# functie voor de dobbelsteen combinatie te zoeken

def search_dice_combination(dice_dict):
    dice_combination = int(input("Welk nummer wil je opzoeken? \n"))
    if(dice_combination < 2 or dice_combination > 6):
        print("Dit getal kan niet.")
        throw_dice(100)

    # for loop om de value te zoeken voor de nummer combinaties die eerder werden gegeven
    for i, value in dice_dict.items():
        if(value == dice_combination):
          print("\n" + i, value)
    
# call de throw dice functie 

throw_dice(100)

