import random
import time

PlayerWins = 0
CompWins = 0
RoundCount = 0

def RPS_rules(player, computer):
    if (player=="R" and computer=="S") or (player=="P" and computer=="R") or (player=="S" and computer=="P"):
        return True

Name = input("Hello there \U0001F600 , what is your name? - ")

Rounds = int (input(Name + ",how many rounds would you like to play? Choose either 3 or 5 - "))

if Rounds == 5:
    WinCount = 3
elif Rounds == 3:
    WinCount = 2

print("Great choice "+ Name + "! You have chosen to play "+ str(Rounds) + " rounds with the computer \U0001F525 \U0001F525")
print("Loading.....")
time.sleep(3)

while not RoundCount == Rounds:

    User_choice = input("Enter one of the following options;\n R for Rock\n P for Paper\n S for Scissors\n")
    Comp_Choice_Options = ["R","P", "S"]
    Comp_Choice =random.choice(Comp_Choice_Options)

    if User_choice == Comp_Choice:
        print ("This round is a draw!!- Computer picked "+ Comp_Choice + " as well")
        while User_choice == Comp_Choice:
            User_choice = input("Enter one of the following options;\n R for Rock\n P for Paper\n S for Scissors\n")
            Comp_Choice_Options = ["R","P", "S"]
            Comp_Choice =random.choice(Comp_Choice_Options)
    
    if RPS_rules(User_choice,Comp_Choice):
        print("Congratulations!! You have won this round; Computer selected "+ Comp_Choice)
        PlayerWins+=1

    
    if RPS_rules(User_choice,Comp_Choice)!=True:
        print("Oops, you have lost this round; Computer selected "+ Comp_Choice)
        CompWins+=1

    RoundCount+=1

print("Calculating the overall winner...")   
time.sleep(4)
if PlayerWins==WinCount:
    print("You have won the game!!! \U0001F917")
else:
    print("You have lost the game \U0001F622")

            

    

