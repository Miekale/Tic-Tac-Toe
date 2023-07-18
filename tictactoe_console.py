import numpy as np
import random
import os

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


#clear output function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#choose which person goes first
def start_player(player):
    if random.getrandbits(1) == False:
        return "X"
    else:
        return "O"

#player input
def get_input(player):
    print(f'Which row and column to put the {player}')
    x = input()
    y = input()
    try:
        x = int(x)
        y = int(y)
    except:
        print("Number entered is not an integer")
        return None, None
    if x > 3 or y > 3 or x < 1 or y < 1:
        print("Row or column out of range")
        return None, None
    if board[y - 1 ,x -1 ] != " ":
        print("This space is already occupied")
        return None, None
    return x - 1 , y -1  


def modify_board(board, row, column, player):
    board[row, column] = player

#checking for winning condition or tie conditon
def is_winner(board, win_conditions):
    for solution in win_conditions:
        board[solution[0]]
        if (board[solution[0,0], solution[0,1]] == board[solution[1, 0], solution[1, 1]] == board[solution[2, 0], solution[2, 1]] 
            and board[solution[0,0], solution[0,1]] != " "):
            return True
    return False

def is_tie(board):
    isfull = False
    for row in board:
        for space in row:
            if space == " ":
                return False
    return True


#Switch player
def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

#main program

current_player = start_player(current_player)

while winner == None:
    cls()
    
    print_board(board)  

    column = None
    row = None

    while column == None or row == None:
        column, row = get_input(current_player)

    modify_board(board, row, column, current_player)

    if is_winner(board, win_conditions):
        cls()
        print_board(board)
        print(f'{current_player} Wins!!')
        winner = "true"
    elif is_tie(board):
        cls()
        print_board(board)
        print("Tie game")
        winner = "tie"
    else:
        current_player = switch_player(current_player)

    
