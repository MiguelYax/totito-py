
#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

import random

s = '   '

board = [[s, s, s],
         [s, s, s],
         [s, s, s]]

icon = ['X', 'O']


def check_winner(x, y):
    value = board[x][y]
    # check row
    if board[x][0] == value and board[x][1] == value and board[x][2] == value:
        return True
    # check column
    if board[0][y] == value and board[1][y] == value and board[2][y] == value:
        return True
    # check diagonal \
    if board[0][0] == value and board[1][1] == value and board[2][2] == value:
        return True
    # check another diagonal /
    if board[0][2] == value and board[1][1] == value and board[2][0] == value:
        return True

    return False


def get_random_move(value):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    p = s
    while p == s:
        if board[x][y] == s:
            board[x][y] = " " + value + " "
            p = value
        else:
            # TODO: prevent infinite loop
            x = random.randint(0, 2)
            y = random.randint(0, 2)

    return x, y


def print_board():
    for x in range(3):
        if x != 0:
            print('───┼───┼───')
        print(board[x][0] + "│"+board[x][1]+"│"+board[x][2])


win = False
move = 0
player = ''

while win == False and move <= 10:
    player = icon[move % 2]
    x, y = get_random_move(player)
    # check who win the game after 5 moves.
    if move > 4:
        win = check_winner(x, y)
    # print_board()
    move += 1

print_board()

if move > 9:
    print("Draw Game!")
else:
    print(player + ' Win the Game!')
