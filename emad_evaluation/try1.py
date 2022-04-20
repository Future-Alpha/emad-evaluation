import pygame
import numpy as np


def draw(virtual_mouse_matrix):
    """
    In our game loop:
    If left mouse button pressed:
        Fetch the click position in our window
        If previous_point not equal to None:
            Draw a line from previous point to click position
        Set previous_point = click position
    """
    pass


def clear():
    """cleare the doawn lines"""
    pass


def grid_render(letter):
    '''
    screan --> grid 72x72
    each point is one square from the grid
    '''
    grid_length = 72
    opacity = 0.5
    grid = np.ones((grid_length, grid_length, 4))
    if letter == 'a':
        grid[2][2]=[0,0,0,opacity]
        grid[3][3]=[0,0,0,opacity]
        grid[4][4]=[0,0,0,opacity]
        grid[5][5]=[0,0,0,opacity]
        grid[4][6]=[0,0,0,opacity]
        grid[3][7]=[0,0,0,opacity]
        grid[2][8]=[0,0,0,opacity]
        grid[3][4]=[0,0,0,opacity]
        grid[3][5]=[0,0,0,opacity]
        grid[3][6]=[0,0,0,opacity]

    if letter == 't':
        grid[4][2]=[0,0,0,opacity]
        grid[4][3]=[0,0,0,opacity]
        grid[4][4]=[0,0,0,opacity]
        grid[3][3]=[0,0,0,opacity]
        grid[2][3]=[0,0,0,opacity]
        grid[1][3]=[0,0,0,opacity]







def evaluate(line_matrix, dots_matrix):
    """
    if the line went over all point squares in the right order: print (pass)
        else calculate the orecision
    """

    a = np.array(line_matrix)
    b = np.array(dots_matrix)
    error = np.mean(a != b)
    print(error)

    # or

    import difflib
    pr = difflib.SequenceMatcher(None, line_matrix, dots_matrix)
    print(pr.ratio())



evaluate([1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7])