from sys import stdin
class matrim(object):
    slots = ['n','back']
    def trib(self, n, back):
        self.n = n
        self.back = back
        global cont
        cont = cont +1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        acum = 0
        for i in range(1, back+1):
            acum = acum + trib(n - i, back)
        return acum
def main():
    global cont;
    cont = 0
    n = 0
    back = 0
    num = 0
    while n <= 61 and back <= 60:
        x = stdin.readline().strip().split(" ")
        n = int(x[0])
        back = int(x[1])
        if n > 61 or back > 60:
            break
        num += 1
        trib(n,back)
        print("Case",num,":",cont)
        cont = 0
        
        
main()
