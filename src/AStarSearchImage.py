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
from random import shuffle

#Maze Solver Algorithm using A* Algorithm Function
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

    checked_coords = 0

    while coords_yet_to_see:

        cur_coord = coords_yet_to_see.pop()
        matrix[cur_coord.y][cur_coord.x] = "C"
        checked_coords += 1

        if cur_coord.is_goal():
            print("GOAL FOUND")
            print("Current path length: ",cur_coord.g)
            print("Checked",checked_coords,"coordinates")
            matrix = _retrace_path(cur_coord,matrix)
            break

        #Complex Relative Coordinate Neighbors (Diagonals Included), diagonals shouldn't be calculated the same with manhattan distance though as regular neighbors
        #neighbors = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

        neighbors_simple = [(1,0),(-1,0),(0,1),(0,-1)]
        #Shuffle for fun
        shuffle(neighbors_simple)

        for neighbor_shift in neighbors_simple:
            tmp_x = cur_coord.x + neighbor_shift[0]
            tmp_y = cur_coord.y + neighbor_shift[1]

            if matrix[tmp_y][tmp_x] == "B":
                continue

            tmp_coord = Coordinate(tmp_x,tmp_y, matrix[tmp_y][tmp_x], parent=cur_coord)

            if (tmp_coord not in coords_yet_to_see) and (tmp_coord not in coords_already_seen):
                coords_yet_to_see.push(tmp_coord)

        coords_already_seen.append(cur_coord)

    else:
        print("GOAL NOT FOUND")

    return mat_to_img(matrix)


#Find Positions of Start and End Points Function
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


#Retrace Path of Goal Coordinate Function
def _retrace_path(cur_coord: Coordinate, mat: list) -> None:

    if cur_coord is None:
        raise Exception("None Coordinate Given")

    if not isinstance(cur_coord, Coordinate):
        raise ValueError("Non-Coordinate Type Given")

    while cur_coord is not None:

        mat[cur_coord.y][cur_coord.x] = "P"
        cur_coord = cur_coord.parent

    return mat



#Testing Area (DELETE BEFORE FINAL DRAFT)
image = Image.open("../TestMazes/TestMaze3.png")

out_image = astar_img(image)

out_image.show()


