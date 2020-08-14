def main():
    cont = 0
    line= 0
    x = [[000] for i in range(10)]
    n = 0
    while cont < 1000 or n != '100':
        cont += 1
        n = input().strip()
        if int(n[0]) == 2 :
            x[n[1]] = n[2]
        elif int(n[0]) == 3:
            x[n[1]] += n[2]
        elif int(n[0]) == 4:
            x[n[1]] * n[2]
        elif int(n[0]) == 5:
            x[n[1]] = x[n[2]]
        elif int(n[0]) == 6:
            x[n[1]] += x[n[2]]
         
main()
            
            
            
        
