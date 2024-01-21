import random
from collections import Counter

moveList = ["rock","paper","scissor"]

donePlayerMoves = ["rock"]

def likelyMove():
    computer = winDictPlayer[recurringItemsMax]

def maxFinder():
    global counter,recurringItems,recurringItemsMax
    counter = Counter(donePlayerMoves)
    recurringItems = counter.most_common()
    return recurringItems

def maxFinderSingle():
    global recurringItems,recurringItemsMax
    recurringItemsMax = recurringItems[0][0]

points = 0
plPoints = 0

def gameLoop():
    global points,plPoints,donePlayerMoves
    maxFinder()

#    print(recurringItems)
#    print(donePlayerMoves)

    player = input("Your Move [rock, paper or scissor] : ")
    donePlayerMoves.append(player)

    computer = random.choice(moveList)

    if player == "exit".lower():
        print("exiting..")
        exit()

    if player.lower() in moveList:
        print("Computer's Move : ", computer,"\n")

    winDictPlayer = {"rock":"paper",
    "paper":"scissor",
    "scissor":"rock"}
    #declaration of wins variable
    try:
        winningMove = winDictPlayer[player]
    except KeyError:
        print("\n! Please make sure that it is either `rock`,`paper` or `scissor`")
        exit()

    if computer == winningMove:
        points = points+1
        print("Computer's Points :",points)
    else:
        points = points
        print("Computer's Points :",points)

    #comp wins variable

    winDictCp = {"paper":"rock",
    "scissor":"paper",
    "rock":"scissor"}

    winningMoveCp = winDictCp[player]
    if computer == winningMoveCp:
        plPoints = plPoints+1
        print("Player's Points :",plPoints,"\n")
    else:
        plPoints = plPoints
        print("Player's Points :",plPoints,"\n")

    maxFinderSingle()
#    print(recurringItemsMax)
while True:
    gameLoop()
