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


class PQ:

    #Constructor for PQ Class
    def __init__(self):
        self._elements = []


    #Push Function
    def push(self, element):
        return heappush(self._elements,element)


    #Pop Function
    def pop(self):
        return heappop(self._elements)

    def __bool__(self):
        return len(self._elements) > 0
