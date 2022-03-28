def area_of_square(side):
    return side*side

def perimeter_of_rectangle(length, breadth):
    return 2*(length + breadth)

def area_of_rectangle(length, breadth):
    return length * breadth

while(True):
    print("Calculate area of Square:")
    print("Calculate perimeter of Rectangle:")
    print("Calculate are of Rectangle:")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        side = int(input("Enter a number:"))
        areaOfSquare = area_of_square(side)
        print(areaOfSquare)
    if choice == 2:
        length = int(input("Enter a number:"))
        breadth = int(input("Enter a number:"))
        perimeterOfRectangle = perimeter_of_rectangle(length, breadth)
        print(perimeterOfRectangle)
    if choice == 3:
        length = int(input("Enter a number:"))
        breadth = int(input("Enter a number:"))
        areaOfRectangle = area_of_rectangle(length, breadth)
        print(areaOfRectangle)

if __name__ =="__main__":
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))

    Square = ara_of_square(a)
    print(Square)
    Rectangle = perimeter_of_rectangle(a, b)
    print(Rectangle)
    Area_of_Rectangle = area_of_rectangle(a, b)
    print(Area_of_Rectangle)
