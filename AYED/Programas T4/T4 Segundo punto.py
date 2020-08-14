def funa(x,y,z):
    if x < y and x < z and y < z:
        var1="True"
    else:
        var1="False"
    return var1
def main():
    var1="True"
    x= float(input("Digite el primer numero"))
    y= float(input("Digite el segundo numero"))
    z= float(input("Digite el tercer numero"))
    m = funa(x,y,z)
    print(m)
main()
