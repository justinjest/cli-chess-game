def create_board():
    board = {}
    for y in range (7, -1, -1):
        for x in range (0, 8):
            board[f"{name_column(x)}{y + 1}"] = ""
    return (board)


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
    pieces = ["p",
              "b",
              "n",
              "r",
              "q",
              "k"]
    tmp = board[f"{name_column(x)}{y+1}"]
    if tmp in pieces:
        piece = tmp
    if x < 7:
        print (f"|{piece}", end = "")
    if x == 7:
        print(f"|{piece}|", end = "")
