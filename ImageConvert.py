"""
Image Converting Module
By: Reid Smith

Notes:
    -Improved from ImageHandle.py in Breadth First Search Image Maze Project

Purpose:
    -To handle conversions between Image objects and a 2D matrix with specific symbol/color conversions in a more readable and pythonic way

Conversion Table (Color/Color Name/Symbol/Symbol Name):
    - 000000 - Black - B (Barrier)
    - ffffff - White - 0 (Open)
    - e91e62 - Red   - S (Start Space)
    - 3f51b5 - Blue  - F (End Space)
    - 4da32e - Green - P (Path Found)

"""

#Import Image Class from PIL
from PIL import Image


#Pixel to Symbol Function
def _pix_to_sym(col: tuple) -> str:

    if col is None:
        raise Exception("None Color Value Given")

    conv_table = {
        (0,0,0,0): "B",
        (0,0,0,255): "B",
        (255,255,255,255): "0",
        (233,30,99,255): "S",
        (233,30,98,255): "S",
        (63,81,181,255): "F"
    }
    sym = conv_table.get(col,None)

    if sym is None:
        raise Exception("Unrecognized Color Value:",col)

    return sym


#Symbol to Pixel Function
def _sym_to_pix(sym: str) -> tuple:
    if sym is None:
        raise Exception("None String Value Given")

    conv_table = {
        "B": (0,0,0,255),
        "0": (255,255,255,255),
        "S": (233,30,99,255),
        "F": (63,81,181,255),
        "P": (77,163,46,255)
    }
    pix = conv_table.get(sym,None)

    if pix is None:
        raise Exception("Unrecognized Symbol Value Given",sym)

    return pix


#Image to Matrix Function
def img_to_mat(img: Image) -> list:

    if img is None:
        raise Exception("None Image Given")

    img_data = img.load()
    mat = [[_pix_to_sym(img_data[y,x]) for x in range(img.width)] for y in range(img.height)]
    return mat


#Matrix to Image Function
def mat_to_img(mat: list) -> Image:

    if mat is None:
        raise Exception("None Matrix Given")

    if not isinstance(mat[0],list):
        raise Exception("1-Dimensional List Given")

    img = Image.new(mode = "RGBA", size = (len(mat[0]),len(mat)))
    img_data = img.load()
    for y in range(img.height):
        for x in range(img.width):
            img_data[y,x] = _sym_to_pix(mat[y][x])
    return img


#Print Matrix Function
def print_mat(mat: list):

    if mat is None:
        raise Exception("None Matrix Given")

    if not isinstance(mat[0],list):
        raise Exception("1-Dimensional List Given")

    for y in range(len(mat)):
        print("".join(mat[y][x] for x in range(len(mat[0]))))


#Diagnostics of Functions (if run directly)
if __name__ == "__main__":

    print("Running ImageConvert Module Diagnostics:")
    print("\tOpening Diagnostic Maze and Converting to Matrix: ", end="")

    image = Image.open("../TestMazes/DiagnosticMaze.png")

    matrix = img_to_mat(image)

    print("Success!")
    print("\tPrinting Test Matrix: ", end="")

    print_mat(matrix)

    print("Success!")
    print("\tConverting Test Matrix Back to Image: ", end="")

    test_image = mat_to_img(matrix)

    print("Success!")

    print("\tShowing Result Image: ", end="")

    test_image.show()

    print("Success!")



