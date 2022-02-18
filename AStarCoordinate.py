"""
Coordinate Module
By: Reid Smith

Notes:
    -Improved from Coordinate.py in Breadth First Search Image Maze Project

Purpose:
    -To create Coordinate objects that store information about a node's position, parent, f cost, g cost, h cost, and comparison in a pythonic way

"""

class Coordinate:

    goal_x = None
    goal_y = None


    #Constructor of Coordinate Class
    def __init__(self, x, y, data, parent = None):

        self.x = x
        self.y = y
        self.data = data
        self.parent = parent

        self.update_costs()


    #G (Cost to Reach Coordiante) Function
    def _calculate_g(self):

        if self.parent is not None:
            return self.parent.g + 1
        else:
            return 0


    #H (Heuristic to Reach Goal Coordinate) Function / Manhattan Distance Estimation
    def _estimate_h(self):

        if Coordinate.goal_x is None or Coordinate.goal_y is None:
            raise Exception("Goal Position Unset")

        x_dist = self.x - Coordinate.goal_x
        y_dist = self.y - Coordinate.goal_y

        if x_dist < 0:
            x_dist *= -1

        if y_dist < 0:
            y_dist *= -1

        return x_dist + y_dist


    #F (Combined G & H Cost) Function
    def _calculate_f(self):

        return self.g + self.h


    #Update Object's Costs Function
    def update_costs(self):

        self.g = self._calculate_g()
        self.h = self._estimate_h()
        self.f = self._calculate_f()


    #Check if is Goal Position
    def is_goal(self):

        return Coordinate.goal_x == self.x and Coordinate.goal_y == self.y


    #Object Comparison (for PriorityQueue Sorting) Function
    def __lt__(self,other):

        if other is None:
            raise Exception("None Other Coordinate Given")

        if not isinstance(other,Coordinate):
            raise ValueError("Unfit Comparison between Coordinate and Non-Coordinate")

        return self.f < other.f


    #Object Comparison (for in/not in Operators) Function
    def __eq__(self,other):

        if other is None or not isinstance(other,Coordinate):
            return False

        return other.x == self.x and other.y == self.y


    #String Typecast Function
    def __str__(self):

        #Parent attribute not listed to prevent recursive loop
        return "x: {} y: {} data: {} g: {} h: {} f: {}".format(self.x, self.y, self.data, self.g, self.h, self.f)


#Diagnostics of Construction and Functions (if run directly)
if __name__ == "__main__":

    print("Running AStarCoordinate's Coordinate Class Diagnostics:")
    print("\tCreating Test Coordinate Objects and Set Up Goal: ", end= "")

    Coordinate.goal_x = 0
    Coordinate.goal_y = 0

    coord_1 = Coordinate(5, 10, "Test Value")
    coord_2 = Coordinate(5, 10, "Another Test Value", parent= coord_1)

    print("Success!")
    print("\tComparing Two Coordinate Objects: ", end= "")

    assert(coord_1 < coord_2)

    assert(coord_1 == coord_2)

    coord_1.x = 100

    assert(not (coord_1 == coord_2))

    coord_1.x = 5

    list_coord = Coordinate(5,10,"Testicles: Hero of Troy")

    test_list = [list_coord]

    assert(coord_1 in test_list)

    print("Success!")
    print("\tUpdating Parent & Cost of Coordinate Object: ", end= "")

    farther_away_coord = Coordinate(25, 25, "Valuish Testuish", parent= coord_2)
    even_father_away_coord = Coordinate(30, 30, "Test Value 2: Electric Boogalo", parent= farther_away_coord)

    coord_1.parent = even_father_away_coord
    coord_1.update_costs()

    assert(coord_2 < coord_1)

    print("Success!")
    print("\tUpdating Postion & Cost of Coordinate Object: ", end="")

    coord_1.x = 1
    coord_1.y = 1

    coord_1.update_costs()

    assert(coord_1 < coord_2)

    print("Success!")
    print("\tCheck if Coordinates are at Goal Position: ",end="")

    assert(not coord_1.is_goal())

    Coordinate.goal_x = 1
    Coordinate.goal_y = 1

    assert(coord_1.is_goal())

    print("Success!")

