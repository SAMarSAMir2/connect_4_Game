# This progam is connect of 4 game
# by Samar Samir

import numpy as np

row_count = 6
column_count = 7
# the board
def create_board():
    board = np.zeros((row_count,column_count))
    return board
board = create_board()
print(board)

# checking to make sure that column has an empty slot
def valid_locatin(board,cal):
    return board[row_count-1][cal] ==0
#checking to see which row if the piece will fall on
def open_row(board,cal):
    for r in range(row_count):
        if board[r][cal-1] ==0:
            return r

def drop_piece(board,row,cal,piece):
    board[row][cal-1] = piece

# to change direction up side down
def new_board(board):
    print(np.flip(board,0))

def winning(board,piece):
    # check horizontal locations for win
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece :
                return True

    # check vertical locations for win
    for c in range(column_count):
        for r in range(row_count -3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece :
                return True

    # check positively sloped diagonals
    for c in range(column_count -3):
        for r in range(row_count -3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece :
                return True

    # check negatively sloped diagonals
    for c in range(column_count -3):
        for r in range(3 , row_count):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece :
                return True


game_over = False
turn = 0      # differentiate between its player 1 or player 2 is turn so i define the variable turn
while not game_over:
    # continue playing
    # Ask Player 1 input
    if turn == 0 :
        col = int(input("Player 1 make your selection (1 - 7) : "))
        if col > 7 :
            print("not valied")
            col = int(input("Player 1 make your selection (1 - 7) : "))
        if valid_locatin(board,col-1):
            row = open_row(board,col)
            drop_piece(board,row,col,1)
            if winning(board,1):
                print(" Player 1 is win ")
                game_over = True
    # Ask Player 2 input
    else:
        col = int(input("Player 2 make your selection (1 - 7) : "))
        if col > 7 :
            print("not valied")
            col = int(input("Player 2 make your selection (1 - 7) : "))
        if valid_locatin(board,col-1):
            row = open_row(board,col)
            drop_piece(board,row,col,2)
            if winning(board,2):
                print(" Player 2 is win ")
                game_over = True

    new_board(board)

    # alternating between my player 1 and player 2
    turn = (turn + 1) % 2



