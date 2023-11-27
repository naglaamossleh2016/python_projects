# I asked chat gpt to run my code in rock-papper-scissors_game as oop code and here
# is the result documented

import random

class RockPaperScissorsGame:
    """A simple Rock, Paper, Scissors game.

    This class allows users to play the classic game of Rock, Paper, Scissors
    against the computer. The game can be played interactively, and the user
    can choose to play multiple rounds.

    Attributes:
        choices (list): A list containing the possible choices for the game,
                       which are 'rock', 'paper', and 'scissors'.
    """

    def __init__(self):
        """Initialize the RockPaperScissorsGame object."""
        self.choices = ['rock', 'paper', 'scissors']

    def start_game(self):
        """Start a round of the Rock, Paper, Scissors game.

        This method prompts the user to enter their choice and randomly selects
        the computer's choice. It then compares the choices and determines the
        winner or if it's a tie.

        Prints:
            User choice
            Computer choice
            Game result (Tie, win, or lose)
        """
        print("Starting Game!")

        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        pc_choice = random.choice(self.choices)

        print(f"User choice: {user_choice}")
        print(f"Computer choice: {pc_choice}")

        if user_choice not in self.choices:
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

    def play_again(self):
        """Ask the user if they want to play another round.

        Returns:
            bool: True if the user wants to play again, False otherwise.
        """
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'


#if __name__ == "__main__":
    # Create an instance of the RockPaperScissorsGame class
game = RockPaperScissorsGame()

    # Main game loop
while True:
      # Start a round of the game
    game.start_game()

    # Check if the user wants to play again
    if not game.play_again():
        print("Thanks for playing. Goodbye!")
        break
