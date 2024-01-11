import pygame

def isValid(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))



def algotithm(nodes, ROWS):
    #Check if sudoku pattern provided is valid
    if isValid(nodes):
         pass
    else:
         