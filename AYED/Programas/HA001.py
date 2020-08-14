import sys
def main():
    n = int(sys.stdin.readline().strip())
    lista = []
    for i in range(n):
        x = int(sys.stdin.readline().strip())
        lista.append(x)
    a = lista.sort()
    for i in range(n):
        print(lista[i])
main()
        
    
