# ___________________________________________________NOT FINISHED YET____________________________________________________________
import pygame
from display import draw
from node import Node

pygame.init()
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window and cell sizes
ROWS = 9
WIDTH = 720

# Set up the window
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("danildenha Sudoku Solver")
font = pygame.font.Font(None, 60)

# Fill the Board (rows and cols are equal so use only ROWS)
BOARD = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

def get_position(pos):
    x, y = pos
    row = y // Node.width
    col = x // Node.width
    return row, col


def main():
    nodes = [[Node(0, i, j) for j in range(ROWS)] for i in range(ROWS)]
    global curr
    curr = nodes[0][0]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                row, col = get_position(clicked_pos)
                curr.selected = False
                curr = nodes[row][col]
                curr.selected = True  # Select the clicked node

            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    if any(node.selected for row in nodes for node in row):
                        curr.value = int(event.unicode)
                        curr.selected = False  # Deselect after inputting number
                elif event.key == pygame.K_SPACE:
                    #algorithm
                    pass

            

        win.fill(WHITE)
        for row in nodes:
            for node in row:
                node.draw(win, font)
        draw(win, BLACK)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
