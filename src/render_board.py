from pieces import *

# TODO: render numbers and letters around edge of board
# TODO: update screen instead of redraw it

def draw_board(board):
    # TODO: turn this into one long string so we can carriage return it
    spacer = " _"
    board_render = ""
    for i in range(0, 8):
        board_render += spacer
    board_render += "\n"
    for y in range(7, -1, -1):
        for x in range (0, 8):
            board_render += draw_square (x,y,board)
        board_render += "\n"
    print(board_render)

def draw_square(x, y, board):
    tmp = board[(x,y)]
    piece = draw_piece(tmp)
    if x < 7:
        return (f"|{piece}")
    if x == 7:
        return(f"|{piece}|")
        

def draw_piece(piece):
    if isinstance(piece, Piece):
        if piece.white:
            return f'\033[0;30;47m{piece.symbol}\033[0;0m'
        return piece.symbol
    return "_"