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
BLUE = (102, 178, 255)

# Fill the Board (rows and cols are equal so use only ROWS)
BOARD = [[0 for _ in range(ROWS)] for _ in range(ROWS)]
font = pygame.font.Font(None, 60)

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
    width = 80
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.selected = False

    def draw(self, win):
        if self.selected:
            color = BLUE
        else:
            color = BLACK
        text = font.render(str(self.value), True, color)
        text_rect = text.get_rect(center=(self.col * Node.width + Node.width // 2, self.row * Node.width + Node.width // 2))
        win.blit(text, text_rect)
    
def get_position(pos):
    x, y = pos
    row = y // Node.width
    col = x // Node.width
    return row, col



def main():
    nodes = [[Node(0, i, j) for j in range(ROWS)] for i in range(ROWS)]

    selected = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                row, col = get_position(clicked_pos)
                selected = nodes[row][col]
                selected.selected = not selected.selected
            if event.type == pygame.KEYDOWN:
                if selected and event.unicode.isdigit():
                    selected.value = int(event.unicode)
                    selected.selected = False
                    selected = None  # Deselect after inputting number

        win.fill(WHITE)
        for row in nodes:
            for node in row:
                node.draw(win)
        draw()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
