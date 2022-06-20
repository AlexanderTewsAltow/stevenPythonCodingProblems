##################################################################
# Mastermind is a game where the player has to guess a 4-digit
# number. The computer will then give a hint about the number of
# correct digits in the correct position.

from enum import Enum
from random import randint

class Color(Enum):
    R = 1   # Red
    G = 2   # Green
    B = 3   # Blue
    P = 4   # Purple
    W = 5   # White

    @staticmethod
    def get_color(color):
        if color == "R":
            return Color.R
        elif color == "G":
            return Color.G
        elif color == "B":
            return Color.B
        elif color == "P":
            return Color.P
        elif color == "W":
            return Color.W
        else:
            return None

class Game():
    def __init__(self):
        # initilize game
        self.secret_code = self.generate_secret_number()
        self.guess_count = 0
        self.guess_limit = 10
        self.guess_list = []
        self.game_won = False
        game_won = False
        # start game
        self.next_guess()

    def generate_secret_number(self):
        return [Color(randint(1, 5)) for _ in range(4)]
    
    def next_guess(self):
        if (self.guess_count >= self.guess_limit):
            return self.game_over()
        guessInput = input("Guess #{} of {}: ".format(self.guess_count, self.guess_limit))
        if len(guessInput) != 4:
            print("Invalid input. Please enter a 4-digit code.")
            return self.next_guess()
        self.guess_count += 1
        self.guess_list.append(self.guess_input_to_number(guessInput))

        # check how many colors are correct in the correct position
        correct_position = 0
        correct_color = 0
        check_color_positions = []
        guess_copy = self.guess_list[-1]
        # check red (correct color && correct position)
        for i in range(4):
            # check if the color is correct in the correct position
            if (self.guess_list[-1][i] == self.secret_code[i]):
                correct_position += 1
                guess_copy[i] = None
            else:
                check_color_positions.append(i)
        # check white (correct color && not correct position)
        for i in check_color_positions:
            if self.secret_code[i] in guess_copy:
                guess_copy[i] = None
                correct_color += 1

        if (correct_position == 4):
            self.game_won = True
            return self.game_over()

        print("You have {} red and {} white.".format(correct_position, correct_color))

        self.next_guess()
    
    def guess_input_to_number(self, guessInput):
        return [Color.get_color(c.capitalize()) for c in guessInput]
    
    def game_over(self):
        if self.game_won:
            print("You guessed it in {} moves!".format(self.guess_count))
        else:
            print("You loose! My secret code was: {}".format("".join([c.name for c in self.secret_code])))

class GameController():
    def __init__(self) -> None:
        self.player_wins = 0
        self.computer_win = 0
        self.rounds = 1
        self.game = None
        # ask for the number of rounds
        while True:
            try:
                self.rounds = int(input("How many rounds do you want to play? "))
                break
            except ValueError:
                print("Please enter a number.")
        # start the game
        self.start_game()
    
    def start_game(self):
        # print available colors
        print("Available colors: R, G, B, P, W")
        while True:
            print("\nRound {}\n".format(self.player_wins + self.computer_win + 1))
            
            self.game = Game()
            if self.game.game_won:
                self.player_wins += 1
            else:
                self.computer_win += 1
            
            self.print_score()

            if self.computer_win + self.player_wins == self.rounds:
                exit(0)
        
    def print_score(self):
        print("Score:")
        print("\tPlayer: {}".format(self.player_wins))
        print("\tComputer: {}".format(self.computer_win))

if __name__ == "__main__":
    game = GameController()