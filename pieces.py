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
    # returns True if move is valid, false otherwise
    def is_move_valid(self, location):
        True
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