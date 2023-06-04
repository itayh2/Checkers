import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, SCORE_FONT
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax


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
            pygame.display.update()
            pygame.time.delay(5000)
            game.reset()
            # run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update(WIN)

    pygame.quit()


main()
