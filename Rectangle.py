def rect(a,b):
    """Returns the area of the rectangle with length a and breadth b"""
    return a*b
a=int(input("Enter length of the rectangle: "))
b=int(input("Enter breadth of the rectangle: "))
print("Area of the rectangle is",rect(a,b))
print(rect.__doc__)
