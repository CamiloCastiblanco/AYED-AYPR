from sys import stdin
def deep(iterador,valor):
    global imp,aj,bol
    if valor:
        valor = False
    else:
        valor = True
    for i in aj[iterador]:
        if bol[i] == None:
            bol[i] = valor
            deep(i,valor)
        elif bol[i] == valor:
            pass
        else:
            imp = 0
            return
def main():
    while True:
        global imp,aj,bol 
        imp = 1
        k = int(stdin.readline().strip())
        if k == 0:
            break
        aj = [[] for i in range(k)]
        bol = [None for k in range(k)]
        z = int(stdin.readline().strip())
        for i in range(z):
            a,b = [int(i) for i in stdin.readline().strip().split()]
            aj[a].append(b)
            aj[b].append(a)
        bol[0] = True
        deep(0,True)
        if imp:
            print('BICOLORABLE.')
        else:print('NOT BICOLORABLE.')
        
main()
