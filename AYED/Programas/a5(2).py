from sys import stdin

x= int(stdin.readline())
y = int(stdin.readline())
z = int(stdin.readline())

#definimos triangulo
if (x<y+z) and (y<x+z) and (z<x+y):
    triangulo = "posible"
else:
    triangulo = "imposible"
#definimos que clase de triangulo es
if  triangulo == "posible":   
    if (x!=y!=z):
        tipotriangulo = "Escaleno"
    if (x==y==z):
        tipotriangulo = "Equilatero"
    if (x!=y==z) or (z!=y==x) or (y!=x==z):
        tipotriangulo = "Isosceles"
if triangulo == "imposible":
    triangulo!="Equilatero"!="Isosceles"!="Escaleno"
    print ("Triangulo Imposible")
elif tipotriangulo == "Equilatero":
    perimetro = int (x+y+z)
    print ((tipotriangulo)+",","Perimetro es",(perimetro))
elif tipotriangulo == "Isosceles":
    ladosiguales = (y==z)or(x==z)or(x==y)
    if (y==z):
            print ((tipotriangulo)+",","Diferencia es", (str((y*z)-x)))
    if (x==z):
            print ((tipotriangulo)+",","Diferencia es", (str((x*z)-y)))
    if (x==y):
            print ((tipotriangulo)+",","Diferencia es", (str((x*y)-z)))
else:
    tipotriangulo == "Escaleno"
    mayor = (x)
    if mayor<y :
        mayor = (y)
    elif mayor<z :
        mayor = (z)
    print ((tipotriangulo)+",","Lado mas largo es", (mayor))
