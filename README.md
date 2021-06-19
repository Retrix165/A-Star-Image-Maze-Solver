# A-Star-Image-Maze-Solver
A project to implement the A* algorithm to create a maze image solving program.

Intended Outcome:
-To be able to take in an image, of certain color constraints, and return a copy of that image with the solution
-The solution will be the path created by the A* algorithm that I will implement

Intended Process:
-Read in the maze image using Image module from PIL
-Convert image into a 2D array of int values based on the color of each pixel
-The A* will use a 'node' class that references the 2D array to calculate the H & G cost for the F cost
-When the A* algorithm reaches the endpoint, retrace the steps and send back the path
-Apply the path to the 2D grid and convert the grid back into an image
