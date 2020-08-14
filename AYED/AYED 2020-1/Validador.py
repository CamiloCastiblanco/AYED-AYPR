def valid(lista):
    x = list(lista)
    for i in range(len(lista)):
        if lista[i] == 0:
             x[i] = "0"
        elif lista[i] < 0:
            x[i] = "-1"
        else:
            x[i] = "+1"
        
    return x
