#----------------------------------------------------------------------------------------------------------
# Name:             Eindopdracht: Een Vereenvoudigde Versie van Regenwormen
# Purpose:          Programma om een vereenvoudigde versie van regenwormen te leren
# Author:           Niels Cremers
#
# Created:          04-11-2024



import random

tegels = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

aantal_tegels = 16

speler_beurten = [1,0,0,0,0,0,0]

def spel_opzet():

    input("Welkom bij het spel Regenwormen! Druk op enter om te beginnen.")
    aantal_spelers = int(input("Hoeveel spelers doen er mee? (2-4 spelers)"))

    if(aantal_spelers < 2 or aantal_spelers > 4):
        print("Het aantal spelers moet tussen de 2 en 4 liggen.")
        spel_opzet()
    
    speler_data = {}
    for i in range(aantal_spelers):
        speler_naam = input(f"Naam speler {i+1}: ")
        speler_leeftijd = int(input(f"Leeftijd speler {i+1}: "))
        speler_data[speler_naam] = speler_leeftijd

    save_data(speler_data)


def save_data(speler_data):

    save_speler_data = open("speler_data.txt", "w")
    for key in speler_data:
        save_speler_data.write(f"{key}:{speler_data[key]}\n")

    save_speler_data.close()

    
    print("De data is opgeslagen in speler_data.txt")
    print("Veel plezier met het spel!")
    start_spel()


def start_spel():


    file_data = {}
    read_data = open("speler_data.txt", "r")

    for line in read_data:
        key, value = line.split(":")
        file_data[key] = value
    
    if(len(file_data) == 0):
        print("Er is geen data gevonden. Start het spel opnieuw.")
        spel_opzet()
    
    print("De data is ingeladen.")
    game_loop(file_data)


def game_loop(file_data):
    global aantal_tegels
    
    while(aantal_tegels > 0):
        
        print("Het spel is begonnen!")
        for speler in file_data:
            if speler_beurten[list(file_data.keys()).index(speler)] == 1:
                print(f"{speler} is aan de beurt.")
                # Hier kan je de logica toevoegen voor de beurt van de speler
                # Bijvoorbeeld: gooi_dobbelstenen(), ronde_handeler(), etc.
                huidige_speler = list(file_data.keys()).index(speler)
                ronde_handeler(huidige_speler)
                # Na de beurt van de speler, de beurt doorgeven aan de volgende speler
                volgende_speler = (huidige_speler + 1) % len(file_data)
                ronde_handeler(volgende_speler)
                break

        

def ronde_handeler(huidige_speler):

    global speler_beurten

    for i in range(len(speler_beurten)):
        if i == huidige_speler:
            speler_beurten[i] = 1
        else:
            speler_beurten[i] = 0
    
    
def save_ronde_data(ronde_data):
    
    save_ronde_data = open("ronde_data.txt", "w")
    for key in ronde_data:
        save_ronde_data.write(f"{key}:{ronde_data[key]}\n")

    save_ronde_data.close()
    print("De ronde data is opgeslagen in ronde_data.txt")
    return


def gooi_dobbelstenen():

    return
    

start_spel()