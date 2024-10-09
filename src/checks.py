
def get_white_checks(board):
    moves = []
    for square in board.values():
        if square != "" and square.symbol != "k":
            if square.white:
                moves.append([square.symbol, square.is_move_valid(board), (square.x, square.y)])
    return moves

def get_black_checks(board):
    moves = []
    for square in board.values():
        if square != "" and square.symbol != "k":
            if not square.white:
                moves.append([square.symbol, square.is_move_valid(board), (square.x, square.y)])
    return moves