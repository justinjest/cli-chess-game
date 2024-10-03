# This is the place where a full turn lives
# a turn is defined by printing the current players turn
# accepting an input in the form of (a,b) (x,y) which will move the piece at (a,b) to (x,y)
# We are not currently validating that moves are correct
# We then reender the next board
import re

# TODO: Make sure you can only move pieces of the color of the current player's turn

def turn(board, player):
    new_board = board
    move = move_validation(new_board, player)
    # This should print a piece if it's a valid move
    new_board[move[1]] = new_board[move[0]]
    new_board[move[0]] = ''
    return new_board

def move_validation(board, player):
    move = ""
    while move == "":
        tmp = input_validation()
        move = translate_move(board, tmp)
    # This calls the coords of the piece you are moving move[0] is the starting position move[1] is the ending position
    starting_pos = (move[0][0], move[0][1])
    ending_pos = (move[1][0], move[1][1])
    # If the starting_pos has a piece validate it's a valid movement for that piece
    if board[starting_pos] != "":
        if player.white == board[starting_pos].white:
            ending_move = piece_validation(ending_pos, board[starting_pos], board)
            return(starting_pos,ending_move)
        else:
            print("Whoops, that's the wrong colored piece!")
    else: 
        return move_validation(board, player)
    
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
    # TODO add capture notation Rxh7
    # TODO add pawn notation (e7) instead of (pe7)

    move_validation_regex = re.compile(r'[rqpnkb][a-h][1-8]')
    if not move_validation_regex.match(move):
        print("That isn't on the board, please try again")
        input_validation()
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
    print(moves)
    # If two similiar pieces can move to the same square, we need to clarify which one we are looking at
    if len(moves) > 1:
        validated = ""
        print("There are multiple pieces that could move there. Please provide the coordinates you want to move from")
        while validated == "":
            coords = input()
            for i in moves:
                if coords == str(i[0]):
                    print("Okay!")
                    validated = i[0]
                    break
            else: 
                print("That isn't a valid starting point. Please ensure you enter the full coordinate (x, y).")
                print("You can see the possible starting moves below")
                for i in moves:
                    print(i[0], end = '')
                print ()
        # TODO: Check to make sure the originating piece is actually at this location
        return(validated, moves[0][1])
    elif len(moves) == 0:
        print("No valid moves found")
        return ""
    # If there is only one option, we just return the move
    else:
        return (moves[0][0], moves[0][1])
    
                
