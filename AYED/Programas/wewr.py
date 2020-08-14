import sys
def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        tabla = []
        tabla.append("1")
        tabla.append(tabla)
    print(tabla)
main()
