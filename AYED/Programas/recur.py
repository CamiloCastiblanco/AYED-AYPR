def funa(n):
    
    if n == 1:
        
        return n
    
    else:
        print(n)
        return funa (n//2)

def main():
    n = int(input())
    x = funa(n)
    print(x)

main()
