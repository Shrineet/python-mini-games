 # Simple two-player Tic Tac Toe game

# Create a blank board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

# Function to check for winner
def check_winner(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Game loop
current_player = "X"

for turn in range(9):
    print_board()
    move = int(input(f"Player {current_player}, enter position (0-8): "))
    
    # Check if the cell is empty
    if board[move] == " ":
        board[move] = current_player
    else:
        print("That spot is already taken.")
        continue

    # Check winner
    if check_winner(current_player):
        print_board()
        print("Player", current_player, "wins!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"
else:
    print_board()
    print("It's a tie!")
