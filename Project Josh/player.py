# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:05:09 2021

@author: brand
"""
import math as math
import random as random
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Player:
    def __init__(self, name, baseHP, speed, coordX, coordY):
        self.name = name
        self.level = 1
        self.baseHP = baseHP + 0.0
        self.currentHP = baseHP + 0.0
        self.speed = speed + 0.0
        self.coordX = coordX
        self.coordY = coordY
        self.status = ""
        self.damageLog = [0]
        self.entryMessage = ["", "Hah, bet you didn't see this coming!", 
                             "Now, I shall give your college despair",
                             "Oski Aditya. I'm looking for this bear.",
                             "Oski Alex, Oski Ryan, Oski everyman.",
                             "Your soul is crying. I will relieve it.",
                             "I know what to protect now!",
                             "You are a bit too sus to be my opponent.",
                             "You are the ambassador of the Tree, aren't you",
                             "FWOEJNFRERJINFKREJN. Execution Filed."]
        self.deathMessage = ["", "I will not just be a memory.",
                             "The Tree. The Bear. The Bruins. The Century.",
                             "Looking cool, Oski...",
                             "I will eject you.",
                             "Peter... I will leave it to you...",
                             "Go ahead, further than where I point.",
                             "Yeah, of course we couldn't get along...",
                             "Just... a bit..."]
        self.lvlUpMessage = ["", "It would be foolish to drop my sword here.",
                             "I have inherited your strength.",
                             "We both did this for Oski."]
    
    def shift(self, boundary):
        angle = random.random() * math.tau
        self.coordX += math.cos(angle) * 0.1 * self.speed
        self.coordY += math.sin(angle) * 0.1 * self.speed
        if self.coordX > boundary or self.coordX < -1 * boundary:
            self.coordX = boundary
        if self.coordY > boundary or self.coordY < -1 * boundary:
            self.coordY = boundary
    
    def lvlUp(self):
        self.level += 1
        self.baseHP += 4
        self.currentHP += 4
        self.speed += 2
        print(self.name + " is now Level " + str(self.level))
        print(self.name + ": " + self.lvlUpMessage[(self.diceRoll(1, 3) - 1)])
    
    def statDamage(self):
        sendback = 0
        if(self.status.find("protect") != -1):
            return -100
        if(self.status.find("shield") != -1):
            return -1 * self.level
        if(self.status.find("paralysis") != -1):
            self.speed -= 2
            return 1 + self.level
        if(self.status.find("prey") != -1):
            self.currentHP -= 1
            print("by enemy's weapon skill \"prey\", 2HP was lost.")
            return 2
        if(self.status.find("breadth") != -1):
            return 2
        return sendback
    
    def diceRoll(self, upBound, throwNum):
        sendback = 0
        for i in range(throwNum):
            sendback += math.ceil(random.random() * upBound)
        return sendback
    

class lettersAndScience(Player):
    def __init__(self, name):
        coordX = 5 * math.cos(math.tau * random.random())
        coordY = 5 * math.sin(math.tau * random.random())
        Player.__init__(self, name, 25, 6, coordX, coordY)
        self.passiveUse = 1
        self.weaponry = ["","Oski Sword", "Breadth Requirements", "Dual Major Breath"]
        self.playerType = "College of Letters and Science"
        self.passiveMsg = [Fore.LIGHTYELLOW_EX + "Upon " + self.name + " 's Seventh Breadth, Territory Expand!",
                           Fore.LIGHTYELLOW_EX + "Beyond my sword will lie your past! Behold! Seventh Breadth of Letters and Science!",
                           Fore.LIGHTYELLOW_EX + "Oski Template Initiate. Sword Form. Seventh Breadth, Imaginary."]
    
    def combatMessage(self, damage, player2):
        x = self.level
        if(x > 3):
            x = 3
        print(Fore.LIGHTYELLOW_EX + self.name + " used " + self.weaponry[x] + " and dealt " + str(damage) + " damage to " + player2.name)
    
    def passive(self, player2):
        if(self.currentHP < 0.4 * self.baseHP and self.passiveUse >= 1):
            damage = 7 + player2.statDamage()
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            print(Fore.CYAN + self.name + ": " + self.passiveMsg[self.diceRoll(len(self.passiveMsg) - 1, 1)])
            print(Fore.CYAN + (player2.name + " was impacted by the strong breadth requirement and lost " + str(damage) + " HP."))
            self.passiveUse -= 1
            self.combatMessage(damage, player2)
    
    def regenerate(self):
        if(self.passiveUse < 1):
            self.passiveUse += 0.5
        if(self.currentHP < self.baseHP):
            self.currentHP += 3
        self.status = ""
        
    def attack(self, player2):
        damage = player2.statDamage() + self.level
        if(self.level == 1):
            damage += self.diceRoll(6, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            self.combatMessage(damage, player2)
        elif(self.level == 2):
            player2.status += "breadth"
            damage += self.diceRoll(6, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            player2.status += "breadth"
            if(damage > 5):
                print("\n This angle, this position, this instant--- I am more than who I was!")
            self.combatMessage(damage, player2)
        else:            
            player2.status += "breadth"
            damage += self.diceRoll(6, 2)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            if(damage > 9):
                print("\n This is the diversity of my arts!")
            self.combatMessage(damage, player2)
        player2.damageLog.append(damage)

class collegeOfEngineering(Player):
    def __init__(self, name):
        coordX = 5 * math.cos(math.tau * random.random())
        coordY = 5 * math.sin(math.tau * random.random())
        Player.__init__(self, name, 25, 8, coordX, coordY)
        self.passiveUse = 2
        self.weaponry = ["","Oski Launcher", "Circuit Tracer", "Gamechanger"]
        self.playerType = "College of Engineering"
        self.passiveMsg = [Fore.LIGHTYELLOW_EX + "I have came. I have engineered. I have mastered your truth.",
                           Fore.LIGHTYELLOW_EX + "This is the only shield engine I hold.",
                           Fore.LIGHTYELLOW_EX + "What are you afraid of? Attack. I, " + self.name + " will rule your fear."]
    
    def combatMessage(self, damage, player2):
        x = self.level
        if(x > 3):
            x = 3
        print(Fore.LIGHTYELLOW_EX + self.name + " used " + self.weaponry[x] + " and dealt " + str(damage) + " damage to " + player2.name)
    
    def passive(self, player2):
        if(self.passiveUse < 2):
            tgIndex = self.status.find("protect")
            self.status = self.status[:tgIndex] + self.status[tgIndex + 7:]
        if(self.currentHP < 0.5 * self.baseHP and self.passiveUse >= 2):
            print(Fore.CYAN + self.name + ": " + self.passiveMsg[self.diceRoll((len(self.passiveMsg) - 1), 1)])
            self.passiveUse -= 2
            self.status += "protect"

    def regenerate(self):
        if(self.passiveUse < 2):
            self.passiveUse += 0.75
        if(self.currentHP < self.baseHP):
            self.currentHP += 5
        
    def attack(self, player2):
        damage = player2.statDamage()
        if(self.level == 1):
            damage += self.diceRoll(6, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            self.currentHP += player2.damageLog[-1] * 0.1
            self.combatMessage(damage, player2)
        elif(self.level == 2):
            damage += self.diceRoll(6, 2)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            if(damage > 8):
                print("\n Delicious! Show me more!")
            self.combatMessage(damage, player2)
            heal = player2.damageLog[-1] * 0.1
            print(Fore.CYAN + self.name + " has drained blood from " + player2.name + " by " + str(heal) + " HP!")
            self.currentHP += heal
        else:
            damage += self.diceRoll(8, 2)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage
            player2.status += "prey"
            self.combatMessage(damage, player2)
            if(damage > 10):
                print("\n We are Gamechangers. We are BERKELEY!!!")
            heal = player2.damageLog[-1] * 0.2
            print(Fore.CYAN + self.name + " has drained blood from " + player2.name + " by " + str(heal) + " HP!")
            self.currentHP += heal

        player2.damageLog.append(damage)

class haas(Player):
    def __init__(self, name):
        coordX = 5 * math.cos(math.tau * random.random())
        coordY = 5 * math.sin(math.tau * random.random())
        Player.__init__(self, name, 30, 4, coordX, coordY)
        self.passiveUse = 1
        self.weaponry = ["","Oski Shield", "Laffer Curve", "Fiat Lux"]
        self.playerType = "Haas"
        self.passiveMsg = [Fore.LIGHTYELLOW_EX + "What happens now is your business ---",
                           Fore.LIGHTYELLOW_EX + "Oski, lend me the strength to protect my comrades!",
                           Fore.LIGHTYELLOW_EX + "Shield Form, Initiate."]
    
    def combatMessage(self, damage, player2):
        x = self.level
        if(x > 3):
            x = 3
        print(Fore.LIGHTYELLOW_EX + self.name + " used " + self.weaponry[x] + " and dealt " + str(damage) + " damage to " + player2.name)
    
    def passive(self, player2):
        if(self.passiveUse >= 1):
            print(Fore.LIGHTMAGENTA_EX + self.name + ": " + self.passiveMsg[self.diceRoll((len(self.passiveMsg) - 1), 1)])
            self.status += "shield"

    def regenerate(self):
        if(self.passiveUse < 1):
            self.passiveUse += 1
        if(self.currentHP < self.baseHP):
            self.currentHP += 3
        
    def attack(self, player2):
        damage = player2.statDamage()
        if(self.level == 1):
            damage += self.diceRoll(4, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage + self.damageLog[-1] * 0.2
            self.combatMessage(damage, player2)
        elif(self.level == 2):
            damage += self.diceRoll(6, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage + self.damageLog[-1] * 0.2
            if(damage > 6):
                print("\n" + "HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAS!!!!!!")
            self.combatMessage(damage, player2)
        else:
            damage += self.diceRoll(8, 1)
            if(damage < 0):
                damage = 0
            player2.currentHP -= damage + self.damageLog[-1] * 0.3
            player2.status += "paralysis!"
            if(damage > 6):
                print("\n" + "I will never kneel after my shield! Let alone your Blood! Fiat Lux!")
            self.combatMessage(damage, player2)
        player2.damageLog.append(damage)