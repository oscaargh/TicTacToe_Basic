from Functions_for_Tic_Tac_Toe import check_game_state

matrix = [[" "," "," "],[" "," "," "],[" "," "," "]]

def print_board(matrix):
    print("---------")
    for row in matrix:
        print("|", " ".join(row), "|")
    print("---------")

print_board(matrix)

current_player = "X"

while True:
    try:
        row, col = map(int, input(f"Type the coordinates that you wish to append {current_player} to! eg. '1 2' for (1, 2): ").split())
        user_move = [row, col]
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        elif matrix[row - 1][col - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
    except (TypeError, ValueError):
        print("You should enter numbers!")
        continue
    else:
        matrix[row - 1][col - 1] = current_player
        playing_field = [cell for row in matrix for cell in row]
        result = check_game_state(playing_field)
        print_board(matrix)
        if result in("O wins", "X wins", "Draw", "Impossible"):
            print(result)
            break
        current_player = "O" if current_player == "X" else "X"
