def funcua(var1):
    cuadrantea = var1.split(',')
    x = float(str(cuadrantea[0]))
    y = float(str(cuadrantea[1]))
    if x > 0 and y > 0:
        var1 = "1"
    elif x < 0 and y > 0:
        var1 = "2"
    elif x < 0 and y < 0:
        var1 = "3"
    else:
        var1 = "4"
    return var1
def funcub(var2):
    cuadranteb = var2.split(',')
    a = float(str(cuadranteb[0]))
    b = float(str(cuadranteb[1]))
    if a > 0 and b > 0:
        var2 = "1"
    elif a < 0 and b > 0:
        var2 = "2"
    elif a < 0 and b < 0:
        var2 = "3"
    else:
        var2 = "4"
    return var2
def funcuc(var3):
    cuadrantec = var3.split(',')
    q = float(str(cuadrantec[0]))
    w = float(str(cuadrantec[1]))
    if q > 0 and w > 0:
        var3 = "1"
    elif q < 0 and w > 0:
        var3 = "2"
    elif q < 0 and w < 0:
        var3 = "3"
    else:
        var3 = "4"
    return var3
def main():
    var1= str(input("Digite el primer punto"))
    var2= str(input("Digite el segundo punto"))
    var3= str(input("Digite el tercer punto"))
    v = funcua(var1)
    n= funcub(var2)
    m = funcuc(var3)
    if v == n == m:
        print ("Los cuadrantes son iguales","El primero es",v,"El segundo es",n,"y el tercero es",m)
    else:
        print ("Los cuadrantes son diferentes","El primero es",v,"El segundo es",n,"y el tercero es",m)
main()

