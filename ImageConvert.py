# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:37:20 2021

@author: Reid Smith
"""
from PIL import Image


def imgToGrid(img: Image):
    imgData = img.load()
    grid = [[colorToNum(imgData[y,x]) for y in range(img.height)]for x in range(img.width)]
    return grid


def gridToImg(grid: list):
    out = Image.new(mode="RGB", size = (len(grid[0]),len(grid)))
    imgOut = out.load()
    for x in range(out.width):
        for y in range(out.height):
            imgOut[y,x] = numToColor(grid[x][y])
    return out


def colorToNum(color: tuple):
    if color == (0,0,0):
        return 1
    elif color == (255,255,255):
        return 0
    elif color == (255,64,64):
        return 7
    elif color == (63, 72, 204):
        return 9
    raise Exception("Unrecognized COLOR: "+str(color))

def numToColor(num: int):
    if num == 1:
        return (0,0,0)
    elif num == 0:
        return (255,255,255)
    elif num == 7:
        return (255,64,64)
    elif num == 9:
        return (63, 72, 204)
    raise Exception("Unrecognized NUMBER: "+str(num))

def printGrid(grid: list):
    print('\n'.join([' '.join([str(item) for item in row]) for row in grid]))
    
#Code to test conversion and reverse
#test = Image.open("./TestMazes/testMaze1.png")
#result = imgToGrid(test)
#printGrid(result)
#back = gridToImg(result)
#back.show()


