def rotar_izquierda(cadena, posiciones):
    return cadena[posiciones:] + cadena[:posiciones]
def rotar_derecha(cadena, posiciones):
    return rotar_izquierda(cadena, -posiciones)
def main():
    x = input().strip().split(" ")
    cadena = x[0]
    posiciones = int(x[-1])
    dire = x[1]
    
    if dire == "izquierda":
        m = rotar_izquierda(cadena, posiciones)
    else:
        rotar_izquierda(cadena, posiciones)
        m = rotar_derecha(cadena, posiciones)
        print(m)
    print(m)
main()
        
    
