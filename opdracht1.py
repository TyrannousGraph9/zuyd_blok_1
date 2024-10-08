#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 'Opdracht 1: Basis Python en Variabelen'
# Purpose:          Programma om de basis van Python te leren
# Author:           Niels Cremers
#
# Created:          6-09-2024 
# Updates:          16-09-2024


import random
# import random voor een random getal te krijgen voor de dobbelsteen


# functie om de input van de user te vragen
def get_input():
    naam = input('Voer hier je naam in!' + '\n')
    leeftijd = input('Voer hier je leeftijd in!'+ '\n')

    check_input(naam, leeftijd)

# functie om de input te checken of de naam en de leeftijd geen ongeldige tekens bevatten
def check_input(naam, leeftijd):
    if not naam.isalpha():
        print("Geen geldige naam. Probeer opnieuw.")
        get_input()

    if not leeftijd.isdigit():
        print("Geen geldige leeftijd. Probeer opnieuw.")
        get_input()

    print('\n' + "Welkom " + naam + ", je bent " + leeftijd + " jaar oud.")
    throw_dobbel()

# functie om de dobbelsteen te gooien
def throw_dobbel():
    random_numb = random.randrange(1,6)
    print("Je hebt een dobbelsteen gegooid, en je hebt nummer " + str(random_numb) + " gegooid!")
    

# call de Input functie
get_input()




