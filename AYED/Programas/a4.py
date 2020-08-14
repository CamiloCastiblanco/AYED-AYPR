def main():
    x=str(input())
    y=str(input())
    fila1=x.split(' ')
    fila2=y.split(' ')    
    A=str((int(str(fila1[0]))*int(str(fila2[1])))-(int(str(fila1[1]))*int(str(fila2[0])))) 
    print('|A|'+'='+A)
main()
