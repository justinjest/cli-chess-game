# This is the place where a full turn lives
# a turn is defined by printing the current players turn
# accepting an input in the form of (a,b) (x,y) which will move the piece at (a,b) to (x,y)
# We are not currently validating that moves are correct
# We then reender the next board
import re
from board_logic import place_queens

def turn(board, player):
    new_board = board
    move = move_validation(new_board, player)
    if move != "O-O" and move != "O-O-O":
        if board[move[0]].symbol == 'k' or board[move[0]].symbol == 'r':
            board[move[0]].moved = True
        new_board[move[1]] = board[move[0]]
        new_board[move[1]].x = move[1][0]
        new_board[move[1]].y = move[1][1]
        new_board[move[0]] = ''
        # Check here to determine if game is over with new_board
    elif move == "O-O-O":
        if casteling_left_possible(board, player):
            if player.white:
                # White is casteling left
                new_board[2,0] = board[4,0]
                new_board[4,0] = ''
                # Move king left two
                new_board[3,0] = board[0,0]
                new_board[0,0] = ''
            if not player.white:
                # Black is casteling left
                new_board[2,7] = board[4,7]
                new_board[4,7] = ''
                # Move king left two
                new_board[3,7] = board[0,7]
                new_board[0,7] = ''
    elif move == "O-O":
        if casteling_right_possible(board, player):
            if player.white:
                # White is casteling left
                new_board[6,0] = board[4,0]
                new_board[4,0] = ''
                # Move king left two
                new_board[5,0] = board[7,0]
                new_board[7,0] = ''
            elif not player.white:
                # Black is casteling left
                new_board[6,7] = board[4,7]
                new_board[4,7] = ''
                # Move king left two
                new_board[5,7] = board[7,7]
                new_board[7,7] = ''

    # Return (new_board, game_over_flag)
    new_board = pawn_promotion(new_board)
    return new_board

def move_validation(board, player):
    move = ""
    while move == "":
        tmp = input_validation()
        if casteling_left_possible(board, player) and tmp == "O-O-O":
            return "O-O-O"
        elif casteling_right_possible(board,player) and tmp == "O-O":
            return "O-O"
        move = translate_move(board, tmp, player)
    # This calls the coords of the piece you are moving move[0] is the starting position move[1] is the ending position
    starting_pos = (move[0][0], move[0][1])
    ending_pos = (move[1][0], move[1][1])
    # If the starting_pos has a piece validate it's a valid movement for that piece
    if board[starting_pos] != "":
        if player.white == board[starting_pos].white:
            ending_move = piece_validation(ending_pos, board[starting_pos], board, player)
            return(starting_pos,ending_move)
        else:
            print("Whoops, that's the wrong colored piece!")
            return move_validation(board,player)
    else: 
        return move_validation(board, player)

def translate_move(board, move, player):
    # takes a move in form Ra8 and converts it to form (0,0)(0,8)
    # Breaks if there are no available moves and the game is not over
    if player.white:
        possible_moves = get_white_moves(board)
    elif not player.white:
        possible_moves = get_black_moves(board)
    moves = []
    for piece in possible_moves:
        if piece[0] == move[0].lower():
            second_letter = name_column(move[1])
            third_letter = int(move[2]) - 1
            for tuple in piece[1]:
                if (second_letter, third_letter) == tuple:
                    moves.append((piece[2], (second_letter, third_letter)))
    # If two similiar pieces can move to the same square, we need to clarify which one we are looking at
    if len(moves) > 1:
        validated = ""
        print(moves)
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
        return(validated, moves[0][1])
    elif len(moves) == 0:
        print("No valid moves found")
        return ""
    # If there is only one option, we just return the move unless it's a castle
    # Casteling we will record the kings final location, even though it's not stored in the valid moves section
    # And update the board
    else:
        return (moves[0][0], moves[0][1])
    
def piece_validation(dest, piece, board, player):
    if dest in piece.is_move_valid(board):
        return (dest)
    else:
        print ("Sorry! Can't make that move")
        return move_validation(board, player)
        
