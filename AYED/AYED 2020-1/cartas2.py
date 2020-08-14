from sys import stdin
import queue
def main():
    n = int(stdin.readline().strip())
    while n != 0:
        fifo = queue.Queue()
        resul = []
        for  i in range (1,n+1):
            fifo.put(i)
        while fifo.qsize() > 1:
            x = fifo.get()
            resul.append(str(x))
            x = fifo.get()
            fifo.put(x)
        sep = ', '
        print("Discarded cards:",sep.join(resul))
        print("Remaining card:",fifo.get())
            
            
        n = int(stdin.readline().strip())
main()
