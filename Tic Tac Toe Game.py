# Tic Tac Toe Game (2 Player)
import random

def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    return move


def tic_tac_toe():
    board = [" " for _ in range(9)]
    human = "X"
    computer = "O"

    print("You are X, Computer is O")

    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:  # Human turn
            try:
                move = int(input("Choose position (1-9): ")) - 1
            except ValueError:
                print("Invalid input! Enter number 1-9.")
                continue

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue

            board[move] = human

            if check_winner(board, human):
                print_board(board)
                print("You win!")
                return

        else:  # Computer turn
            print("Computer is making a move...")
            move = computer_move(board)
            board[move] = computer

            if check_winner(board, computer):
                print_board(board)
                print("Computer wins!")
                return

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()