def get_all_moves(board):
    return get_white_moves(board) + get_black_moves(board)

def get_white_moves(board):
    moves = []
    for square in board.values():
        if square != "":
            if square.white:
                moves.append([square.symbol, square.is_move_valid(board), (square.x, square.y)])
    return moves

def get_black_moves(board):
    moves = []
    for square in board.values():
        if square != "":
            if not square.white:
                moves.append([square.symbol, square.is_move_valid(board), (square.x, square.y)]) 
    return moves

def input_validation():
    move = input("Please enter your move in the form of Rh7 ")
    # Make sure the move they entered is the correct format
    # TODO add capture notation Rxh7
    # TODO add pawn notation (e7) instead of (pe7)

    move_validation_regex = re.compile(r'[rqpnkb][a-h][1-8]')
    if move == "O-O" or move == "O-O-O":
        return move
    if not move_validation_regex.match(move):
        print("That isn't on the board, please try again")
        input_validation()
    return move

def casteling_left_possible(board, player):
    # Also known as long castle
    if player.white:
        if board[4,0] == '' or board[0,0] == '':
            return False
        # King moved somewhere, don't need to worry about it
        if board[4,0].symbol != 'k':
            return False
        if board[4,0].moved == True:
            return False
        if board[0,0].symbol != 'r':
            return False
        if board[0,0].moved == True:
            return False 
        if board[1,0] != '' or board[2,0] != '' or board[3,0] != '':
            # If the whole board is empty
            return False 
        return True 
    if not player.white:
        if board[4,7] == '' or board[0,7]=='':
            return False
        # King moved somewhere, don't need to worry about it
        if board[4,7].symbol != 'k':
            return False
        if board[4,7].moved == True:
            return False
        if board[0,7].symbol != 'r':
            return False
        if board[0,7].moved == True:
            return False 
        if board[1,7] != '' or board[2,7] != '' or board[3,7] != '':
            # If the whole board is empty
            return False 
        return True 
        
def casteling_right_possible(board, player):
    # Also known as short castle
    if player.white:
        if board[4,0] == '' or board [7,0] == '':
            return False
        # King moved somewhere, don't need to worry about it
        if board[4,0].symbol != 'k':
            return False
        if board[4,0].moved == True:
            return False
        if board[7,0].symbol != 'r':
            return False
        if board[7,0].moved == True:
            return False 
        if board[6,0] != '' or board[5,0] != '': 
            # If the whole board is empty
            return False 
        return True 
    if not player.white:
        if board[4,7] == '' or board[7,7] == '':
            return False
        # King moved somewhere, don't need to worry about it
        if board[4,7].symbol != 'k':
            return False
        if board[4,7].moved == True:
            return False
        if board[7,7].symbol != 'r':
            return False
        if board[7,7].moved == True:
            return False 
        if board[6,7] != '' or board[5,7] != '':
            # If the whole board is empty
            return False 
        return True 
            
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

# Board -> [0-2]
# interp. 0 game is not over
#         1 game is a draw
#         2 current player is winner
# TODO: Provides game over the turn after a king is in check
 
def is_game_over(board):
    checked_black = get_black_moves(board)
    checked_white = get_white_moves(board)
    for square in board.values():
            if square != "":
                if square.symbol == "k":
                    k_pos = (square.x, square.y)
                    color = square.white
                    if color:
                        for possible in checked_black:
                            if k_pos in possible[1]:
                                return 2
                            elif square.is_move_valid(board) == [] and len(checked_white) == 1:
                                return 1
                    if not color:
                        for possible in checked_white:
                            if k_pos in possible[1]:
                                return 2
                            elif square.is_move_valid(board) == [] and len(checked_black) == 1:
                                return 1
    return 0

def pawn_promotion(board):
    new_board = board
    for square in board.values():
        if square != "":
            if square.symbol == "p":
                if square.white == True:
                    if square.y == 7:
                        new_board = place_queens(board, square.x, square.y, True)
                        print(new_board)
                if square.white == False:
                    if square.y == 0:
                        new_board = place_queens(board, square.x, square.y, False)
                        print(new_board)
    return new_board
