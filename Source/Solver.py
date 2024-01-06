# ___________________________________________________NOT FINISHED YET____________________________________________________________
import pygame

pygame.init()

# Window and cell sizes
WIDTH = 720
HEIGHT = 720
ROWS = 9

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREY = (128, 128, 128)

# Fill the Board (rows and cols are equal so use only ROWS)
BOARD = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

# Set up the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("danildenha Sudoku Solver")

def draw():
    for row in range(ROWS):
        if row%3==0:
            thickness = 3
        else:
            thickness = 1
        
        pygame.draw.line(win, BLACK, (0, row*110), (WIDTH, row*110), thickness)



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



