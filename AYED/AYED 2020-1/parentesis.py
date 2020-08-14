from sys import stdin 
def nuevas(listap):
    listaparder = []
    listaparizq = []
    listacorder = []
    listacorizq = []
    listap = list(listap)
    for i in range(len(listap)):
        if listap[i] == '(':
            listaparder += listap[i]
        elif listap[i] == ')':
            listaparizq += listap[i]
        elif listap[i] == '[':
            listacorder += listap[i]
        elif listap[i] == ']':
            listacorizq += listap[i]
    a = len(listaparder) == len(listaparizq)
    b = len(listacorizq) == len(listacorder)
    if a and b:
        return 'Yes'
    else:
        return 'No'
           
def main():
    listap = ""
    n = int(stdin.readline().strip())
    for i in range(n):
        listap = stdin.readline().strip()
        print(nuevas(listap))
main()
    
        
