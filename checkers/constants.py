import pygame

# Display Size
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Rgb Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Load Image
CROWN = pygame.transform.scale(
    pygame.image.load('assets/crown.png'), (45, 25))

pygame.init()

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
