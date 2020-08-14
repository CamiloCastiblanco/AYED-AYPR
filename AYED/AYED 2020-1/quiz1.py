def cantidad(z):
    r = []
    acum = 0
    m = []
    for i in z:
        for j in range(len(i)):
            r.append(i[j])
    for i in r:
        m.append(r.count(i))        
    return m
        
def diferentes(z):
    r = []
    acum = 0
    for i in z:
        for j in range(len(i)):
            if i[j] not in r:
                r.append(i[j])
    for i in r:
        acum += i
    
    return r, acum
        
def main():
    m = int(input().strip())
    n = int(input().strip())
    z =[]
    d = []
    h = 0
    if m <= 40 and n <= 60:
        z = [[[0] for j in range(n)] for i in range (m)]
        for i in range(m):
            for j in range(n):
                x = int(input())
                z[i][j] = x
        d, h = diferentes(z)
        print(len(d))
        print(cantidad(z))
        """d es la lista de los numeros diferentes y lo que retorna 'Cantidad(z)' es las veces que está repetido cada numero"""
    else:
        print('Error!')        
main()
                
                
