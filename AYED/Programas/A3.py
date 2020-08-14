import sys
def main():
    num = int(sys.stdin.readline())
    var2 = (num//1000)
    var3 = ((num-(var2*1000))//100)
    var4 = (num-(var2*1000)-(var3*100))//10
    var5 = (num-(var2*1000)-(var3*100)-(var4*10))
    if var2>var3 and var2>var4 and var2>var5:
        print(var2)
    elif var3>var2 and var3>var4 and var3>var5:
        print(var3)
    elif var4>var3 and var4>var2 and var4>var5:
        print(var4)
    else:
        print(var5)
main()
