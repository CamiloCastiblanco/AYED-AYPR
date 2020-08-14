def silaba(palabra):
    vocalestil = 'áéíóú'
    if  palabra[len(palabra)-1] in vocalestil :
        return palabra[len(palabra)-1]
    else:
        i = len(palabra)-2
        vocales = 'aeiou'
        bandera = True
        if i<=2:
            return palabra
        else:  
            while i >= 0 and bandera:
                if palabra[i] in vocales or palabra[i] in vocalestil and palabra[i-1] not in vocales:
                    rim = palabra[i:]
                    bandera = False
                i = i -1
            return rim

def rima(lista,palabra,finales):
    for i in range(len(lista)):
        if palabra == lista[i][len(lista[i])-len(palabra):]:
            finales = repetidos(finales,lista[i])
            
    return finales

def repetidos(lista,elemento):
    if elemento not in lista:
        lista = lista + [elemento]
    return lista
    
        
def limpiar(line):
    line = line.replace(',','')
    line = line.replace('.','')
    line = line.replace('-','')
    line = line.split(' ')
    return line

def guardar(finales, palabra):
    resultado = open('resultado.txt','w')
    for i in range(len(finales)):
        resultado.write(finales[i]+'\n')
        
def imprimir(lista,palabra):
    print('Palabras que riman con:',palabra)
    for i in range(len(lista)):
        print(lista[i])

def main():
    nom_archivo = input('Ingrese el nombre del archivo ')
    palabra = input('Ingrese la palabra a buscar ')
    sil = silaba(palabra)
    print(palabra)
    finales = []
    archivo = open(nom_archivo,'r')
    linea = archivo.readline().strip()
    while linea != '':
        linea = limpiar(linea)
        finales = rima(linea,sil,finales)
        linea = archivo .readline().strip()
    archivo.close()
    imprimir(finales,palabra)
    guardar(finales,sil)



main()
    
