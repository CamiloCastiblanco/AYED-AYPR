def funa(y,x):
    x = x+(x*2)+10
    
    if  y != 1:
        
        funa((y-1),x)
        
    if y == 1:
        
        print (x,"estampillas")
 


def main():
    
    x = 3
    
    y=int(input())
    
    y = y-1
    
    if y == 0:
        
        print (x,"estampillas")
        
    else:
        
        x = funa(y,x)
        
        
main()
