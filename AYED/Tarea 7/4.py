def funa(x,y):
    cont = 0
    for i in y:
        if i == x:
            cont = cont + 1
    return cont


def main():
    lista = []
    x = str(input()) 
    y = str(input()).split(",")
    for i in y:
        
        lista.append(i)

    print(funa(x,lista))

main()


    
