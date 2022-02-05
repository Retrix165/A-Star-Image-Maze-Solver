"""
Coordinate Module
By: Reid Smith

Notes:
    -Improved from Coordinate.py in Breadth First Search Image Maze Project

Purpose:
    -To create Coordinate objects that store information about a node's position, parent, f cost, g cost, and h cost in a pythonic way

"""
class Coordinate:

    goal_x = None
    goal_y = None

    def __init__(self, x, y, data, parent = None):

        self.x = x
        self.y = y
        self.data = data
        self.parent = parent

        if parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 0

        self._estimate_h()

        self._calculate_f()

    def _estimate_h(self):

        if Coordinate.goal_x is None or Coordinate.goal_y is None:
            raise Exception("Goal Position Unset")

        x_dist = self.x - Coordinate.goal_x
        y_dist = self.y - Coordinate.goal_y

        if x_dist < 0:
            x_dist *= -1

        if y_dist < 0:
            y_dist *= -1

        self.h = x_dist + y_dist

    def _calculate_f(self):
        self.f = self.g + self.h

    def __lt__(self,other):
        return self.weight < other.weight

    def __str__(self):
        return "x: {} y: {} data: {} g: {} h: {} f: {}".format(self.x, self.y, self.data, self.g, self.h, self.f)
