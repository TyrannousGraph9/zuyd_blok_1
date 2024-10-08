#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 'Opdracht 3: Functies'
# Purpose:          Programma om de basis van functies te leren
# Author:           Niels Cremers
#
# Created:          16-09-2024 

# import random voor de dobbelsteen
import random

# functie wat een dobbelsteen gooit waarvan de waarde tussen de 1 en 6 is
def gooi_dobbelsteen():
    dobbel_value = random.randrange(1,7)
    print("je hebt " + str(dobbel_value) + " gegooid")

# functie wat telt voor de waarde n, als de waarde 5 is telt ie van 1 tot 5
def tel_tot(n):
    for i in range(n):
        print(i)

gooi_dobbelsteen()

# input voor de n, waarbij we een +1 doen zodat ie correct telt.
number_input = int(input("Vul hier een getal in: "))
number_input+=1 

# Call de tel_tot functie
tel_tot(number_input)