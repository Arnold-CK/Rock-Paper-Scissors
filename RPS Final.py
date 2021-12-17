import random
import time

global PlayerWins
global RoundCount
global CompWins

PlayerWins = 0
CompWins = 0
RoundCount = 0

def getting_started():

    global Rounds

    Name = input("Hello there \U0001F600 , what is your name? - ")
    Rounds = int (input(Name + ",how many rounds would you like to play? Choose either 3 or 5 - "))
    print(f'Great choice {Name} ! You have chosen to play {str(Rounds)} rounds with the computer \U0001F525 \U0001F525')
    print("Loading.....")
    time.sleep(3)

def game_play(RoundCount,Rounds,PlayerWins,CompWins):

    global User_choice
    global Comp_Choice
    global final_computer
    global final_player

    while not RoundCount == Rounds:

        User_choice = input("Use one of the following options;\n R for Rock\n P for Paper\n S for Scissors\n")
        Comp_Choice_Options = ["R","P", "S"]
        Comp_Choice = random.choice(Comp_Choice_Options)

        while User_choice == Comp_Choice:
            print (f'This round is a draw!!- Computer picked {Comp_Choice} as well. You are going to select again')
            
            User_choice = input("Enter one of the following options;\n R for Rock\n P for Paper\n S for Scissors\n")
            Comp_Choice_Options = ["R","P", "S"]
            Comp_Choice =random.choice(Comp_Choice_Options)


        if (User_choice=="R" and Comp_Choice=="S") or (User_choice=="P" and Comp_Choice=="R") or (User_choice=="S" and Comp_Choice=="P"):
            print("Congratulations!! You have won this round; Computer selected "+ Comp_Choice)
            PlayerWins+=1
        else:
            print("Oops, you have lost this round; Computer selected "+ Comp_Choice)
            CompWins+=1
            

        RoundCount+=1

    final_player = PlayerWins
    final_computer = CompWins
    return final_computer, final_player
        

def wincount_declaration(Rounds):
    
    global WinCount

    if Rounds == 5:
        WinCount = 3
    elif Rounds == 3:
        WinCount = 2
    return WinCount

def overall_winner(final_player,final_computer,WinCount):
    # print("Calculating the overall winner...")   
    # time.sleep(4)
    if final_player == WinCount:
        return print("You have won the game!!! \U0001F917")
    elif final_computer == WinCount:
        return print("You have lost the game \U0001F622")


getting_started()
wincount_declaration(Rounds)
game_play(RoundCount,Rounds,PlayerWins,CompWins)
overall_winner(final_player,final_computer,WinCount)










            

    

