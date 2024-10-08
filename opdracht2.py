#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 'Opdracht 2: Lijsten en Loops'
# Purpose:          Programma om de basis van lijsten en loops te leren
# Author:           Niels Cremers
#
# Created:          16-09-2024 

# functie voor de nummerlijst te maken
def create_number_lists():
    number_lijst = [1,2,3,4,5,6]
    for i in number_lijst:
        print(i)

# functie voor de input te vragen van de personen
def name_input():
    naam_lijst = []
    for i in range(0,4):
        persoon_naam = i+1
        naam = input("Vul hier de naam van persoon " + str(persoon_naam) + " in: ")
        naam_lijst.append(naam)
    
    for i in naam_lijst:
        print(i)

# call de create_number_lists functie
create_number_lists()

# Call de name_input functie
name_input()

