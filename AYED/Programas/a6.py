from sys import stdin
def main():
    x= int(stdin.readline())
    y=int(stdin.readline())
    if x==y:
        print ("=")
    else:
        if x<y:
            print ("<")
        else:
            print (">")
main()
