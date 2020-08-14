import sys
def main():
    x=int(input())
    y=int(input())
    z=int(input())

    if x>y and x>z:
        if y>z:
            print ("Case 1:",y)
        else:
            print ("Case 1:",z)
            
    if y>x and y>z:
        if x>z:
            print ("Case 1:",x)
        else:
            print ("Case 1:",z)
            
    if z>y and z>x:
        if y>x:
            print ("Case 1:",y)
        else:
            print ("Case 1:",x)
main()
