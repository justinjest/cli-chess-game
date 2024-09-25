from pieces import *


def name_column(col_num):
    replacement = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h'
    }

    return replacement[col_num]

def draw_board(board):
    spacer = " _"
    for i in range(0, 8):
        print (spacer, end = "")
    print ("")
    for y in range(7, -1, -1):
        for x in range (0, 8):
            draw_square(x, y, board)
        print ("")

def draw_square(x, y, board):
    piece = "_"
    piece_symbols = ["p",
              "b",
              "n",
              "r",
              "q",
              "k"]
    tmp = board[f"{name_column(x)}{y+1}"] 
    if isinstance(tmp, Piece):
        piece = tmp.symbol
    if x < 7:
        print (f"|{piece}", end = "")
    if x == 7:
        print(f"|{piece}|", end = "")
        

