import math

def calc_shape_area(length, width=None, shape="s"):
    if length == None or length <= 0:
        return None
    
    if shape == "s":
        return length * length
    elif shape == "r":
        if width == None :
            width = length
        if width <= 0:
            return None
        return length * width
    elif shape == "t":
        if width == None :
            width = length
        if width <= 0:
            return None
        return length * width / 2
    elif shape == "c":
       return math.pi * (length**2)
    else:
        return None

def print_area(length, width=None, shape="s"):
    area = calc_shape_area(length, width, shape)

    if width == None or width <= 0:
        width = length
    if area != None:
        if shape.lower() == "s":
            print(f"Area of a square {length} x {length} is {area:.4f}")
        elif shape.lower() == "r":
            print(f"Area of a rectangle {length} x {width} is {area:.4f}")
        elif shape.lower() == "t":
            print(f"Area of a triangle with base {length} x height {width} is {area:.4f}")
        elif shape == "c":
            print(f"Area of a circle with radius {length} is {area:.4f}")
    else:
        print(f"Invalid input: No area value.")


if __name__ == "__main__":

    # Get inputs
    dim = input("Enter dimension(s): ").split()
    if len(dim) == 1:
        try:
            l = float(dim[0])
            w = 0
        except ValueError as e:
            print("Can't convert length")
            exit()
    elif len(dim) == 2:
        try:
            l = float(dim[0])
            w = float(dim[1])
        except ValueError as e:
            print("Can't convert width or length")
            exit()
    else:
        print("Invalid input dimension.")
        exit()
    
    # Test cases
    print_area(l, None, "s")
    print_area(l, w, "r")
    print_area(l, w, "t")
    print_area(l, None, "c")
    print_area(l, w, "x")
