# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def update_board(board, pos, player):
    board[pos[0]][pos[1]] = player

def show_board(board):
    for row in board:
        print (row)
        print()

def get_pos():
    x = int(input());
    y = int(input());
    return [x - 1, y - 1]

def move(board):
    # Specifies the x/y index of the cell to move in
    pos = get_pos()
    # The player can only move to "unoccupied" cells.
    while None != board[pos[0]][pos[1]] or 0 > pos[0] or 2 < pos[0] or 0 > pos[1] or 2 < pos[1]:
        print ("Invalid move!")
        pos = get_pos()

    return pos

def other_player(player):
    """Given the character for a player, returns the other player."""
    #return "O"  # FIXME
    if 'O' == player:
        return 'X'
    if 'X' == player:
        return 'O'

def check_line(first, second, third):
    if None == first:
        if None == second or None == third or second == third:
            return None
        return 'D'

    if first == second and first == third:
        return first
    if other_player(first) == second or other_player(first) == third:
        return 'D'
    return None

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', 'D' which means it ties and game is
        over or None, which means the game will go on."""

    result = 'D'

    # Check 3 "horizonal" lines
    row = 0
    while row < 3:
        line_result = check_line(board[row][0], board[row][1], board[row][2])
        # if a winner found
        if 'O' == line_result or 'X' == line_result:
            return line_result
        # if no winner till now but the game will go on
        if None == line_result:
            result = None
        row += 1

    # Check 3 "vertical" lines
    col = 0
    while col < 3:
        line_result = check_line(board[0][col], board[1][col], board[2][col])
        if 'O' == line_result or 'X' == line_result:
            return line_result
        if None == line_result:
            result = None
        col += 1

    # Check 2 "diagonal" lines
    line_result = check_line(board[0][0], board[1][1], board[2][2])
    if 'O' == line_result or 'X' == line_result:
        return line_result
    if None == line_result:
        result = None

    line_result = check_line(board[0][2], board[1][1], board[2][0])
    if 'O' == line_result or 'X' == line_result:
        return line_result
    if None == line_result:
        result = None
    return result
