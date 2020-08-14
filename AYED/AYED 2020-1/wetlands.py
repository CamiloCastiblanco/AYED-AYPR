import sys

dx=[-1,-1,-1, 0, 0, 1, 1, 1]
dy=[-1, 0, 1,-1, 1,-1, 0, 1]

def dfs(i,j):
    global matriz, filas, columnas, cont
    matriz[i][j]="*"
    for k in range(8):
        x=i+dx[k]; y=j+dy[k];
        if x<0 or x>=filas or y<0 or y>=columnas: continue #se salio de la matriz
        elif matriz[x][y]=='W':
            cont+=1
            dfs(x,y)

def main():
    global matriz, filas, columnas, cont
    x = int(sys.stdin.readline().strip())

    sys.stdin.readline()
   
    for cases in range(x):
        matriz = []
        pos = []

        line = sys.stdin.readline().strip()

        while line:
            if ("L" in line) or ("W" in line) or ("L" and "W" in line):
                matriz.append(list(line))
            else:
                pos.append([int(x)for x in line.split()])
            line = sys.stdin.readline().strip()
        filas=len(matriz)
        columnas=len(matriz[0])

        for i,j in pos:
            cont=1
            dfs(i-1,j-1)
            print(cont)

        if cases!=x-1 and x!=1:
            print()
            sys.stdin.readline()

main()
