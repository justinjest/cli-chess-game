class Piece:
    # White is a boolean to represent white or black
    # White is True, black is False
    def __init__(self, white, x, y):
        self.white = white
        self.x = x
        self.y = y

class Pawn(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "p"
    # returns a list of valid moves
    def is_move_valid(self, board):
        # TODO: add capture logic
        # TODO: add en passant (HOW)
        valid_moves = []
        if self.white == True:
            if self.y == 1:
                if board[self.x, self.y + 1] == '':
                    valid_moves.append((self.x, self.y+1))
                if board[self.x, self.y + 2] == '':
                    valid_moves.append((self.x, self.y + 2))
            else:
                if board[self.x, self.y + 1] == '':
                    valid_moves.append((self.x, self.y + 1))
        else:
            if self.y == 6:
                if board[self.x, self.y - 1] == '':
                    valid_moves.append((self.x, self.y-1))
                if board[self.x, self.y - 2] == '':
                    valid_moves.append((self.x, self.y-2))
            else:
                if board[self.x, self.y - 1] == '':
                    valid_moves.append((self.x, self.y - 1))
        return (valid_moves)
        # TODO: Implement this for all pieces

class Rook(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1]) 
        self.symbol = "r"
    def is_move_valid(self, board):
        # TODO: Glitch in this where it does not render on screen when first attempt at move fails
        valid_moves = []
        # Check moves to the right
        for i in range (0,8):
            check_x = self.x + i
            # We can improve this by checking up, and then down allowing us to stop when we run into a piece
            if check_x in range (0,8):
                if board[(check_x, self.y)] == '':
                    valid_moves.append((check_x, self.y))
                else:
                    if board[(check_x, self.y)].white != self.white:
                        valid_moves.append((check_x, self.y)) 
        # check left
        for i in range (0, 8):
            check_x = self.x - i
            # We can improve this by checking up, and then down allowing us to stop when we run into a piece
            if check_x in range (0,8):
                if board[(check_x, self.y)] == '':
                    valid_moves.append((check_x, self.y))
                else:
                    if board[(check_x, self.y)].white != self.white:
                        valid_moves.append((check_x, self.y)) 
        # Check down
        for j in range (0,8):
            check_y = self.y - j
            if check_y in range (0,8):
                if board[(self.x, check_y)] == '':
                    valid_moves.append((self.x, check_y))
                else:
                    if board[(self.x, check_y)].white != self.white:
                        valid_moves.append((self.x, check_y))
        # Check up
        for j in range (0,8):
            check_y = self.y + j
            if check_y in range (0,8):
                if board[(self.x, check_y)] == '':
                    valid_moves.append((self.x, check_y))
                else:
                    if board[(self.x, check_y)].white != self.white:       
                        valid_moves.append((self.x, check_y))
        return valid_moves
    

class Knight(Piece):     
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "n"

class Bishop(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "b"
    
    def is_move_valid(self, board):
        # TODO: Glitch in this where it does not render on screen when first attempt at move fails
        valid_moves = []
        # Check moves to the right and up
        for i in range (0,8):
            check_x = self.x + i
            check_y = self.y + i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
            else:
                break
        # check left and up
        for i in range (0, 8):
            check_x = self.x - i
            check_y = self.y + i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
        # Check right and down
        for j in range (0,8):
            check_x = self.x + j
            check_y = self.y - j
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
            else:
                break
        # Check left and down
        for j in range (0,8):
            check_x = self.x - j
            check_y = self.y - j
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
            else:
                break
        return valid_moves

class Queen(Piece):
    def __init__(self, x_y_pair, white):    
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "q"
    def is_move_valid(self, board):
        # TODO: Glitch in this where it does not render on screen when first attempt at move fails
        valid_moves = []
        # Check moves to the right and up
        for i in range (1,8):
            check_x = self.x + i
            check_y = self.y + i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y))
                    break
                    
        # check left and up
        for i in range (1, 8):
            check_x = self.x - i
            check_y = self.y + i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
                    break
                    
        # Check right and down
        for i in range (1,8):
            check_x = self.x + i
            check_y = self.y - i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
                    break
                    
        # Check left and down
        for i in range (1,8):
            check_x = self.x - i
            check_y = self.y - i
            if check_x in range (0,8) and check_y in range (0,8):
                if board[(check_x, check_y)] == '':
                    valid_moves.append((check_x, check_y))
                else:
                    if board[(check_x, check_y)].white != self.white:
                        valid_moves.append((check_x, check_y)) 
                    break
                    
        # check right
        for i in range (1,8):
            check_x = self.x + i
            if check_x in range (0,8):
                if board[(check_x, self.y)] == '':
                    valid_moves.append((check_x, self.y))
                else:
                    if board[(check_x, self.y)].white != self.white:
                        valid_moves.append((check_x, self.y))
                    break
                    
        # check left
        for i in range (1, 8):
            check_x = self.x - i
            if check_x in range (0,8):
                if board[(check_x, self.y)] == '':
                    valid_moves.append((check_x, self.y))
                else:
                    if board[(check_x, self.y)].white != self.white:
                        valid_moves.append((check_x, self.y)) 
                    break
                    
        # Check down
        for j in range (1,8):
            check_y = self.y - j
            if check_y in range (0,8):
                if board[(self.x, check_y)] == '':
                    valid_moves.append((self.x, check_y))
                else:
                    if board[(self.x, check_y)].white != self.white:
                        valid_moves.append((self.x, check_y))
                    break
                    
        # Check up
        for j in range (1,8):
            check_y = self.y + j
            if check_y in range (0,8):
                if board[(self.x, check_y)] == '':
                    valid_moves.append((self.x, check_y))
                else:
                    if board[(self.x, check_y)].white != self.white:       
                        valid_moves.append((self.x, check_y))
                    break
                    
        return valid_moves
class King(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "k"
    def is_move_valid(self, board):
        # TODO: prevent moving into check
        # This will require an array of all valid moves, so it can't be completed until those are all done
        valid_moves = []
        for i in range (-1,2):
            for j in range (-1,2):
                check_x = self.x - i
                check_y = self.y - j
                if check_x in range (0,8) and check_y in range(0,8):
                    if board[(check_x, check_y)] == '':
                        valid_moves.append((check_x, check_y))
                    else:
                        if board[(self.x, check_y)].white != self.white:
                            valid_moves.append((self.x, check_y))
        print(valid_moves)
        return valid_moves