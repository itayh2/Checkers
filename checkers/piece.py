import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

#  The Piece class represents a single piece in the checkers game. It keeps track of its position, color, and whether it is a king. It provides methods for drawing the piece on the game window, updating its position, and making it a king.


class Piece:

    PADDING = 15
    OUTLINE = 3

    # The __init__ method initializes a Piece object
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    # The calc_pos method calculates and sets the exact position of the piece on the game board based on its row and column. It uses the SQUARE_SIZE constant to determine the size of each square on the board.
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # The make_king method sets the piece as a king by setting the king attribute to True.
    def make_king(self):
        self.king = True

    # The draw method is responsible for drawing the piece on the game window (win).
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() //
                     2, self.y - CROWN.get_height()//2))

    # The move method updates the position of the piece on the board.
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # The __repr__ method returns a string representation of the piece's color.
    def __repr__(self):
        return str(self.color)
