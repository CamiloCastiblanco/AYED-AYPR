from sys import stdin
#No usa docstring.
#No usa documentacion.
#La solución hace lo pedido, pero usa las funciones no permitidas.
#Ciclos mal planteados.
#Corregido por: David garcía y Camilo Castiblanco
"""La funcion toma notas de diferentes estudiantes, las compara y devuelve el promedio, la mayor nota y los que reprobaron
str,str,str... -> str,str,str"""
def mayor(estudiantes):
    may = float(estudiantes[0][1])
    y = estudiantes[0]
    while len(estudiantes) != 1:
        if float(estudiantes[0][1]) > may:
            may = float(estudiantes[0][1])
            y = estudiantes[0]
        else:
            pass
        estudiantes = estudiantes[1:]
    return y
def promedi(estudiantes):
    promedio = 0
    cont = 0
    while len(estudiantes) != 1:
        cont += 1
        promedio = promedio + float(estudiantes[0][1])
        estudiantes = estudiantes[1:]
    return promedio / cont 
def perd(estudiantes):
    rep = 0
    while len(estudiantes) != 1:
        if float(estudiantes[0][1]) < 3.0:
            rep = rep + 1
        else:
            pass
        estudiantes = estudiantes[1:]
    return rep
def main():
    x = stdin.readline().strip().split(",")
    estudiantes = []
    estudiantes = estudiantes + [x]
   
    while len(x) != 1:
        x =stdin.readline().strip().split(",")
        estudiantes = estudiantes + [x]
    m = round(promedi(estudiantes),1) + 0.2
    print("Reprobaron",str(perd(estudiantes)),"estudiantes")
    print("La mejor nota es", mayor(estudiantes)[0],"con",mayor(estudiantes)[1])
    print("La nota promedio es",m)
main()


        
        
        
        

