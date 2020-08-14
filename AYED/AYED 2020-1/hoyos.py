def encontrar_hoyos(m,n,matriz):
    resultados = []
    for i in range(1,int(m)+1):
        for j in range(1,int(n)+1):
            if matriz[i][j] < matriz[i-1][j] and matriz[i][j] < matriz[i][j-1] and matriz[i][j] < matriz[i-1][j-1] and matriz[i][j] < matriz[i+1][j] and matriz[i][j] < matriz[i][j+1] and matriz[i][j] < matriz[i+1][j+1] and matriz[i][j] < matriz[i-1][j+1] and matriz[i][j] < matriz[i+1][j-1]:
                resultados.append([matriz[i][j],i-1,j-1])
    return resultados
def main():
    a = open("alturas1.txt","r")
    lineas = a.readlines()
    m,n = lineas[0].split(",")
    resultados = []
    linea = [9999999 for x in range(int(m)+2)]
    matriz =[linea]
    for i in lineas[1:]:
        p = [9999999]
        for j in i.strip().split(","):
            p.append(int(j))
        p.append(9999999)
        matriz.append(p)
    matriz.append(linea)
    x = encontrar_hoyos(m,n,matriz)
    print(x)          
main()
