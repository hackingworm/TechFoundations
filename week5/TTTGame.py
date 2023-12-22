# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from numpy import random

# Base class
class Player():
    def move(self, board):
        pass

    def is_bot(self):
        pass

# Extended class for human player
class HumanPlayer(Player):
    def move(self, board):
        # Specifies the row and column index of the cell to move in
        row = int(input()) - 1;
        col = int(input()) - 1;
        # Check if it's a valid move
        while 0 > row or 2 < row or 0 > col or 2 < col or None != board[row][col]:
            print ("Invalid move!")
            row = int(input()) - 1;
            col = int(input()) - 1;

        # Update the game board
        board[row][col] = self

    def is_bot(self):
        return False

# Extended class for bot player
class BotPlayer(Player):
    # Bot is a dummy player, it never try to win, but just follow the basic rule
    def move(self, board):
        while True:
            # Find a random cell to move in
            rnd = random.randint(8)
            row = int(rnd / 3)
            col = int(rnd % 3)
            # Check validity
            if None == board[row][col]:
                break

        board[row][col] = self

    def is_bot(self):
        return True

class Game:
    def __init__(self, O_player, X_player):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        self.winner = None
        self.O_player = O_player
        self.X_player = X_player
        self.current_player = O_player

    def show_board(self):
        for row in self.board:
            for player in row:
                if self.O_player == player:
                    print('O', end = '')
                elif self.X_player == player:
                    print('X', end = '')
                else:
                    # It's an empty cell
                    print('_', end = '')
            print()

    def check_line(self, first, second, third):
        if None == first:
            if None == second or None == third or second == third:
                return "continue"
            return "draw"

        if first == second and first == third:
            return "succeed"

        if first != second and None != second or first != third and None != third:
            return "draw"
        return "continue"

    def get_winner(self):
        result = "draw"

        # Check 3 "horizonal" lines
        for row in self.board:
            line_result = self.check_line(row[0], row[1], row[2])
            # if a winner found
            if "succeed" == line_result:
                self.winner = row[0]
                return "succeed"
            # if no winner till now but the game will go on
            if "continue" == line_result:
                result = "continue"

        # Check 3 "vertical" lines
        for col in range(3):
            line_result = self.check_line(self.board[0][col], self.board[1][col], self.board[2][col])
            if "succeed" == line_result:
                self.winner = self.board[0][col]
                return "succeed"
            if "continue" == line_result:
                result = "continue"

        # Check 2 "diagonal" lines
        line_result = self.check_line(self.board[0][0], self.board[1][1], self.board[2][2])
        if "succeed" == line_result:
            self.winner = self.board[0][0]
            return "succeed"
        if "continue" == line_result:
            result = "continue"

        line_result = self.check_line(self.board[0][2], self.board[1][1], self.board[2][0])
        if "succeed" == line_result:
            self.winner = self.board[0][2]
            return "succeed"
        if "continue" == line_result:
            result = "continue"

        return result

    def run(self):
        result = "continue"
        while "continue" == result:
            # If it's a human player, the show the game board and a prompt
            if not self.current_player.is_bot():
                self.show_board()
                print("Take ur turn!")
            self.current_player.move(self.board)
            # Switch turn
            if self.current_player == self.O_player:
                self.current_player = self.X_player
            else:
                self.current_player = self.O_player
            # Get winner
            result = self.get_winner()

        # Game over. Show the final game board and the winner or 'draw'
        self.show_board()
        if self.O_player == self.winner:
            print("O wins!")
        elif self.X_player == self.winner:
            print("X wins!")
        else:
            print("It draws.")

if __name__ == '__main__':
    print("Play with a bot?")
    answer = input()
    if 'y' == answer or 'Y' == answer:
        # Play with bot
        print("Play first?")
        answer = input()
        if 'y' == answer or 'Y' == answer:
            # U play first
            game = Game(HumanPlayer(), BotPlayer())
        else:
            # Bot plays first
            game = Game(BotPlayer(), HumanPlayer())
    else:
        # It's a human x human game
        game = Game(HumanPlayer(), HumanPlayer())

    # Game starts!
    game.run()
