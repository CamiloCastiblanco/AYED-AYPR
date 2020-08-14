from sys import stdin
def main():
    z = int(stdin.readline().strip())
    for i in range(z):
        m = 0
        g = 0
        b,c,d = [int(j) for j in stdin.readline().strip().split()]
        n = [int(k) for k in stdin.readline().strip().split()]
        lis = n[0:c]
        for s in lis:
            m+=s
            if m <= d:
                g+=1
        print("Case "+str(i+1)+":",g)
main()
       
