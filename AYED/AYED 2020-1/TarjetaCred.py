def multiplo(n):
    s = 0
    t = 0
    g = 0
    for i in range(1,len(n),2):
        x = (int(n) % 10 ** i) 
        print(x,"x")
        k = x * 2
    return k
def funcion(k):
    k = multiplo(n)
    for j in range(0,len(str(k)) + 1):
        m =  (k  % 10 ** j) 
        print(m,"m")
        s += m
        print(s,"s")
    return s    
def validar_numero(n):
    funcion(k)
    for i in range(0,len(n),2):
        p = (int(n) % 10 ** i)
        print(p,"p")
        t += p
        print(t,"t")
    print(g,"g")
    g = s + t
    return g % 10 == 0
def main():
    n = input().strip()
    multiplo(n)
    k = funcion(k)
    l = validar_numero(n)
    print(l)
main()
    
    
    
