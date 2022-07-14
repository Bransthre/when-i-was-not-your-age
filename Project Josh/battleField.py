# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 08:58:25 2021

@author: brand
"""
import math as math
import random as random
from datetime import datetime
import time as time
from colorama import init, Fore, Back, Style
init(autoreset=True)

class battleField():
    def __init__(self, playerList):
        self.radius = 6
        self.turn = 0
        self.playerList = playerList
        self.playerOrder = []
    
    def displayHPBar(self, player1):
        progress = round(player1.currentHP, 2)
        maximum = player1.baseHP
        percent = round(100 * progress / maximum, 1)
        numBars = percent / 100 * 50
        numRB, numYB, numGB = 0, 0, 0
        while(numBars > 0 and numRB <= 8):
            numRB += 1
            numBars -= 1
        while(numBars > 0 and numYB <= 12):
            numYB += 1
            numBars -= 1
        while(numBars > 0 and numGB <= 30):
            numGB += 1
            numBars -= 1
        numNB = 50 - (numRB + numYB + numGB)
        hpMsg = player1.name + " current HP: " + str(progress) + "/" + str(maximum) + " ("+str(percent)+"%)"
        print(Fore.LIGHTMAGENTA_EX + hpMsg + "\n" + Fore.BLUE + "||" + Style.BRIGHT + Fore.RED + numRB * "/" + Fore.YELLOW + numYB * "/" + Fore.GREEN + numGB * "/" + Fore.LIGHTWHITE_EX + numNB * "/" + Fore.BLUE + "||")
        
    def getDistance(self, player1, player2):
        distanceX = player1.coordX - player2.coordX
        distanceY = player1.coordY - player2.coordY
        return math.sqrt(distanceX**2 + distanceY**2)
    
    def scanSurrounding(self, player1):
        tgFighter = None
        tgDistance = 2
        if len(self.playerList) == 2:
            ptr = 0
            while(self.playerList[ptr] == player1):
                ptr += 1
            return self.playerList[ptr]
        for x in self.playerList:
            distance = self.getDistance(player1, x)
            if(x == player1):
                continue
            if(self.getDistance(player1, x) < tgDistance):
                   tgFighter = x
                   tgDistance = distance
        if(tgFighter == None):
            return -1
        return tgFighter
    
    def displayHP(self, player1, player2):
        print("\n=================================\n")
        self.displayHPBar(player1)
        self.displayHPBar(player2)
        print("\n=================================\n")
        time.sleep(0.5)
    
    def eliminatePlayer(self, player):
        if(player.currentHP < 0):
            print(player.deathMessage[player.diceRoll(len(player.deathMessage) - 1, 1)])
            print("\n")
            datehour = str(datetime.now())
            print(player.name + " has fallen, " + datehour)
            time.sleep(2)
            self.playerOrder.append(player)
            self.playerList.remove(player)
        return player.currentHP < 0
    
    def determineOrder(self, player1, player2):
        playerF, playerS = None, None
        if(player1.speed > player2.speed):
                playerF, playerS = player1, player2
        elif(player2.speed > player1.speed):
            playerF, playerS = player2, player1
        else:
            coinFlip = random.random()
            if(coinFlip > 0.5):
                playerF, playerS = player1, player2
            else:
                playerF, playerS = player2, player1
        return [playerF, playerS]
        
    def combat(self, player1, player2, interval):
        print("====================")
        print(player1.name + " and " + player2.name + " has entered combat!!")
        time.sleep(1)
        print(Fore.GREEN + player1.name +": " + (player1.entryMessage[player1.diceRoll(len(player1.entryMessage) - 1, 1)]))
        print(player1.name + " is a Level " + str(player1.level) + " from " + player1.playerType)
        time.sleep(2)
        print(Fore.GREEN + player2.name +": " + (player2.entryMessage[player2.diceRoll(len(player2.entryMessage) - 1, 1)]))
        print(player2.name + " is a Level " + str(player2.level) + " from " + player2.playerType)
        time.sleep(2)
        print("now, the battle begins!!!\n====================")
        playerArr = self.determineOrder(player1, player2)
        playerF, playerS = playerArr[0], playerArr[1]
        while(playerF.currentHP > 0 or playerS.currentHP > 0):
            self.displayHP(playerF, playerS)
            time.sleep(interval)
            playerF.attack(playerS)
            time.sleep(interval)
            playerF.passive(playerS)
            time.sleep(1.5)
            if(self.eliminatePlayer(playerS)):
                playerF.lvlUp()
                playerF.baseHP += 4
                playerF.currentHP += 2
                break
            playerS.attack(playerF)
            time.sleep(interval)
            playerS.passive(playerF)
            time.sleep(1.5)
            if(self.eliminatePlayer(playerF)):
                playerS.lvlUp()
                playerS.baseHP += 4
                playerS.currentHP += 2
                break
    
    def victoryCheck(self):
        if(len(self.playerList) <= 1):
            print("the battle has ended.")
        return len(self.playerList) <= 1

    def inGameTurn(self):
        self.turn += 1
        print("\nelimination enters turn " + str(self.turn))
        print("Surviving Names Left: " + str(len(self.playerList)))
        if(self.turn >= 5):
            for x in self.playerList:
                print(x.name + "survived last turn.")
        print("arena radius: " + str(self.radius))
        print("\n")
        i = len(self.playerList) - 1
        while(i >= 0):
            x = self.playerList[len(self.playerList) - 1 - i]
            tgPlayer = self.scanSurrounding(x)
            if(tgPlayer == -1):
                print(x.name + " did not encounter any enemies this turn.")
            else:
                self.combat(x, tgPlayer, 0.1)
            i -= 1
        if(self.radius > 0):
            self.radius -= 1
        for x in self.playerList:
            x.regenerate()
            x.shift(self.radius)
        