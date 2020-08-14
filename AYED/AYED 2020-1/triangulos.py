from sys import stdin
def f(cont,z,b,c,p):
    
    if z == b and z == c and c== b:
        
        print("Case",str(p)+": Equilateral")
            
    else:
        if z == b or b == c or c == z:
            print("Case",str(p)+": Isosceles")
        else:
            if z != b and z != c and b != c:
                        
                if (z + b) < c or (z + c) < b or (c + b) < z:
            
                            
                    print("Case",str(p)+": Invalid")
       
                else:
               
                    print("Case",str(p)+": Scalene")
    
def main():
    
                       
    z = int(stdin.readline().strip())
    p = 0
    for x in range(z):
        b,c,d = [int(x) for x in stdin.readline().strip().split()]
        p = p + 1
        f(z,b,c,d,p)
main()
