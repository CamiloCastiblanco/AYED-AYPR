from sys import stdin
def decoder(txt):
    palabra = ""
    cont = 0
    cont1 = 0
    for i in txt:
        if cont1 < len(i):
            palabra += i[cont]
            cont += 1
            cont1 += 1
    return palabra
def main():
    casos = int(stdin.readline().strip())
    x = stdin.readline().strip()
    for i in range(casos):
        line = stdin.readline().strip().split()
        print("Case #" ,str(i + 1), ":")
        while line != []:
            print(decoder(line))
            line = stdin.readline().strip().split()
        if line != []:
            print()
main()
