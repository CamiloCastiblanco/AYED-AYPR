def repe(lista):
    x = []
    for i in lista:
        if int(i) not in x:
            x.append(int(i))
    return x
def main():
    lista = input().strip().split(",")
    l = repe(lista)
    print(str(l).replace("[","").replace("]",""))
main()
