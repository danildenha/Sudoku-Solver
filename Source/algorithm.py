import pygame
import collections
from Solver import BLACK, WHITE, win, font, Node, ROWS, draw

def get_position(pos, Node):
    x, y = pos
    row = y // Node.width
    col = x // Node.width
    return row, col

def is_valid(node, value, nodes):
    # Check row
    for i in range(ROWS):
        if nodes[node.row][i].value == value and nodes[node.row][i] != node:
            return False
    
    # Check column
    for i in range(ROWS):
        if nodes[i][node.col].value == value and nodes[i][node.col] != node:
            return False
    
    # Check 3x3 grid
    box_row = node.row // 3 * 3
    box_col = node.col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if nodes[i][j].value == value and nodes[i][j] != node:
                return False
    
    return True

def solve_sudoku_step_by_step(nodes):
    for i in range(ROWS):
        for j in range(ROWS):
            if nodes[i][j].value == 0:
                for value in range(1, ROWS + 1):
                    nodes[i][j].value = value
                    if is_valid(nodes[i][j], value, nodes):
                        pygame.time.delay(100)  # Add a delay to visualize the solving step
                        win.fill(WHITE)
                        for row in nodes:
                            for node in row:
                                node.draw(win, font)
                        draw(win, BLACK)
                        pygame.display.update()
                        pygame.event.get()  # Handle events to avoid freezing
                        pygame.time.delay(100)  # Another delay for better visualization
                        if solve_sudoku_step_by_step(nodes):
                            return True
                    nodes[i][j].value = 0
                return False
    return True

def solve_one_step(nodes):
    for i in range(ROWS):
        for j in range(ROWS):
            if nodes[i][j].value == 0:
                for value in range(1, ROWS + 1):
                    nodes[i][j].value = value
                    if is_valid(nodes[i][j], value, nodes):
                        pygame.time.delay(100)  # Add a delay to visualize the solving step
                        win.fill(WHITE)
                        for row in nodes:
                            for node in row:
                                node.draw(win, font)
                        draw(win, BLACK)
                        pygame.display.update()
                        pygame.event.get()  # Handle events to avoid freezing
                        pygame.time.delay(100)  # Another delay for better visualization
                        return True
                    nodes[i][j].value = 0
    return False  # Return False if no steps were solved


def solve_sudoku(nodes):
    for row in range(ROWS):
        for col in range(ROWS):
            if nodes[row][col].value == 0:
                for value in range(1, ROWS + 1):
                    nodes[row][col].value = value
                    if is_valid(nodes[row][col], value, nodes) and solve_sudoku(nodes):
                        return True
                    nodes[row][col].value = 0
                return False
    return True
