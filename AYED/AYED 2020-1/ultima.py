
def f(b,p):
    b = b.upper()
    p = p+1
    if b != "#":
        
        if b == "HELLO":
            print("Case",str(p)+": ENGLISH")
            f(str(input()),p)
            
        elif b == "HOLA":
            print("Case",str(p)+": SPANISH")
            f(str(input()),p)
            
        elif b == "HALLO":
            print("Case",str(p)+": GERMAN")
            f(str(input()),p)
            
        elif b == "BONJOUR":
            print("Case",str(p)+": FRENCH")
            f(str(input()),p)
            
        elif b == "CIAO":
            print("Case",str(p)+": ITALIAN")
            f(str(input()),p)
            
        elif b == "ZDRAVSTVUJTE":
            print("Case",str(p)+": RUSSIAN")
            f(str(input()),p)
            
        else:
            print("Case",str(p)+": UNKNOWN")
            f(str(input()),p)
def main():
    b = str(input())
    p = 0
    f(b,p)
main()
    
