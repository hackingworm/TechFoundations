from typing import List


def tic_tac_toe(board: List[List[str]]) -> str:
    """Returns the winner for a given tic tac toe game.
    Args:
        board (List[List[str]]): Board configuration for which the result is to be determined.
    Raises:
        ValueError: Raised if no input is given.
        IndexError: Raised if the input board is not of dimensions 3x3.
        ValueError: Raised if the input has elements that are not 'X' or 'O'.
    Returns:
        str: String description of result of the game.
    """
    if not board:
        raise ValueError("No inputs given.")

    if len(board) != 3 or len(board[0]) != 3:
        raise IndexError("Board does not conform to the right dimensions of a 3x3 matrix.")

    if not all([element in ["X", "O"] for row in board for element in row]):
        raise ValueError("Board contains one or more entries that is neither 'X' nor 'O'.")

    winner = ""
    if board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
        return winner + " won"
    if board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
        return winner + " won"
    if board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
        return winner + " won"
    if board[0][0] == board[0][1] == board[0][2]:
        winner = board[0][0]
        return winner + " won"
    if board[1][1] == board[1][1] == board[1][2]:
        winner = board[1][1]
        return winner + " won"
    if board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
        return winner + " won"
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner + " won"
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return winner + " won"
    else:
        return "It was a draw"


b = [["O", "O", "X"], ["X", "O", "O"], ["X", "X", "X"]]

print(tic_tac_toe(b))
