import pygame

# Display Size
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Rgb Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

# Loads an image of a crown and then scaled to a size of 45x25 pixels
CROWN = pygame.transform.scale(
    pygame.image.load('assets/crown.png'), (45, 25))

pygame.init()

# Sets up a font object that will be used for rendering text in the game
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
