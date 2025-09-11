winning_indices = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
    [0, 4, 8], [2, 4, 6], # Diagonals
    ]

def x_wins(a):
    for indices in winning_indices:
        if all(a[i] == "X" for i in indices): # Checks all the indices for three X's in a row for a given board "a"
            return True
    return False

def o_wins(a):
    for indices in winning_indices:
        if all(a[i] == "O" for i in indices): # Checks all the indices for three O's in a row for a given board "a"
            return True
    return False


def impossible(a):
    if o_wins(a) and x_wins(a): # Both can't win at the same time
        return True
    elif abs(a.count("X") - a.count("O")) >= 2: # The difference of X's and O's cannot be > 2
        return True
    return False

def game_not_finished(a):
    if " " in a and not x_wins(a) and not o_wins(a): # " " = empty spaces on the board, and x/o has not won yet
        return True
    return False

def draw(a):
    if not o_wins(a) and not x_wins(a) and not game_not_finished(a):
        return True
    return False

def check_game_state(a):
    if o_wins(a):
        return "O wins"
    elif x_wins(a):
        return  "X wins"
    elif draw(a):
        return "Draw"
    elif game_not_finished(a):
        return "Game not finished"
