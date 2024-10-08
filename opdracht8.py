#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 8: Spel Logica en Condities
# Purpose:          Programma om Spel Logica en Condities te leren
# Author:           Niels Cremers
#
# Created:          30-09-2024

import time

import random
# import random library voor de dobbelsteen

# globale lijst om de score bij te houden
dobbel_list = []

# spelers namen 

player_1_name = ""

player_2_name = ""

# speler wins

player_1_wins = 0

player_2_wins = 0

# functie om de dobbelsteen te gooien
def throw_dobbel():

    dobbel = random.randrange(1,7)
    return dobbel

# functie om het spel te starten
def start_game():

    global player_1_name
    global player_2_name
    

    dobbel_list.clear()
    
    player_1_name = input("Wat is de naam van speler 1?")
    player_2_name = input("Wat is de naam van speler 2?")

    if player_1_name == player_2_name or player_2_name == player_1_name:
        print("Speler namen kunnen niet hetzelfde zijn.")
        player_1_name = ""
        player_2_name = ""
        start_game()


    aantal_rondes = random.randrange(5,10)
    player_1 = True
    
    huidige_ronde = 0

    while huidige_ronde < aantal_rondes:

        if player_1:
            player_1_value = throw_dobbel()
            save_dobbel(player_1_name, player_1_value)
            player_1 = False

        else:
            player_2_value = throw_dobbel()
            save_dobbel(player_2_name, player_2_value)
            player_1 = True
            highest_round_score(huidige_ronde)
            huidige_ronde += 1
           
    
    print_score()


def save_dobbel(player,player_value):

    save_string = f"{player} - {player_value}"
    dobbel_list.append(save_string)

def print_score():

    if player_1_wins >= player_2_wins:
        print("Speler 1 heeft gewonnen met:" + str(player_1_wins) + " overwinningen")
    
    if player_2_wins >= player_1_wins:
        print("Speler 2 heeft gewonnen met:" + str(player_2_wins) + " Overwinningen")

    else:
        print("Gelijkspel! Beide spelers hebben " + str(player_1_wins) + " Overwinningen")

    exit()

    
def highest_round_score(huidige_ronde):


    global player_1_wins
    global player_2_wins

    player_1_value = dobbel_list[huidige_ronde * 2]
    player_2_value = dobbel_list[huidige_ronde * 2 + 1]

    player_1_value = int(player_1_value.replace(player_1_name + " - ", ''))
    player_2_value = int(player_2_value.replace(player_2_name + " - ", ''))

    my_new_file = open("scores.txt", "a")
    player_scores = str(f"{player_1_name + str(player_1_value)} + {player_2_name + str(player_2_value)} \n ")
    my_new_file.write(str(player_scores))
    my_new_file.close()

    if player_1_value >= player_2_value:
        print(f"Speler 1 heeft deze ronde gewonnen en heeft {player_1_value} gegooid.")
        time.sleep(2)
        player_1_wins += 1

    if player_2_value >= player_1_value:
        print(f"Speler 2 heeft deze ronde gewonnen en heeft {player_2_value} gegooid.")
        time.sleep(2)
        player_2_wins += 1
        
    if player_2_value == player_2_value:
        print(f"Gelijkspel! beide spelers hebben {player_1_value} gegooid.")
        time.sleep(2)


start_game()