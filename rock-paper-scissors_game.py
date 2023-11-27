# print starting game 
# ask the user to enter his choice rock, paper or scissors
# computer choose random
# compare user choice with computer choice if the same print it is atie
# check user choice 
# if user enter paper and compter rock or user = rock and computer  =scissors or user= scissors and computer =paper
# user won
# else user lose
import random

while True:
    print("Starting Game!")

    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    pc_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"User choice: {user_choice}")
    print(f"Computer choice: {pc_choice}")

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Wrong choice, try again!")
    elif user_choice == pc_choice:
        print("It's a Tie")
    elif (
        (user_choice == 'paper' and pc_choice == 'rock') or
        (user_choice == 'rock' and pc_choice == 'scissors') or
        (user_choice == 'scissors' and pc_choice == 'paper')
    ):
        print("Congratulations! You won!")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break