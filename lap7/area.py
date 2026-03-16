# area.py
def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Both values has to be positive")
    if not isinstance(length, (int, float)):
        raise TypeError("length")
    if not isinstance(width, (int,float)):
        raise TypeError("width faaaaa")

    return length * width