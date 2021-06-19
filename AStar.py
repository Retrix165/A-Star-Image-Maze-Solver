# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:21:24 2021

@author: Reid Smith

NOTES:
    -grid[y coord][x coord] = point WHICH DOES NOT EQUAL (x-coord, y-coord) = point
    
"""
from PIL import Image
import GridTransfer 


#Method to identify the coordinates of the starting point for A* algorithm
def findStartPoint(grid: list):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 7:
                return [y,x] #Returned as grid[y][x] format

#Method to identify the coordinates of the starting point for A* algorithm
def findEndPoint(grid: list):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 9:
                return [y,x] #Returned as grid[y][x] format


#Code to test function importation and in-file functions(point finders)
#test = Image.open("./TestMazes/testMaze1.png")
#result = GridTransfer.imgToGrid(test)
#GridTransfer.printGrid(result)
#print(findStartPoint(result))
#print(findEndPoint(result))
#print(result)