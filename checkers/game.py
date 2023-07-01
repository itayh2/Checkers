import pygame
from .constants import RED, WHITE, GREEN, SQUARE_SIZE
from checkers.board import Board
import pygame.mixer


pygame.mixer.init()
step_sound = pygame.mixer.Sound("assets/step.wav")

# The Game class represents the checkers game itself. It handles the game state, player turns, piece selection, piece movement, and AI moves. It also provides methods for resetting the game, retrieving the game board, and checking for a winner.


class Game:

    # The __init__ method initializes a Game object. It takes a win parameter representing the game window and calls the _init method to initialize the game state.
    def __init__(self, win):
        self._init()
        self.win = win

    # The update method updates the display and draws the current state of the game on the game window (win).
    def update(self, win):
        self.board.draw(win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # The _init method initializes the game state.
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    # The winner method returns the result of the winner method of the game board. It determines if there is a winner in the game.
    def winner(self):
        return self.board.winner()

    # The reset method resets the game by calling the _init method.
    def reset(self):
        self._init()

    # The select method which will allow us to actually select a piece or potentially move a piece
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    # The _move method is responsible for moving a piece on the game board.
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # The draw_valid_moves method is responsible for drawing the valid moves on the game window.
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE +
                               SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    # The change_turn method is responsible for changing the turn to the next player.
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
        step_sound.play()

    # The get_board method returns the current game board.
    def get_board(self):
        return self.board

    # The ai_move method is used to simulate an AI move.
    def ai_move(self, board):
        self.board = board
        self.change_turn()
