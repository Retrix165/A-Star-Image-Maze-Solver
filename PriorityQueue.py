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


    #Contains Operator
    def __contains__(self, other):
        return other in self._elements


    #Boolean Operator
    def __bool__(self):
        return len(self._elements) > 0

    #String Operator
    def __str__(self):
        return str(self._elements)


#Diagnostics of Functions and Operators (if run directly)
if __name__ == "__main__":

    print("Running PriorityQueue Module Diagnostics:")
    print("\tCreating Test PriorityQueue Object: ", end="")

    test_pq = PQ()

    print("Success!")
    print("\tPushing and Popping Integers: ", end="")

    test_pq.push(7)
    test_pq.push(1)
    test_pq.push(5)
    test_pq.push(2)
    test_pq.push(6)
    test_pq.push(3)
    test_pq.push(4)

    assert(test_pq.pop() == 1)
    assert(test_pq.pop() == 2)
    assert(test_pq.pop() == 3)
    assert(test_pq.pop() == 4)
    assert(test_pq.pop() == 5)
    assert(test_pq.pop() == 6)
    assert(test_pq.pop() == 7)

    print("Success!")
    print("\tChecking Boolean Value of PriorityQueue Object: ", end="")

    assert(not test_pq)

    test_pq.push(1)

    assert(test_pq)

    print("Success!")
    print("\tChecking Contains Operator of PriorityQueue Object: ",end="")

    test_pq.push(2)
    test_pq.push(17)

    assert(2 in test_pq)
    assert(3 not in test_pq)

    print("Success!")




