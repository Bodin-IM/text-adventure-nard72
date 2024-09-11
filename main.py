import random

def hpCheck():
    global hp
    if hp <= 0:
        print("you died..")
        quit()

hp = 100


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
    hpCheck()


print("all the bodyguards jumped in and you came out somehow alive")
print("do you want to execute the assasin")
print("1: yes ")
print("2: no")


kill = input("--> ")
if kill == "1":
    print("one of your bodyguard tried to kill him")
    print("mission failed")

elif kill == "2":
    print("you let him live")
    print("more damge was done and more people died...")




if kill == "1":
    again = input("do you want to try again? yes -- no -->" )
    if again == "yes":
        print("you manged to kill him mission compleated")
    if again == "no":
        print("he did more damage and more people was killed.")


if again == "yes":
    print("you go back stage and try to recover")
    print("three guys in skimask come out and hold you hostage")
    print("they are telling you to not resist and if you do your going to get it")
    input("do you want to resist and try to ascape?--> ")







    






