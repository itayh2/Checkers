import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, SCORE_FONT
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax
import pygame.mixer

# sounds for win and lose
pygame.mixer.init()
lose_sound = pygame.mixer.Sound("assets/lose.wav")
winner_sound = pygame.mixer.Sound("assets/winner.wav")
logo = pygame.image.load("assets/logo.png")
pygame.display.set_icon(logo)

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    # Game Loop
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            # The Depth is the difficult level of the ai
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        # Checking if someone has won
        if game.winner() != None:
            text = SCORE_FONT.render(game.winner(), 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            if game.winner() == "You Lose !":
                lose_sound.play()
            else:
                winner_sound.play()
            pygame.display.update()
            pygame.time.delay(5000)
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            # Press on 'r' key for reset the game
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game.reset()

        game.update(WIN)

    pygame.quit()


main()
