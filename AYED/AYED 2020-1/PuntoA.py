import sys
class Nodo:
    def __init__(self,val):
        self.val = val
        self.next = None

class Card:
    def __init__(self):
        self.tail = None
        self.head = None
        self.len = 0

    def Mazo(self,val):
        nodo = Nodo(val)

        if self.len==0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo

        self.len += 1

    def Ans(self):
        self.tail = self.head
        self.head = self.tail.next
        
        rta = self.head

        return rta

def main():
    x = int(sys.stdin.readline().strip())

    while x!=0:
        cards = Card()

        rta = []
        
        for i in range(1,x+1):
            cards.Mazo(i)
        for j in range(x):
            rta += [cards.Ans()]

        print(rta)
        x = int(sys.stdin.readline().strip())

main()
