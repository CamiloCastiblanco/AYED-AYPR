def main():
    
    x = int(input())
    for _ in range(1,x+1):
        b = list(map(int,input().split()))
        b.sort()
        b.reverse()
        print('Case %d:' %_ ,b[0])
    
main()
