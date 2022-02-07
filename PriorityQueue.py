"""
Priority Queue Module
By Reid Smith

Notes:
    -Bare bones improvement over heapq library functions

Purpose:
    -To implement a priority queue

"""

#Import Functions from heapq
from heapq import heappush, heappop


class PriorityQueue:

    #Constructor for PriorityQueue Class
    def __init__(self):
        self.elements = []


    #Push Function
    def push(self, element):
        return heappush(self.elements,element)


    #Pop Function
    def pop(self):
        return heappop(self.elements)


