from sys import stdin
def trib(n, back):
    global cont
    cont = cont +1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        acum = 0
        for i in range(1, back+1):
            acum = acum + trib(n - i, back)
        return acum
    
def main():
    global cont;
    cont = 0
    n = 0
    back = 0
    num = 0
    x = list(map(int,stdin.readline().strip().split()))
    while x[0]<= 61 and x[1]<= 60:
        num += 1
        trib(x[0],x[1])
        print("Case",num,":",cont)
        cont = 0
        x = list(map(int,stdin.readline().strip().split()))
        
main()
