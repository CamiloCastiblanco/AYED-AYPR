def encontrar_hoyos(matriz,m,n):
    resultados = []
    for i in range(0,int(m)):
        for j in range(0,int(n)):
            if matriz[i][j] < matriz[i-1][j] and matriz[i][j] < matriz[i][j-1] and matriz[i][j] < matriz[i-1][j-1] and matriz[i][j] < matriz[i+1][j] and matriz[i][j] < matriz[i][j+1] and matriz[i][j] < matriz[i+1][j+1]:
                resultados.append([matriz[i][j],i-1,j-1])
    return resultados
    
def main():
    a = open("alturas3.txt","r")
    lineas = a.readlines()
    m,n = lineas[0].split(",")
    
    linea = [0 for x in range(int(m)+2)]
    matriz =[linea]
    for i in lineas[1:]:
        p = [0]
        for j in i.strip().split(","):
            p.append(int(j))
        p.append(0)
        matriz.append(p)
    matriz.append(linea)
   
    print(encontrar_hoyos(matriz,m,n))
main()
