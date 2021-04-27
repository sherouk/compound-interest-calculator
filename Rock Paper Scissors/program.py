# This program simulates a game of rock, paper, scissors
# between the user and the program

import random

# Generate a random computer choice from 1 to 3
def computer_choice():
    computerChoice = random.randint(1,3)
    if computerChoice == 1:
        computerChoice = "Rock"
    elif computerChoice == 2:
        computerChoice = "Paper"
    elif computerChoice == 3:
        computerChoice = "Scissors"
    return computerChoice

# Ask the user to input a choice from 1 to 3
def user_choice():
    userChoice = int(input("Enter 1 to choose rock, 2 to choose paper, and 3 to choose scissors: "))
    if userChoice == 1:
        userChoice = "Rock"
    elif userChoice == 2:
        userChoice = "Paper"
    elif userChoice == 3:
        userChoice = "Scissors"
    return userChoice

# Define the main module to determine the winner
def main():
    userChoice = user_choice()
    print("You chose", userChoice)

    computerChoice = computer_choice()
    print("The computer chose", computerChoice)

    # Determine the winners
    if userChoice == computerChoice:
        print("It's a tie!")
    elif userChoice == "Rock":
        if computerChoice == "Scissors":
            print("Rock smashes scissors. You win.")
        else:
            print("Paper covers rock. You lose.")
    elif userChoice == "Paper":
        if computerChoice == "Rock":
            print("Paper covers rock. You win.")
        else: 
            print("Scissors cuts paper. You lose.")
    elif userChoice == "Scissors":
        if computerChoice == "Paper":
            print("Scissors cuts paper. You win.")
        else:
            print("Rock smashes scissors. You lose.")
    
    #print("This program was written by Sherouk Omara")

# Call the main module
if __name__ == '__main__':
    main()
