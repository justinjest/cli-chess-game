# This is the place where a full turn lives
# a turn is defined by printing the current players turn
# accepting an input in the form of (a,b) (x,y) which will move the piece at (a,b) to (x,y)
# We are not currently validating that moves are correct
# We then reender the next board
import re

def turn(board):
    new_board = board
    move = move_validation(new_board)
    # This should print a piece if it's a valid move
    new_board[move[1]] = new_board[move[0]]
    new_board[move[0]] = ''
    return new_board

def move_validation(board):
    move = input_validation()
    starting_pos = (int(move[1]),int(move[3]))
    ending_pos = (int(move[6]),int(move[8]))
    if board[starting_pos] != "":
        print ("valid move")
        return(starting_pos,ending_pos)
    else:
        print("no piece there! Try again")
        return move_validation(board)

def input_validation():
    move = input("Please enter your move in the form of (a,b)(x,y) ")
    # Make sure the move they entered is the correct format
    move_validation_regex = re.compile(r'\([0-7],[0-7]\)\([0-7],[0-7]\)')
    if not move_validation_regex.match(move):
        print("That isn't on the board, please try again")
        input_validation
    return move
