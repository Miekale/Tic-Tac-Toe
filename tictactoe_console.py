import numpy as np
import random

#make board
board = np.array([[" "," "," "], [" "," "," "], [" "," "," "]])
current_player = "X"
winner = None

win_conditions = np.array([[[0,0], [0,1], [0,2]],
                          [[1,0], [1,1], [1,2]],
                          [[2,0], [2,1], [2,2]],
                          [[0,0], [1,0], [2,0]],
                          [[0,1], [1,1], [2,1]],
                          [[0,2], [2,2], [2,2]],
                          [[0,0], [1,1], [2,2]],
                          [[2,0], [1,1], [0,2]]]
                        )

def print_board(board):
    line = "-+-+-"
    print(board[2,0] + "|" + board[2,1] + "|" + board[2,2])
    print(line)
    print(board[1,0] + "|" + board[1,1] + "|" + board[1,2])
    print(line)
    print(board[0, 0]+ "|" + board[0,1] + "|" + board[0,2])

#choose which person goes first

def start_player(player):
    if random.getrandbits(1) == False:
        player = "X"
    else:
        player = "Y"

#player input
def get_input(player):
    print(f'Which row and column to put the {player}')
    x = int(input())
    y = int(input())
    if x > 3 or y > 3 or x < 1 or y < 1:
        print("Row or column out of range")
        get_input(player)
    if board[x - 1 ,y -1 ] != " ":
        print("This space is already occupied")
        get_input
    return x - 1 , y -1  


def modify_board(board, row, column, player):
    board[row, column] = player

#checking for winning condition or tie conditon


def is_winner(board, win_conditions):
    for solution in win_conditions:
        if (board[solution[0,1]] == board[0 ,solution[1]] == board[0, solution[2]]):
            return True
    return False



#Switch player
def switch_player(player):
    if player == "X":
        player = "O"
    else:
        player = "X"

#main program

start_player(current_player)

while winner == None:
    print_board(board)
    row, column = get_input(current_player)
    modify_board(board, row, column, current_player)
    if is_winner(board, win_conditions):
        print(f'{current_player} Wins!!')
    else:
        switch_player(current_player)
