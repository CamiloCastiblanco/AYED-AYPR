def funa (var1):
    x=str(int(var1))
    primero = int(str(x[0]))
    segundo = int(str(x[1]))
    tercero = int(str(x[2])) 
    cuarto = int(str(x[3]))  
    quinto = int(str(x[4]))
    sexto = int(str(x[5]))
    septimo = int(str(x[6]))
    octavo = int(str(x[7]))  
    noveno = int(str(x[8]))  
    decimo = int(str(x[9]))
    var1 = primero + segundo + tercero + cuarto + quinto + sexto + septimo + octavo + noveno
    return var1
def funb (var1):
    var1 = funa (var1) 
    if var1 % 10 == 0 and var1 == 20:
        var1 = "El numero es invalido"
    else:
        var1 = "El numero es valido"
    return var1 
                 
def main():
    var1= int(input("Digite el numero de diez digitos"))
    y = funb (var1)
    print(y)
main()
