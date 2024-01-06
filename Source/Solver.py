import pygame

pygame.init()

# Window and cell sizes
WIDTH = 900
ROWS = 9

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREY = (128, 128, 128)

# Fill the Board
rows = 9
cols = 9
BOARD = [[0 for _ in range(cols)] for _ in range(rows)]

# Set up the window
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("danildenha Sudoku Solver")

def draw():
    for row in ROWS:
        if row%3==0:
            thickness = 3
        else:
            thickness = 1
        
        pygame.draw.line(win, BLACK, (row*100))



