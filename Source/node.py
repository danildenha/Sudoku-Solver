import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (102, 178, 255)
PINK = (255, 182, 193)

class Node:
    width = 80
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.selected = False

    def draw(self, win, font):
        if self.selected:
            color = GREY
            bg = BLUE
        else:
            color = BLACK
            # Change the background color based on the position in the Sudoku grid
            if (self.row in [1, 5] and self.col in [0, 2, 6, 8]) or (self.row in [0, 2, 3, 4, 6, 7, 8] and self.col in [3, 5]):
                bg = PINK
            else:
                bg = WHITE

        pygame.draw.rect(win, bg, (self.col * Node.width, self.row * Node.width, Node.width, Node.width))
        text = font.render(str(self.value), True, color)
        text_rect = text.get_rect(center=(self.col * Node.width + Node.width // 2, self.row * Node.width + Node.width // 2))
        if self.value != 0:
            win.blit(text, text_rect)
