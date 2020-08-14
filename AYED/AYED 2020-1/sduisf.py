from sys import stdin
def idioma(palabra):
    if palabra=="HELLO":
        return "ENGLISH"
    elif palabra=="HOLA":
        return "SPANISH"
    elif palabra=="HALLO":
        return "GERMAN"
    elif palabra=="BONJOUR":
        return "FRENCH"
    elif palabra=="CIAO":
        return "ITALIAN"
    elif palabra=="ZDRAVSTVUJTE":
        return "RUSSIAN"
    else:
        return "UNKNOWN"
def main():
    renglon=0
    x=str(stdin.readline().strip())
    while x !="#":
        print("Case",str(renglon+1)+":",idioma(x))
        renglon+=1
        x=str(stdin.readline().strip())
main()
