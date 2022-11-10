# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

#from logic import make_empty_board
import logic


if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = 'O'
    while winner == None:
        #print("TODO: take a turn!")
        print ("'", player, sep = "", end = "' take your turn!\n")
        # TODO: Show the board to the user.
        logic.show_board(board)
        # TODO: Input a move from the player.
        pos = logic.move(board)
        # TODO: Update the board.
        logic.update_board(board, pos, player)
        #winner = 'X'  # FIXME
        winner = logic.get_winner(board)
        # TODO: Update who's turn it is.
        player = logic.other_player(player);

    if 'D' == winner:
        print ("It's draw.\n")
    else:
        print("'", winner, sep = "", end = "' wins!\n")
    logic.show_board(board)

    # TODO: Provide graphic interface for the game!
