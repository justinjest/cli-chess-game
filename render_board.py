from pieces import *

# TODO: render numbers and letters around edge of board
# TODO: update screen instead of redraw it



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
    tmp = board[(x,y)]
    piece = draw_piece(tmp)
    if x < 7:
        print (f"|{piece}", end = "")
    if x == 7:
        print(f"|{piece}|", end = "")
        

def draw_piece(piece):
    if isinstance(piece, Piece):
        if piece.white:
            return f'\033[0;30;47m{piece.symbol}\033[0;0m'
        return piece.symbol
    return "_"