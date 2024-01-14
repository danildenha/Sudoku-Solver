# ___________________________________________________NOT FINISHED YET____________________________________________________________
import pygame
from display import draw
from node import Node
from algorithm import *


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

#=========================================================================================
SOLVING = False

def main():
    global SOLVING
    # Fill the Board (rows and cols are equal so use only ROWS)
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
                row, col = get_position(clicked_pos, Node)
                curr.selected = False
                curr = nodes[row][col]
                curr.selected = True  # Select the clicked node

            if event.type == pygame.KEYDOWN:
                
                if event.unicode.isdigit():
                    if any(node.selected for row in nodes for node in row):
                        curr.value = int(event.unicode)
                        curr.selected = False  # Deselect after inputting number

                elif event.key == pygame.K_BACKSPACE:
                    curr.value = 0
                    curr.selected = False
                elif event.key == pygame.K_SPACE:
                    if not SOLVING:
                        SOLVING = True
                        solve_sudoku_step_by_step(nodes)  # Call a new step-by-step solving function
                    else:
                        SOLVING = False
                elif event.key == pygame.K_s:
                    if solve_sudoku(nodes):
                        print("Sudoku Solved!")
                    else:
                        print("No solution exists")
                elif event.key == pygame.K_c:
                    solve_one_step(nodes)
  

        win.fill(WHITE)
        for row in nodes:
            for node in row:
                node.draw(win, font)
        draw(win, BLACK)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
