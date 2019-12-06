#!/usr/bin/env python3

# developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from easygui import *
import random
import sys


dice1 = "./images/dice1.gif"
dice2 = "./images/dice2.gif"
dice3 = "./images/dice3.gif"
dice4 = "./images/dice4.gif"
dice5 = "./images/dice5.gif"
dice6 = "./images/dice6.gif"


def dice():
    inputNum = 6
    outputNum = list(range(inputNum + 1))
    outputNum.remove(0)

    numbers = random.shuffle(outputNum)

    top6 = outputNum[:1]

    if top6 == [1]:
        image = dice1
    elif top6 == [2]:
        image = dice2
    elif top6 == [3]:
        image = dice3
    elif top6 == [4]:
        image = dice4
    elif top6 == [5]:
        image = dice5
    else:
        image = dice6

    diceChoice = ["Replay", "Quit"]
    top6 = str(top6)
    top6 = top6.replace("[", "")
    top6 = top6.replace("]", "")
    replay = buttonbox(
        image=image,
        choices=diceChoice,
        title="Dice simulator",
        msg="Dice simualtor\n\nNumber on the dice : " + str(top6),
    )
    if replay == "Replay":
        dice()
    else:
        sys.exit(0)


logoDice = "./images/dice-full.gif"
msg = "Do you want to play ?"
choices = ["Yes", "No"]

begining = buttonbox(msg, image=logoDice, choices=choices)

if begining == "Yes":
    dice()
else:
    sys.exit(0)
