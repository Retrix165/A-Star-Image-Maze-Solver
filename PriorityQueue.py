from heapq import heappush, heappop

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def push(self, element):
        return heappush(self.elements,element)

    def pop(self):
        return heappop(self.elements)


test = PriorityQueue()

test.push(5)
test.push(7)
test.push(3)
test.push(-1)
test.push(18)

print(test.pop())
print(test.pop())

