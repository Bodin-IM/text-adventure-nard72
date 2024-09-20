import random
from random import randint
from time import sleep
import time

money = 100000
hp = 100
enemyhp = 100
playerminDmg = 5
playermaxDmg = 20
hitChance = 90 # hit chance in percent
enemyHitchance = randint(50,70)
enemyDmg = randint(10,20)


def hpCheck(hp):
    if hp < 0:
        return True
    else:
        return False

def combat():
    global hp, playermaxDmg, playerminDmg, enemyDmg,enemyhp


    combat = True
    while combat:
        sleep(1)
        print(f"You have {hp} HP left. The enemy has {enemyhp} HP left.")
        
        # player attack
        if randint(0,100) < hitChance:
            dmg = randint(playerminDmg, playermaxDmg)
            enemyhp -= dmg
            print(f"You did {dmg} to the enemy, the enemy now has {enemyhp} HP.")
        else:
            print("You missed.")
            
        if hpCheck(enemyhp):
            print("Enemy is dead")
            combat = False
            break
        input()

        # enemy attack
        if randint(0,100) < enemyHitchance: # if enemy hits you
            enemyDmg = randint(10, 20)
            hp -=  enemyDmg
            print(f"he did {enemyDmg} to you, you have now {hp} HP left.")
        else:
            print("the enemy missed his attack")    
        
        if hpCheck(hp):
            print("You died")
            combat = False
            break


def slow_print(text, delay=0.002):
    """Function to simulate typing text gradually."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def room1():
    print("you enter a cold and empty room")
    print("you see a chest in the middle of the room")
    open = input("do you want to open it?y/n--> ")
    if open == "yes":
        print("its so dark you can bearly see whats in it")


def ending(ending):
    main()

def main():
    global hp,enemyDmg,enemyHitchance,enemyhp,hitChance,playermaxDmg,playerminDmg,money

    ''' slow_print(""" ____  ____     ___  _____ ____  ___      ___  ____   ______     
    |    |    \   /  _]/ ___/|    ||   \    /  _]|    \ |      |    
    |  o  )  D  ) /  [_(   \_  |  | |    \  /  [_ |  _  ||      |    
    |   _/|    / |    _]\__  | |  | |  D  ||    _]|  |  ||_|  |_|    
    |  |  |    \ |   [_ /  \ | |  | |     ||   [_ |  |  |  |  |      
    |  |  |  .  \|     |\    | |  | |     ||     ||  |  |  |  |      
    |__|  |__|\_||_____| \___||____||_____||_____||__|__|  |__|      
                                                                    
    _____ ____  ___ ___  __ __  _       ____  ______   ___   ____  
    / ___/|    ||   |   ||  |  || |     /    ||      | /   \ |    \ 
    (   \_  |  | | _   _ ||  |  || |    |  o  ||      ||     ||  D  )
    \__  | |  | |  \_/  ||  |  || |___ |     ||_|  |_||  O  ||    / 
    /  \ | |  | |   |   ||  :  ||     ||  _  |  |  |  |     ||    \ 
    \    | |  | |   |   ||     ||     ||  |  |  |  |  |     ||  .  |
    \___||____||___|___| \__,_||_____||__|__|  |__|   \___/ |__|\_|
    """)  '''
    print("you are holding a speech in front of a whole nation.")
    print("you are looking around..")
    print("you see a sniper glare")
    print("A: you jump left")
    print("B: you jump right")

    safe = input("-->  ").lower()
    if safe == "a":
        print("your ear was hit!")
        hp -= random.randint(10, 20)
        print("you have",hp,"hp!")

    elif safe == "b":
        print("you where hit!")
        print("your almost guaranteed too be brain damaged!")
        hp -= random.randint(85, 100)
        print("you have",hp,"hp!")
        hpCheck(hp)

    print("all the bodyguards jumped in and you came out somehow alive")
    print("do you want to execute the assasin")
    print("1: yes ")
    print("2: no")


    kill = input("--> ")
    if kill == "1":
        print("one of your bodyguard tried to kill him")
        print("mission failed")
        again = input("do you want to try again? yes -- no -->" )
        if again == "yes":
            print("you manged to kill him mission compleated")
            print("you go back stage and try to recover")
            print("three guys in skimask come out and hold you hostage")
            print("they are telling you to not resist and if you do your going to get it")
        
            resist = input("do you want to resist and try to ascape?yes or no?--> ")
    
            if resist == "yes":
                print("you have tried and got you hands free")
                fight = input("do you want to fight them?-->" )
                if fight == "yes":
                    combat()
            elif resist == "no": 
                print("you are getting blindfolded and wrapped, you are getting shipped to a unknown place")
                print("you fell asleep..")
                print(".")
                print("..")
                print("...")
                print("you are getting woken up by a loud voice, and banging on the car door")
                print("someone grabbed you and lifted you on their shoulder")
                print("you are getting carried too some place!")
                print("you here a radio that are saying")
                print("The president are getting kidnapped and if someone find him and deliver him alive reward of 9 000$")

                
        if again == "no":
            print("you didn't do anything to stop him")
            print("but he is after you and he offer you to fight like real man")
            sniper = input("do you want to fight him-->  ")
            if sniper == "yes":
                enemyhp = 75
            
                combat()

            elif sniper == "no":
                print("you are a pussy")
                print("he pulled out a gun and you where shot!")
                    

    elif kill == "2":
        print("you let him live")
        print("more damge was done and more people died...")
        print("you failed end game!")
        
        