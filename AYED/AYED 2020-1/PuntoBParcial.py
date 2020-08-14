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
    while n <= 61 and back <= 60:
        x = stdin.readline().strip().split(" ")
        n = int(x[0])
        back = int(x[1])
        if n > 61 or back > 60:
            break
        num += 1
        trib(n,back)
        print("Case",num,":",cont)
        cont = 0
        
main()
