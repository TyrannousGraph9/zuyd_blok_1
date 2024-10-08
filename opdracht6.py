#----------------------------------------------------------------------------------------------------------
# Name:             Opdracht 6: File writing
# Purpose:          Programma om File writing te leren
# Author:           Niels Cremers
#
# Created:          30-09-2024 


# import random voor de dobbelsteen values te pakken en random nummers te generaten
import random

def start_program():

    throw_dobbel()

def file_handler(dobbel_list):
    my_new_file = open("pythoncreatedfile.txt","w")
     
    for i in range(0,len(dobbel_list)):
        my_new_file.write(f"Roll number {i +1 } is {dobbel_list[i]}. \n")

    my_new_file.close()

    my_file = open("pythoncreatedfile.txt", "r")
    print(my_file.read())

def throw_dobbel():

    dobbel_combos = []
    count = random.randrange(1,100)

    for i in range(0,int(count)):
        dobbel = random.randrange(1,6)
        dobbel_combos.append(dobbel)

    file_handler(dobbel_combos)

        

start_program()