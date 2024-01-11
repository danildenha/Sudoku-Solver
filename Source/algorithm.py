import pygame

    #Check 3x3 box
def isValidSudoku(self, board):
        res = []
        for i in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))



def algotithm(nodes, ROWS):
    pass