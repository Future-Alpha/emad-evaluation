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


def evaluate(line_matrix, dots_matrix):
    """
    screan --> grid 32x32
    each point is one square from the grid
    if the line went over all point squares in the right order --> pass
        else calculate the orecision
    """
    grid_length = 32
    grid = np.ones((grid_length, grid_length, 4))

    # https://stackoverflow.com/questions/20402109/calculating-percentage-error-by-comparing-two-arrays
    a = np.array([1, 2, 3, 4, 5, 6, 7])
    b = np.array([1, 2, 3, 5, 5, 6, 7])
    error = np.mean(a != b)

    # or
    import difflib

    pr = difflib.SequenceMatcher(None, array1, array2)
    print(pr.ratio())

    pass
