import random
import time

# Variablen 
figuren = ("Schere", "Stein", "Papier")
index = (input("Wähle für Schere 0, für Stein 1 und für Papier 2"))
if index == 0 or index == 1 or index == 2:     
    spieler = figuren[int(index)]
    npc = figuren[random.randint(0,2)]
    if spieler == "Schere": 
        if npc == "Schere":
            print ("Unentschieden Der npc hat " + npc + " gewählt")
        if npc == "Papier": 
            print ("Du hast gewonnen Der npc hat " + npc + " gewählt")
        if npc =="Stein": 
            print ("Du hast verloren Der npc hat " + npc + " gewählt")
    if spieler == "Stein": 
        if npc == "Papier":
            print ("Du hast verloren Der npc hat " + npc + " gewählt")
        if npc == "Stein": 
            print ("Unentschieden Der npc hat " + npc + " gewählt")
        if npc == "Schere": 
            print ("Du hast gewonnen Der npc hat " + npc + " gewählt")
    if spieler == "Papier":
        if npc =="Papier": 
            print ("Unentschieden Der npc hat " + npc + " gewählt")
        if npc =="Stein": 
            print ("Du hast gewonnen Der npc hat " + npc + " gewählt")  
        if npc =="Schere": 
            print ("Du hast verloren Der npc hat " + npc + " gewählt")
else: 
    print ("nope")
    