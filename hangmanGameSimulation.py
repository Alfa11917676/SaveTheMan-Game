import random
def hanged():
    legitWords=random.choice(["Sherlock","BreakingBad","Dark","MoneyHeist","Patallok","Umbrella Acedemy","Narcos","GameOfThrones","BabySitter","Friends","WalkingDead","The100","Ratched","Lucifer","SacredGames","Betal","SHE","DelhiCrime","TheHauntingOfHillHOuse","BossBaby","RickAndMorty","BardOfBlood","LittleThings","Ghoul","Leila","YOU","13ReasonsWhy","SexEducation","TheDeathNote","OnePunchMan","Naruto","AttackOnTitans","DragonBallZ","Pokemon",])
    validleters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQERSTUVWXYZ1234567890"
    turns=10
    guessMade=""

    while len(legitWords)>0:
        main=""
        missed=0

        for letter in legitWords:
            if letter in guessMade:
                main=main+letter
            else:
                main=main+"_"+" "

        if main==legitWords:
                print(main)
                print("You Win")
                print("            ")
                print("|           ")
                print("|          ")
                print("|        O -->ahh!!Thank you %s for saving my life"%userInput)
                print("|       \|/     ")
                print("|        |  ")
                print("|    ___/|\_______")
                break

        print("Guess the letter",main)
        guess=input()

        if guess in validleters:
            guessMade=guessMade+guess
        else:
            print("Enter a valid character")
            guess=input()
        if guess not  in legitWords:
            turns=turns-1
            if turns==9:
                    print("Only 9 chances left")
                    print(" ----------  ")
            if turns==8:
                    print("Only 8 turns left")
                    print(" ----------  ")
                    print("|")
                    print("|")
                    print("|")
            if turns==7:
                print("Only 7 turns left")
                print(" ----------  ")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
            if turns==6:
                print("Only 6 turns left")
                print(" ----------  ")
                print("|        |")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
            if turns==5:
                print("Only 5 turns left")
                print(" ----------  ")
                print("|        |")
                print("|--------O")
                print("|")
                print("|")
                print("|")
                print("|")
            if turns == 4:
                print("Only 4 turns left")
                print(" ----------  ")
                print("|        |")
                print("|--------O")
                print("|       \|/")
                print("|        |")
                print("|")
                print("|")
            if turns == 3:
                print("Only 3 turns left")
                print(" ----------  ")
                print("|        |")
                print("|--------O")
                print("|       \|/")
                print("|        |")
                print("|       /|\ ")
                print("|")
            if turns == 2:
                print("Only 2 turns left")
                print(" ----------  ")
                print("|        |  ")
                print("|--------O  ")
                print("|       \|/")
                print("|        |")
                print("|       /|\ ")
                print("|    __________")
            if turns==1:
                print("Only last turn left")
                print(" ----------  ")
                print("|        |  ")
                print("|---     O  -->%s please save me!!!Its your last chance"%userInput)
                print("|       \|/")
                print("|        |")
                print("|       /|\ ")
                print("|    __________")
            if turns==0:
                print("You failed to save him..Such a shame!!!")
                print(" ----------  ")
                print("|        |  ")
                print("|        O -->%s such a disgrace you are!!! ")
                print("|           ")
                print("|       \|/")
                print("|        |")
                print("|    ___/|\_______")
                print("The Webseries was ",legitWords)
                break
import time
userInput=input("Enter Your Name Hero")
print("Welcome %s to the DON'T HANG THE MAN"%userInput)
print("---------------------------------")
inn=input("If you know about the game press 'Y' else press anything ")
if(inn=='Y' or inn=='y'):
    print("Try to guess the word in 10 chances")
    print("The Name will be a some famous webseries")
    print("Your game will start in 10 sec get ready!!!")
    time.sleep(10)
else:
    print("This game is about saving a from being hanged.")
    print("You have guess each letter of the webseries. The letter can be anything from beginning, end or middle.")
    print("You will be given 10 chances to guess the name, after that the man will be hanged.")
    print("The Name will be a some famous webseries")
    print("Your game will start in 10 sec get ready!!!")
    time.sleep(10)
hanged()