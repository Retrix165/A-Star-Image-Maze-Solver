"""
Maze Image Solver using A* Algorithm Module
By: Reid Smith

Notes:
    -Improved from BreathFirstSearchImage.py in Breath First Search Image Maze Project

Purpose:
    -To implement the A* algorithm by replacing the previously used breadth first search algorithm and make code more readable and pythonic

"""
from PIL import Image
from AStarCoordinate import Coordinate
from ImageConvert import img_to_mat, mat_to_img

def astar_img(img: Image) -> Image:

    if img is None:
        raise Exception("None Image Given")

    matrix = img_to_mat(img)
    pass

