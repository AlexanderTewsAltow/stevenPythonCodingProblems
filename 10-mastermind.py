# Als erstes den Nutzer festlegen lassen welche/wie viele Farben/Buchstaben, Positionen es im Spiel geben soll und die Anzahl an Runden
# Von den genannten Buchstaben sucht sich der Computer die Anzahl an zu verwendenen Buchstaben raus und randomized sie zu einem String (4 Buchstaben/Faren -> BWWB, RGBW, ist halt random)
# Dann kann der Nutzer anfangen zu raten und gibt seinen Vorschlag ein, wenn eins der Buchstaben (Buchstabe[i] z.b Buchstabe[0] wäre beim beispiel BWWB B) gleich des vom Computergenerierten
# strings ist, dann erhöt sich die Anzahl der erhaltenen Blacks für den Zug, wenn einer der Buchstaben vorhanden ist aber nicht am richtigen Index, dann erhöt sich die Anzahl der erhaltenen Whites
# für den Zug, sobald len(blacks) == len(computergenertierterString) dann hat der Spieler gewonnen

import math
from random import randint
from turtle import pos, position


includedCharacters = input("Characters you want to use in the game (Format: A-B-C-D):")
if len(includedCharacters.split("-")) < 3:
    includedCharacters = input("Please enter at least 3 different characters:")

positionsInGame = int(input("Amount of positions you want to use:"))
rounds = int(input("Rounds:"))
curRound = 1

generatedCode = []
includedCharacters = includedCharacters.split("-")

def userGuess(curRound):
    blacks = 0
    whites = 0

    if curRound > rounds:
        print("You weren't able to guess the code! The code was:", generatedCode)
        return False
    x = input(f"ROUND {curRound} Give your guess, codebreaker:")

    if x.find("-") == False:
        x = input(f"ROUND {curRound} Please re-enter your guess using following format: A-B-C-D:")

    x = x.split("-")
    copyGenCode = generatedCode.copy()

    for i in range(positionsInGame):
        if x[i] == copyGenCode[i]:
            blacks += 1
            copyGenCode[i] = ""

    for i in range(positionsInGame):
        if x[i] in copyGenCode:
            copyGenCode.remove(x[i])
            whites += 1

    if blacks == len(generatedCode):
        print(f"You have won the game after {curRound} Round(s)!")
        return True

    print("You have",blacks,"blacks and",whites,"whites")
    curRound += 1
    userGuess(curRound)

for i in range(positionsInGame):
    generatedCode += includedCharacters[randint(0, positionsInGame-1)]

print("Please use following format for your guesses: A-B-C-D")
userGuess(curRound)
