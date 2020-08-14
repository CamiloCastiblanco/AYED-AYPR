def funa (x):
    m= list (x)
    s=0
    for i in m:
        if s%2==1:
            x="True"
        else:
            x="False"
    return x
    
def main():
    x = str(input("Digite los valores booleanos de la forma 'T' o 'F'"))
    y= funa (x)
    print(y)
main()
    
