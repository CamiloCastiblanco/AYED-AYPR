from sys import stdin
import math

ASCII_EXTENDED_SIZE = 255

# Memoria y tiempo
# Mas memoria, menor tiempo
# Mas tiempo, menos memoria

#int, chr, boolean, str, array, ......
#str = array[chr]
def findMaxCharOcurrence(word):
    ocurrencies = [ 0 for i in range(ASCII_EXTENDED_SIZE)]
    #Recorrido de los elementos en la palabra
    maxOcurrencies, maxCharacter = -math.inf, None
    for character in word:
        ascci_code = ord(character) # chr - Usa la tabla ascii cómo función de orden
        ocurrencies[ascci_code]+=1
        #Verificar que el caracter nuevo supere el maximo local
        if ocurrencies[ascci_code] > maxOcurrencies:
            maxOcurrencies, maxCharacter = ocurrencies[ascci_code], character
        # En caso de disparidad, tomar el caracter lexicograficamente menor
        if ocurrencies[ascci_code] == maxOcurrencies:
            maxOcurrencies, maxCharacter = ocurrencies[ascci_code], chr(min(ord(maxCharacter), ord(character)))

    return maxOcurrencies, maxCharacter

def main():
    word = stdin.readline().strip()
    while word:
        print(findMaxCharOcurrence(word))
        word = stdin.readline().strip()

if __name__ == '__main__':
    main()