from random import randint
 
def tabla(filas,columnas,num):
    tablero = []
    for i in range(0,filas):
        v = [num]*columnas
        tablero.append(v)
    return tablero


def minas(filas,columnas,tablero,mines):
    mi = 1
    while mi <= mines:
        
        filas1 = randint(0,filas - 1)
        columnas1 = randint(0,columnas - 1)
        tablero[filas1][columnas1] = "*"
        mi = mi + 1 
   
        
    return tablero
            

def main():
    a = str(input()).split(",")
    
    b = int(a[0])
    
    c = int(a[1])
    
    d = int(a[2])

    tablero = tabla(b,c,"0")
    
    tableromin = minas(b,c,tablero,d)
    
    print(tableromin)
 
    
   
main()
