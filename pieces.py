class Piece:
    # White is a boolean to represent white or black
    # White is True, black is False
    def __init__(self, white, x, y):
        self.white = white
        self.x = x
        self.y = y

class Pawn(Piece):
    def __init__(self, x, y, white):
        super().__init__(white, x, y)
        self.symbol = "p"

class Rook(Piece):
    def __init__(self, x, y, white):
        super().__init__(white, x, y)
        self.symbol = "r"