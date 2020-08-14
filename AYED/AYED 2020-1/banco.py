import sys

class Nodo:
    def __init__(self,key):
        self.key = key
        self.next = None

class Banco:
    def __init__(self):
        self.tail = None
        self.head = None
        self.len = 0

    def New(self,val):
        nodo = Nodo(val)
        
        if self.len==0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            self.tail = nodo

        self.len += 1
        
    def Out(self):
        if self.len==0:
            print("No hay fila")
        else:
            print(self.head.key)
            self.head = self.head.next
            self.len -= 1

def main():
    cases = int(sys.stdin.readline().strip())

    for i in range(cases):
        clients = int(sys.stdin.readline().strip())

        b = Banco()

        for j in range(clients):
            person = sys.stdin.readline().strip()

            if person=="Siguiente":
                b.Out()
            else:
                b.New(person)
    
main()
        

    
