#!/usr/bin/env python

global board

def print_board():
    """ Print to console the pieces positions."""
    print(board)

def next_move():
    """ Ask for the next move and read."""
    pass

def check_move():
    """ Verify if this is a valid move."""
    pass

def move_peice():
    """ Move piece """
    pass

# Inital empty board
board = [[0 for x in range(10)] for x in range(10)]

# Inital pieces
# player 1
board[0][0] = 1
board[0][2] = 1
board[0][4] = 1


print_board()
