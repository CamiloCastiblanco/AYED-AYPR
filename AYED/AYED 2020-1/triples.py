def main():
    a = str(input())
    b = str(input())

    a = a.split(" ")
    b = b.split(" ")

    

    if int(a[0]) > int(b[0]):
        ana = 1
        bob = 0
    elif int(a[0]) == int(b[0]):
        ana = 0
        bob = 0
    else:
        ana = 0
        bob = 1
        
    if int(a[1]) > int(b[1]):
        ana = ana + 1
        bob = bob
        
    elif int(a[1]) == int(b[1]):
        ana = ana
        bob = bob
    else:
        ana = ana
        bob = bob + 1
        
    if int(a[2]) > int(b[2]):
        ana = ana + 1
        bob = bob
        
    elif int(a[2]) == int(b[2]):
        ana = ana
        bob = bob
    else:
        ana = ana
        bob = bob + 1

    print (str(ana) + ' ' + str(bob))
main()

