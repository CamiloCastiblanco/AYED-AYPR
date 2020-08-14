from sys import stdin
def main():
    y = int(stdin.readline().strip())
    for i in range(y):
        lista = [float(i) for i in stdin.readline().strip().split()]
        lista.reverse()
        y = lista[0]
        constante = lista[1]
        a = lista[2:]
        c = 0
        exp = 1
        res = expo(a,y,c,exp)
        print("p("+str(y)+")="+str(res+constante))
def expo(a,y,c,exp):
    rta = 0
    if c < len(a):
        rta = a[c]*(y**exp) + expo(a,y,c+1,exp+1)
    return rta

main()
