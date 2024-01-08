import pygame
import sys
sys.path.append('Screen')

from Screen.display import Node, draw

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (102, 178, 255)

# Window and cell sizes
ROWS = 9
WIDTH = 720
HEIGHT = 720

# Set up the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("danildenha Sudoku Solver")

def draw():

    # We dont want to draw the first line at the top of the screen
    for row in range(1, ROWS):
        if row%3==0:
            thickness = 3
        else:
            thickness = 1
        pygame.draw.line(win, BLACK, (0, row* HEIGHT/ROWS), (WIDTH, row*HEIGHT/ROWS), thickness)
        pygame.draw.line(win, BLACK, (row*WIDTH/ROWS, 0), (row*WIDTH/ROWS, HEIGHT), thickness)
    pass
