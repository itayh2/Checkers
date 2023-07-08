import pygame
from checkers.piece import Piece
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, GREY

#  The Board class represents the game board, which is made up of 8 x 8 squares, and is responsible for all the movements of the pieces on the board


class Board:
    # The __init__ method initializes the Board object
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    # The draw_squares method is responsible for drawing the checkerboard pattern on the game window
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREY, (row*SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # The evaluate method calculates and returns the evaluation score of the current board state
    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    # The get_all_pieces method takes a color parameter and returns a list of all the pieces on the board that match the specified color.
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    # The move method moves a piece to a new position on the board, If the piece reaches the last row, it is promoted to a king
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    # The get_piece method retrieves the piece object at a given row and column on the board.
    def get_piece(self, row, col):
        return self.board[row][col]

    # The create_board method populates the board list with Piece objects according to the initial configuration of the checkers game, Empty positions are represented as 0 in the board list.
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # The draw method draws the entire game board, including the squares and the pieces. It calls the draw_squares method to draw the squares and iterates over each position on the board.
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # The remove method removes a list of pieces from the board.
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    # The winner method checks if there is a winner in the current game state.
    def winner(self):
        if self.red_left <= 0:
            # return WHITE
            return "You Lose !"
        elif self.white_left <= 0:
            # return RED
            return "You Winner !"

        return None

    # The get_valid_moves method takes a piece object and returns a dictionary containing all the valid moves that the piece can make.
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(
                row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(
                row - 1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(
                row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(
                row + 1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    # Traverse Left Method which is handling how we actually determine where we can move to
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(
                        r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(
                        r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    # Traverse Right Method which is handling how we actually determine where we can move to
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(
                        r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(
                        r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return moves
