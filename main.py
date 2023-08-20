import os
from game_info import board, board_matrix, potential_moves, past_moves

# 1. Draw the board
# 2. Prompt the players for input
# 3. Redraw the game board
# 4. Check for the end of the game
# 5. Loop through the previous 3 steps
# 6. Declare the winner and end the game


def main():
    move_number = 1
    while True:
        if move_number % 2 == 0:
            player = "O"
        else:
            player = "X"
        new_board = draw_board(board, board_matrix)
        print(new_board)
        prompt_for_move(board_matrix, potential_moves, player, past_moves)
        winner = check_for_winner(board_matrix, player)
        if winner or move_number == 9:
            declare_winner(winner)
            return
        move_number += 1


def draw_board(board, board_matrix):
    os.system("cls" if os.name == "nt" else "clear")
    new_board = ""
    idx = 0
    for char in board:
        if char.isdigit():
            char = board_matrix[idx]
            idx += 1
        new_board += char
    return new_board


def prompt_for_move(board_matrix, potential_moves, player, past_moves):
    while True:
        choice = input(f"It's your turn {player}! Pick a position: ")
        if choice not in potential_moves.keys():
            print("Please enter a valid value: ")
        elif choice in past_moves:
            print("That space has already been taken. Try again: ")
        else:
            move = potential_moves[choice]
            board_matrix[move] = player
            past_moves.append(choice)
            break


def check_for_winner(board_matrix, player):
    for i in range(3):
        if board_matrix[i] == board_matrix[i + 3] == board_matrix[i + 6]:
            return player
    for i in range(7, 3):
        if board_matrix[i] == board_matrix[i + 1] == board_matri[i + 2]:
            return player
    if board_matrix[0] == board_matrix[4] == board_matrix[8]:
        return player
    if board_matrix[2] == board_matrix[4] == board_matrix[6]:
        return player
    return False


def declare_winner(winner):
    if winner:
        print(f"Congratulations {winner}! Please come by again!")
    else:
        print("You two are very well matched!!! It's a tie!")


main()
