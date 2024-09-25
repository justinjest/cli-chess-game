def create_board():
    board = {}
    for x in range (0,8):
        for y in range (0, 8):
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
    for x in range(0, 8):
        for y in range (0, 8):
            print ("""|   |
                   |    |
                   _____""")
            
create_board()