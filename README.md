# A-Star-Image-Maze-Solver
A project to implement the A* algorithm to create a maze image solving program.

## Intended Outcome:

-To be able to take in an image, of certain color constraints (listed in ImageConvert.py), and return a copy of that image with the solution shown

-The solution will be the path found by an implementation of the [A* (A-Star) algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)

## Pathfinding Process Using A* Algorithm:

-Read in the maze image using Image module from PIL library

-Convert image into a matrix (2D array) of str values based on the color of each pixel from image using ImageConvert module

-Identify start and end points by looping through matrix

-Create initial Coordinate object, from AStarCoordinate module, and add to a priority queue that maintains the invariant that minimizes the *F* cost of the head Coordinate

>A* calculates a *G*, *H*, and *F* cost per vertice (Coordinates in this implementation) in order to prioritize certain vertices  over others. The *G* cost is the actual cost to reach the current vertice (each step in a direction adds 1 to the *G* cost here) from the starting vertice. The *H* cost, however, is a heuristic that estimates the cost to reach goal vertice from the current vertice. This implementation uses an admissisable and consistent heuristic called the [Taxicab metric/Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) in order to calculate our *H* cost. Finally, the *F* is the sum of the *G* and *H* cost.

-Pop the head Coordinate from the priority queue of coordinates yet to see and check if it the goal coordinate

-If not, check the neighbors of the current Coordinate and add a new Coordinate to priority queue with current Coordinate as the parent if the neighbor hasn't already been seen, then add the current Coordinate to list of already see Coordinates.

-Repeat process until either goal position is found or priority becomes empty

-If goal is found, retrace correct path and mark each position on the matrix with the path symbol ("P")

-Convert matrix back into an Image object and translate each symbol into a pixel using ImageConvert module
