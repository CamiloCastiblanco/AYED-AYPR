from sys import stdin
class DISTRASCHOLTEN:
    def __init__(self,x):
        self.data = [i for i in range(x+1)]
        self.size = x
    def union(self,i,j):
        i = self.ans(i)
        j = self.ans(j)
        if j != i:
            self.data[i] = j
            self.size-=1
    def ans(self,x):
        if self.data[x] != x:
            self.data[x] = self.ans(self.data[x])
        return self.data[x]  
def main():
    z = 1
    while -1:
        x,y = list(map(int,stdin.readline().strip().split()))
        if x == y == 0:
            break
        lista = DISTRASCHOLTEN(x) 
        for i in range(y):
            j,k = list(map(int,stdin.readline().strip().split()))
            lista.union(j,k)
            p = lista.size
        print('Case',str(z)+':',int(p))
        z+=1
main()
