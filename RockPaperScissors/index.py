import random 

player_input = input("Enter Your Choice. Rock, Paper, Scissors: ")

options = ["Rock", "Paper", "Scissors"]
computer_pick = random.choice(options)

if player_input == computer_pick:
    print("It's a tie! Both player's selected " + player_input) 
elif player_input == "Rock" and computer_pick == "Scissors":
    print("Congratulations! You won!")
    if computer_pick == "Rock" and player_input == "Scissors":
        print("You Lose!")
elif player_input == "Scissors" and computer_pick == "Paper":
    print("Congratulations! You won!")
    if computer_pick == "Scissors" and player_input == "Paper":
        print("You Lose!")
elif player_input == "Paper" and computer_pick == "Rock":
    print("Congratulations! You won!")
    if computer_pick == "Paper" and player_input == "Rock":
        print("You Lose!")

# Adding Replay Functionality