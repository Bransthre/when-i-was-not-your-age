# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:30:08 2021

@author: brand
"""
from player import *
from battleField import battleField

a1 = collegeOfEngineering("Aditya Trippy3003")
a2 = lettersAndScience("Aditya adit.bala")
a3 = lettersAndScience("Aditya dtslumpgod jr")
a4 = collegeOfEngineering("Aditya aohri")
a5 = collegeOfEngineering("Aditya adityeah")
a6 = haas("Aditya (EECS) DankPrankster")
a7 = haas("Aditya LocalHostNotFound")
a8 = haas("Aditya (Economics) AdityaJoshi101")
a9 = haas("Aditya (Physics/CS) yandhi")
a10 = lettersAndScience("Aditya nugget")
a11 = lettersAndScience("Aditya mega")
a12 = collegeOfEngineering("Aditya AADI")
p1 = lettersAndScience("A M O G U S")
p2 = lettersAndScience("Oski's Clone")
p3 = collegeOfEngineering("Sans Undertale")
p4 = collegeOfEngineering("C R I S P R")
p5 = haas("Stonks")
p6 = haas("Zucc")
p7 = lettersAndScience("Peter Parker")
p8 = collegeOfEngineering("RAMEN")
p9 = haas("Bazos")

r1 = haas("Ryan (Business) RyuYoshika")
r2 = lettersAndScience("Ryan (Computer Science) TheRyGuy34")
r3 = lettersAndScience("Ryan (Physics) liuryan")
r4 = lettersAndScience("Ryan (Undeclared) Out0f|deas")
r5 = lettersAndScience("Ryan (Comp Sci) GoblinRum")
r6 = haas("Ryan (Business) ruachange")
r7 = lettersAndScience("Ryan (Computer Science) sockhock")
r8 = lettersAndScience("Ryan (Economics) lifein2021")
r9 = collegeOfEngineering("Ryan (EEKS) DaJuukes")
r10 = lettersAndScience("Ryan (Physics) ryanopher")
r11 = collegeOfEngineering("Ryan (EEKS) Mekav")
r12 = collegeOfEngineering("Ryan (BioEngineering) RyanReal")
r13 = collegeOfEngineering("Ryan (Quantum Physics) Breezy")
r14 = collegeOfEngineering("Ryan (EEKS) ryyn")

z1 = lettersAndScience("Zaid #1")
z2 = lettersAndScience("Zaid #2")
z3 = lettersAndScience("Zaid #3")
z4 = lettersAndScience("Zaid #4")
z5 = lettersAndScience("Zaid #5")
z6 = lettersAndScience("Zaid #6")
z7 = collegeOfEngineering("Zaid #7")
z8 = collegeOfEngineering("Zaid #8")
z9 = collegeOfEngineering("Zaid #9")
z10 = collegeOfEngineering("Zaid #10")
z11 = collegeOfEngineering("Zaid #11")
z12 = collegeOfEngineering("Zaid #12")
z13 = collegeOfEngineering("Zaid #13")
z14 = haas("Zaid #14")
z15 = haas("Zaid #15")
z16 = haas("Zaid #16")
z17 = haas("Zaid #17")
z18 = haas("Zaid #18")
z19 = haas("Zaid #19")
z20 = haas("Zaid #20")

playerList1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
playerList2 = [p1, p2, p3, p4, p5, p6]
playerList3 = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20]
playerList4 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14]

def gameInitiate(playerList):
    field = battleField(playerList)
    while(not field.victoryCheck()):
        field.inGameTurn()
        print("enter to continue this battle!")
        statement = str(input())
    for i in range(len(field.playerOrder)):
        print(str(len(field.playerOrder) - i + 1) + " place is " + field.playerOrder[i].name)
    print("1st place: " + field.playerList[0].name)
    print("type yes to have second battle.")
    statement = str(input())
    if(statement == "yes"):
        gameInitiate(playerList)
print("fun mode 2, zaid mode 3, aditya mode 1")
decision = int(input())
if(decision == 1):
    gameInitiate(playerList1)
elif(decision == 2):
    gameInitiate(playerList2)
elif(decision == 3):
    gameInitiate(playerList3)
elif(decision == 4):
    gameInitiate(playerList4)