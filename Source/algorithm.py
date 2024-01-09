import pygame

def is_valid(node, value, nodes, ROWS):
    for i in range(ROWS):
        if nodes[nodes.row][i].value == value and nodes[node.row][i] != node:
            return False


def algotithm(nodes, ROWS):
    pass