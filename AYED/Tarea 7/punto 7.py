import sys
"""La funcion toma dos valores y evalua si hay un primo entre los 2 numeros introducidos"""
def gcdlike(p, q):
    if q == 0: return p == 1
    return gcdlike(q, p % q)
def main():
    p = int(sys.stdin.readline())
    q = int(sys.stdin.readline())
    print(gcdlike(p, q))
    print(7%4)
main()
""" Si p = 32 y q = 8 se hace 5 llamados a la recurrencia """
""" Si p = 35 y q = 8 se hace 2 llamados a la recurrencia """
""" Si q es mayor que p no afecta el programa, simplemente sigue haciendo lo que debe de hacer"""
