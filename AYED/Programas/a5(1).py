def main():
    import sys
    num = int(sys.stdin.readline())
    num1=int(sys.stdin.readline())
    num2=int(sys.stdin.readline())
    if (num<num1+num2) and (num1<num+num2) and (num2<num+num1):
        triangulo = "posible"
    else:
        triangulo = "imposible"
    if  triangulo == "posible":
        if num == num1 == num2:
           print("Equilatero,","Perimetro es", num+num1+num2)
        elif num==num1 and num!=num2 and num1!= num2:
            print ("Isosceles,","Diferencia es", num*num1-num2)
        elif num==num2 and num!=num1 and num2!= num1:
            print("Isosceles,","Diferencia es", num*num2-num1)
        elif num1==num2 and num1!=num and num2!=num:
            print("Isosceles,","Diferencia es", num1*num2-num)
        else:
            num != num1 != num2 and num+num1 > num2 and num + num2 > num1 and num1 + num2 > num
            if num > num1 and num > num2 :
                print("Escaleno,","Lado mas largo es",num)
            elif num1 > num and num1 > num2:
                print("Escaleno,","Lado mas largo es",num1)
            else:
                print("Escaleno,","Lado mas largo es",num2)
    if triangulo == "imposible":
        triangulo!="Equilatero"!="Isosceles"!="Escaleno"
        print ("Triangulo Imposible")
main()
            
    
