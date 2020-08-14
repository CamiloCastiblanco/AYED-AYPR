def multi(a,b):
    if a%b == 0:
        print("SI")
        
    elif b%a == 0:
        print("SI")

    else:
        print ("NO")

def main():
    a = int(input())
    
    b = int(input())
    
    multi(a,b)
    
main()
