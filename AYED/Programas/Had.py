import sys
def had(s):
    tabla=[[0]*s]*s
    if s == 1:
        print(True)
    elif s == 2:
        print(True,True,True,False)
    else:
        for i in range(s):
            for j in range(s):
                if i < s//2 or j < s//2:
                    tabla[i][j] = True 
                    tabla[i][j+1] = True 
                    tabla[i+1][j] = True 
                    tabla[i+1][j+1] = False 
                else:
                    tabla[i][j] = False 
                    tabla[i][j+1] = False 
                    tabla[i+1][j] = True  
                    tabla[i+1][j+1] = False 
            
def main():
    n = sys.stdin.readline().strip()
    while n != "":
        s = int(n)
        print(had(s))
        n = sys.stdin.readline().strip()
        
main()
