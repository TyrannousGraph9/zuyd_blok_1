#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 4: Geavanceerde Lijstoperaties
# Purpose:          Programma om de Geavanceerde Lijstoperaties te leren
# Author:           Niels Cremers
#
# Created:          16-09-2024 


import random
# import random voor een random getal te krijgen voor de dobbelsteen


# functie waarmee we een dobbelsteen gooien, de nummers opslaan in een lijst en doorsturen naar CountAppereance en count_even_numbers
def dobbel_worp():
    dobbel_amount = random.randint(0,30)
    worp_lists = []

    for i in range(0,int(dobbel_amount)):
        worp = random.randrange(1,7)
        worp_lists.append(worp)

    print("Je hebt " + str(dobbel_amount) + " keer gedobbeld")
    count_appereance(worp_lists)
    count_even_numbers(worp_lists)

# functie waarmee uitprinten hoevaak een nummer is voorgekomen
def count_appereance(worp_lists):
    for number in range(1, 7):  # Loop van 1 tot en met 6
        count = worp_lists.count(number)
        print(f"Het getal {number} is {count} keer voorgekomen!")

# functie om te kijken welk nummer even is en dit word opgeslagen in een list en geprint
def count_even_numbers(worp_lists):
    even_numbers = []
    for i in worp_lists:
        if (i % 2) == 0:
            even_numbers.append(i)
    
    print(even_numbers)
    
# start dobbel_worp
dobbel_worp()


