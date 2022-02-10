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
from PriorityQueue import PQ

def astar_img(img: Image) -> Image:

    if img is None:
        raise Exception("None Image Given")

    matrix = img_to_mat(img)

    end_points = _find_end_point_coords(matrix)
    Coordinate.goal_x, Coordinate.goal_y = end_points[1]
    start_coord = Coordinate(end_points[0][0], end_points[0][1], "S")

    coords_yet_to_see = PQ()
    coords_yet_to_see.push(start_coord)
    coords_already_seen = []

    while coords_yet_to_see:
        cur_coord = coords_yet_to_see.pop()

    return img
    #return mat_to_img(matrix)



def _find_end_point_coords(mat: list) -> tuple:

    if mat is None:
        raise Exception("None Matrix Given")

    if not isinstance(mat[0],list):
        raise Exception("1-Dimensional List Given")

    start_coords = None
    end_coords = None

    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == "S":
               start_coords = (x,y)
            elif mat[y][x] == "F":
                end_coords = (x,y)

    if start_coords is None:
        raise Exception("Starting Coordinates Not Found")

    if end_coords is None:
        raise Exception("Ending Coordinates Not Found")

    return (start_coords,end_coords)


#Testing Area (DELETE BEFORE FINAL DRAFT)
image = Image.open("../TestMazes/RealMaze1.png")

astar_img(image)


