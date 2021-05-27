#generate random paper, scissors, rock for computer
import random
#this is the randomiser for the program, chooses between paper, scissors, rock
psr = ("paper", "rock", "scissors")
program_choice = random.choice(psr)

#ask user for choice (paper/scissors/rock)
psr_choice=input("Paper,Scissors or Rock? (type paper/scissors/rock): ")

#this code is repeated for the other choices
#compare psr_choice with program_choice
if psr_choice == "paper":

#compares directly with the random program_choice if equal, will result in a draw
    if psr_choice == program_choice:
        print("It's a draw!")
#checks program_choice, if program_choice is rock, will result in win
    elif program_choice == "rock":
        print("You win!")
#directly check program_choice, if program_choice is scissors and you chose paper, you lose
    elif program_choice == "scissors":
        print("You lose!")
    
if psr_choice == "rock":
    if psr_choice == program_choice:
        print("It's a draw!")
    elif program_choice == "scissors":
        print("You win!")
    elif program_choice == "paper":
        print("You lose!")

if psr_choice == "scissors":
    if psr_choice == program_choice:
        print("It's a draw!")
    elif program_choice == "paper":
        print("You win!")
    elif program_choice == "rock":
        print("You lose!")
