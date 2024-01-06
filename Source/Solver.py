import pygame

pygame.init()

# Window and cell sizes
WIN = 900
WIDTH = 100

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREY = (128, 128, 128)

# Fill the Board
rows = 9
cols = 9
BOARD = [[0 for _ in range(cols)] for _ in range(rows)]

