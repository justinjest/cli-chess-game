# This is the place where a full turn lives
# a turn is defined by printing the current players turn
# accepting an input in the form of (a,b) (x,y) which will move the piece at (a,b) to (x,y)
# We are not currently validating that moves are correct
# We then reender the next board
import re

# TODO: convert move into something akin to chess notation (r E7) etc

def turn(board):
    new_board = board
    move = move_validation(new_board)
    # This should print a piece if it's a valid move
    new_board[move[1]] = new_board[move[0]]
    new_board[move[0]] = ''
    return new_board

def move_validation(board):
    move = input_validation()
    move = translate_move(board, move)
    starting_pos = (move[0][0], move[0][1])
    ending_pos = (move[1][0], move[1][1])
    if board[starting_pos] != "":
        ending_move = piece_validation(ending_pos, board[starting_pos], board)
        return(starting_pos,ending_move)
    else:
        print("no piece there! Try again")
        move_validation(board)
    
def piece_validation(dest, piece, board):
    if dest in piece.is_move_valid(board):
        return (dest)
    else:
        print ("Sorry! Can't make that move")
        return move_validation(board)
        
def get_all_moves(board):
    moves = []
    for square in board.values():
        if square != "":
            moves.append([square.symbol, square.is_move_valid(board), (square.x, square.y)])
    
    return moves

def input_validation():
    move = input("Please enter your move in the form of Rh7 ")
    # Make sure the move they entered is the correct format
    move_validation_regex = re.compile(r'[rqpnkb][a-h][1-8]')
    if not move_validation_regex.match(move):
        print("That isn't on the board, please try again")
        input_validation
    return move

def name_column(col_num):
    replacement = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }

    return replacement[col_num]

def translate_move(board, move):
    # takes a move in form Ra8 and converts it to form (0,0)(0,8)
    all_moves = get_all_moves(board)
    moves = []
    for piece in all_moves:
        if piece[0] == move[0].lower():
            second_letter = name_column(move[1])
            third_letter = int(move[2]) - 1
            for tuple in piece[1]:
                if (second_letter, third_letter) == tuple:
                    moves.append((piece[2], (second_letter, third_letter)))
    
    if len(moves) > 1:
        print("There are multiple pieces that could move there. Please end the game")
        # TODO: Add handling here
        return
    return (moves[0][0], moves[0][1])
    
                
