#Brayan Camilo Castiblanco Bernal
#Grupo 3 AYED
#CARNET: 216005
import sys
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.before = None
        self.next = None

    def getData(self):
        return self.data

    def getbefore(self):
        return self.before

    
    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setbefore(self, newbefore):
        self.before = newbefore

    def setNext(self, newNext):
        self.next = newNext
    

# Linked List definition
class LL:
    def __init__(self):
        self.tail = None
        self.head = None

    def addFromTail(self, item):
        node = Node(item)
        if self.head == None and self.tail == None:
            self.tail,self.head = node, node
        else:
            self.tail.setNext(node)
            node.setbefore(self.tail)
            self.tail = node
        
    def addFromHead(self, item):
        node = Node(item)
        if self.head == None and self.tail == None:
            self.tail,self.head = node, node
        else:
            node.setNext(self.head)
            self.head.setbefore(node)
            self.head = node
            
    def hasOne(self):
        return self.tail != None and self.tail.getbefore() == None

    def getTail(self):
        return self.tail

    def print(self):
        tmp = self.tail
        while tmp is not None:
            print(tmp.getData())
            tmp = tmp.getbefore()
        
            
    def pop(self):
        fOne = self.tail
        self.tail = self.tail.getbefore()
        if self.tail is not None:
            self.tail.setNext(None)
        else:
            self.head = None
        fOne.setbefore(None)
        return fOne
        
def main():
    n = int(sys.stdin.readline().strip())
    while n != 0:
        n1 = int(sys.stdin.readline().strip())
        x = LL()
        while n1 != 0:
            n2 = sys.stdin.readline().strip()
            if n2 == "Siguiente":
                if x.getTail() == None:
                    print("No hay fila")
                else:
                    print(x.pop().getData())
            else:
                x.addFromHead(n2)
            
            n1 -= 1
        n -= 1
main()


