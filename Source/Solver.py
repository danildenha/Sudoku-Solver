# ___________________________________________________NOT FINISHED YET____________________________________________________________
import pygame

pygame.init()

# Window and cell sizes
WIDTH = 720
HEIGHT = 720
ROWS = 9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Fill the Board (rows and cols are equal so use only ROWS)
BOARD = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

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

class Node:
    size = 80
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.selected = False



def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        win.fill(WHITE)
        draw()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()



