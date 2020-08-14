def f(x,y):
    for i in y:
        
        if i == x:
            return True
            break
        else:
            return False


def main():
    lista = []
    x = str(input()) 
    y = str(input()).split(",")
    for i in y:
        
        lista.append(i)

    print(f(x,lista))

main()

