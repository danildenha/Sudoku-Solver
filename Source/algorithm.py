import pygame

def is_valid(node, value, nodes, ROWS):
    for i in range(ROWS):
        if nodes[nodes.row][i].value == value and nodes[node.row][i] != node:
            return False
        if nodes[i][nodes.col].value == value and nodes[i][nodes.col] != node:
            return False
        

        
    return True


def algotithm(nodes, ROWS):
    pass