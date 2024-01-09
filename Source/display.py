import pygame

# Window and cell sizes
ROWS = 9
WIDTH = 720
HEIGHT = 720

def draw(win, color):

    # We dont want to draw the first line at the top of the screen
    for row in range(1, ROWS):
        if row%3==0:
            thickness = 3
        else:
            thickness = 1
        pygame.draw.line(win, color, (0, row* HEIGHT/ROWS), (WIDTH, row*HEIGHT/ROWS), thickness)
        pygame.draw.line(win, color, (row*WIDTH/ROWS, 0), (row*WIDTH/ROWS, HEIGHT), thickness)
    pass
