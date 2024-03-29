import pygame
import copy
import collections
from Solver import BLACK, WHITE, win, font, Node, ROWS, draw

def reset(nodes):
    for i in range(ROWS):
        for j in range(ROWS):
            nodes[i][j].value = 0
    return

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
                    if is_valid(nodes[i][j], value, nodes):
                        nodes[i][j].value = value
                        pygame.time.delay(50)  # Add a delay to visualize the solving step
                        for row in nodes:
                            for node in row:
                                node.draw(win, font)
                        draw(win, BLACK)
                        pygame.display.update()
                        pygame.event.get()  # Handle events to avoid freezing
                        pygame.time.delay(50)  # Another delay for better visualization
                        if solve_sudoku_step_by_step(nodes):
                            return True
                        
                    nodes[i][j].value = 0
                return False
    return True

def solve_sudoku(nodes):
    for row in range(ROWS):
        for col in range(ROWS):
            if nodes[row][col].value == 0:
                for value in range(1, ROWS + 1):
                    nodes[row][col].value = value
                    if is_valid(nodes[row][col], value, nodes) and solve_sudoku(nodes):
                        nodes[row][col].value = value
                        return True
                    nodes[row][col].value = 0
                return False
    return True

def solve_one_step(nodes, curr):
    # Copy the initial state of the nodes
    initial_state = copy.deepcopy(nodes)
    row1 = curr.row
    col1 = curr.col

    # Solve the entire Sudoku puzzle and store it in initial state
    solve_sudoku(initial_state)

    # Reveal one step using solve_one_step
    if curr.value == 0:
        curr.value = initial_state[row1][col1].value
        return
