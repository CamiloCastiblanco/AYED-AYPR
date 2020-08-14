def funa(a):
    if a < 2:     
        return False
    for i in range(2, a):  
        if a % i == 0:    
            return False
    return True    

def funb(a):  

    cont = 0
  
    for i in range(a):
        if funa(i) == True: 
            cont += 1
            
    return cont 

    
def main() :
    n = int(input())
    print(funb(a))
main()

    

