from sys
def main():   
    pri = [2]
    n = int(sys.stdin.readline())
    for x in range(3, n+1):
        for i in range(2, x):         
            if (x % i) != 0:    
                continue
            else:    
                break 
        else:
            pri.append(x)            
    print(len(pri))
main()
