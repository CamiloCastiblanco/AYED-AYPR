def validar_numero(num):
    sumatot = 0
    for i in range(len(num)):
        if i % 2  != 0:
            p = int(num[i])*2
            if len(str(p))>=2:
                suma = 0
                for j in str(p):
                    suma += int(j)
            else:
                suma = p
            sumatot += suma
        else:
            sumatot+= int(num[i])
    if sumatot %10 == 0:
        return True
    else:
        return False
def main():
    num = input()
    print(validar_numero(num))
main()

        
        
