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
    

class Knight(Piece):     
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "n"

class Bishop(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "b"

class Queen(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "q"

class King(Piece):
    def __init__(self, x_y_pair, white):
        super().__init__(white, x_y_pair[0], x_y_pair[1])
        self.symbol = "k"
    def is_move_valid(self, board):
        valid_moves = []
        for i in range (-1,2):
            for j in range (-1,2):
                check_x = self.x - i
                check_y = self.y - j
                print (f"({check_x},{check_y})")
                if check_x in range (0,8) and check_y in range(0,8):
                    if board[(check_x, check_y)] == '':
                        valid_moves.append((check_x, check_y))
        print (valid_moves, self.symbol)
        return valid_moves