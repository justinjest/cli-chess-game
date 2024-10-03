from render_board import *
from board_logic import *
from player import Player
from turn import *

def main():
    board = generate_ambigious_board(create_board())
    draw_board(board)
    game_loop_2_turns(board)

# This is here for before I created checkmate conditions
def game_loop_2_turns(board):
    game_over = False
    player = Player(True)
    player_code = {False: "black",
              True: "white"}
    while game_over == False:
        print (f"\r It is {player_code[player.white]}'s turn!")
        board = turn(board)
        draw_board(board)
        if not player.white:
            game_over = True
        player.white = not player.white


def game_loop(board):
    game_over = False
    player = Player(True)
    player_code = {False: "black",
              True: "white"}
    while game_over == False:
        print (f"It is {player_code[player.white]}'s turn!")
        board = turn(board)
        draw_board(board)
        for square in board.values():
            if square != "":
                if square.symbol == "k":
                    if square.is_move_valid(board) == []:
                        game_over = True
        player.white = not player.white
    # For some reason this program flips the turn after game over, this flips it back to clarify who won
    print (f"Game over! {player_code[not player.white]} won")

# This is placeholder to generate options in the future (Like connecting online)
def startup_message():
    init = input("would you like to play a game? y/n ")
    if init.lower() == "n":
        print ("Okay, have fun!")
        return False
    elif init.lower() == "y":
        print ("Great! Let's play!")
        return True
    else:
        print ("Sorry that's not y/n")
        startup_message()

if __name__ == "__main__":
    main()