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

speler_tegels = {}


def lees_winnaar():

    try:
        file = open("winnaar.txt", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("Er zijn nog geen winnaars bekend.")

def spel_opzet():

    lees_winnaar()
    input("Welkom bij het spel Regenwormen! Druk op enter om te beginnen.")
    aantal_spelers = int(input("Hoeveel spelers doen er mee? (2-7 spelers)"))

    if(aantal_spelers < 2 or aantal_spelers > 7):
        print("Het aantal spelers moet tussen de 2 en 7 liggen.")
        spel_opzet()
    
    speler_data = {}
    for i in range(aantal_spelers):
        speler_naam = input(f"Naam speler {i+1}: ")
        speler_leeftijd = int(input(f"Leeftijd speler {i+1}: "))
        speler_data[speler_naam] = speler_leeftijd

    game_loop(speler_data)

def game_loop(speler_data):

    global aantal_tegels
    
    aantal_spelers = len(speler_data)

    speler_data = dict(sorted(speler_data.items(), key=lambda x: x[1]))
    eerste_speler = list(speler_data.keys())[0]
    print(f"{eerste_speler} mag beginnen.")

    while(aantal_tegels > 0):
        
        for i in range(aantal_spelers):
            ronde_handeler(i)
            speler_naam = list(speler_data.keys())[i]
            print(f"Het is de beurt van {speler_naam}.")
            gooi_dobbelstenen(i)
    
    if(aantal_tegels == 0):
        print("Er zijn geen tegels meer over.")
        winner = bepaal_winner()
        print(f"De winnaar is: {winner}")
        print("Bedankt voor het spelen!")
        return
         

def ronde_handeler(huidige_speler):

    global speler_beurten

    for i in range(len(speler_beurten)):
        if i == huidige_speler:
            speler_beurten[i] = 1
        else:
            speler_beurten[i] = 0
    

def gooi_dobbelstenen(speler_id):

    global speler_tegels
    global aantal_tegels

    aantal_dobbelstenen = 8
    saved_numbers = {}
    wormen_waarde = 5

    while aantal_dobbelstenen > 0:

        dobbelstenen = [random.randint(1, 6) for _ in range(aantal_dobbelstenen)]
        dobbelstenen = [d for d in dobbelstenen if d not in saved_numbers]
        print(f"Je hebt gegooid: {dobbelstenen}")

        if not dobbelstenen:
            print("Alle gegooide dobbelstenen komen overeen met opgeslagen nummers. Reroll.")
            aantal_dobbelstenen = len(dobbelstenen)
            continue

        save_number = int(input("Welk nummer wil je opslaan? "))

        if save_number not in dobbelstenen:
            print("Dit nummer is niet gegooid. Probeer opnieuw.")
            continue

        if save_number in saved_numbers:
            print("Dit nummer is al opgeslagen. Kies een ander nummer.")
            continue

        count = dobbelstenen.count(save_number)
        saved_numbers[save_number] = count
        dobbelstenen = [d for d in dobbelstenen if d != save_number]
        
        print(f"Opgeslagen nummers: {saved_numbers}")

        aantal_dobbelstenen = len(dobbelstenen)

        if aantal_dobbelstenen == 0:
            print("Je hebt alle dobbelstenen opgeslagen.")
            break

        verder = input("Wil je verder gooien met de resterende dobbelstenen? (ja/nee) ")
        
        if verder.lower() != 'ja':
            break
    
    if 6 in saved_numbers:
        wormen = saved_numbers[6]
        saved_numbers.pop(6)
        for i in range(wormen):
            saved_numbers.append(wormen_waarde)
    else:
        print("Je hebt geen wormen (6) gegooid.")
        return
    
    totaal_punten = sum(number * count for number, count in saved_numbers.items())

    print(f"Je hebt in totaal {totaal_punten} punten.")
    
    if totaal_punten < 21:
        print("Je hebt te weinig punten om een tegel op te slaan. Je beurt is voorbij.")
        return
    if totaal_punten > 36:
        print("Je hebt te veel punten om een tegel op te slaan. Je beurt is voorbij.")
        return

    print(f"Kies een getal tussen 21 en {totaal_punten} om op te slaan.")
    gekozen_tegel = int(input("Welk getal wil je opslaan? "))

    if gekozen_tegel in speler_tegels.values():
        if speler_id in speler_tegels:
            speler_tegels.pop(speler_id)
            tegels.append(gekozen_tegel)
            print("Je hebt deze tegel al opgeslagen. Je legt deze terug.")
            print(speler_tegels)

    if gekozen_tegel in speler_tegels.values():
        print("Deze tegel is al opgeslagen door een andere speler. Je steelt deze tegel.")
        speler_tegels[speler_id] = gekozen_tegel
        print(speler_tegels)

    if gekozen_tegel not in tegels:
        print("Deze tegel bestaat niet. Kies een andere tegel.")
        gekozen_tegel = int(input("Welk getal wil je opslaan? "))
    else:
        print(f"Je hebt tegel {gekozen_tegel} opgeslagen.")
        tegels.remove(gekozen_tegel)
        aantal_tegels -= 1
        print(f"Er zijn nog {aantal_tegels} tegels over.")
        speler_tegels[speler_id] = gekozen_tegel
        print(speler_tegels)


def bepaal_winner():

    global speler_tegels

    winner = max(speler_tegels, key=speler_tegels.get)

    score = speler_tegels[winner]
    filewriter = open("winnaar.txt", "w")
    filewriter.write(f"{winner} heeft gewonnen met een score van {score}!")
    filewriter.close()

    return winner

spel_opzet()