import random
import time

print("\t \t \t Rock \t Paper \t Scissors \t Game \t \t \t")
play = (input('Type "Play" to start.\n'))

if play=="Play":
    print("Loading...")
    time.sleep(3.5)
else:
    time.sleep(3.5)
    print("Invalid Input. \n Game Exiting.")
    exit()

def game(PointsYou, PointsComp):
    print("Choose your option:")
    print("(R) Rock")
    print("(P) Paper")
    print("(S) Scissors")
    Computer = random.choice([1, 0, -1])
    youStr = input("Enter Your Choice: ")
    youDict = {"R": 1, "P": 0, "S": -1}
    reverseDict = {1: "Rock", 0: "Paper", -1: "Scissors"}
    you = youDict[youStr]
    print(f"You Chose {youStr} \n The Computer chose {reverseDict[Computer]}")
    
    if Computer == you:
        print("It's a draw.")
    elif Computer==1 and you==0:
        print("You Won.")
        PointsYou += 1
    elif Computer==0 and you==-1:
        print("You Won.")
        PointsYou += 1
    elif Computer==-1 and you==1:
        print("You Won")
        PointsYou += 1
    elif Computer==0 and you==1:
        print("You Lost.")
        PointsComp += 1
    elif Computer==-1 and you==0:
        print("You Lost.")
        PointsComp += 1
    elif Computer==1 and you==-1:
        print("You Lost.")
        PointsComp += 1
    
    return PointsYou, PointsComp

elements = int(input("Choose for how many points you want to play for: "))
PointsYou = 0
PointsComp = 0
for i in range(elements):
    PointsYou, PointsComp = game(PointsYou, PointsComp)
if PointsYou > PointsComp:
    print("You won and successfully finished the entire game.")
else:
    print("You lost and the game was finished.")
    retry = input("Want a Retry?\n Press R or any other key to exit. ")
    if retry == "R":
        game(PointsYou, PointsComp)
