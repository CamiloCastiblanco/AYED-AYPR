def main():
    x = int(input())
    y = int(input())
    z = int(input())
    if x > y and x > z :
        if (z**2 + y**2 == x**2):
            print("right")
        else:
            print("wrong")
    if y > x and y > z :
        if (x**2 + z**2 == y**2):
            print("right")
        else:
            print("wrong")
    if z > y and z > x :
        if (x**2 + y**2 == z**2) :
            print("right")
        else:
            print("wrong")
main()
