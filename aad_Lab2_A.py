import math


def main(): 
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))

    if side1 < side2 and side3 < side2:
        out = ((side1**2) + (side3**2))
        if out == (side2**2): 
            print("This triangle has a right angle!")
        else: 
            print("This triangle doesn’t have a right angle...")
    if side2 < side1 and side3 < side1: 
        out = ((side2**2) + (side3**2))
        if out == (side1**2):
            print("This triangle has a right angle!")
        else: 
            print("This triangle doesn’t have a right angle...")
    if side1 < side3 and side2 < side3:
        out = ((side1**2) + (side2**2))
        if out == (side3**2):
            print("This triangle has a right angle!")
        else: 
            print("This triangle doesn’t have a right angle...")




if __name__ == "__main__":
    main()


