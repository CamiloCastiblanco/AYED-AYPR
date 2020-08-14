from sys import stdin

def printResult(result):
    for row in result:
        print(' '.join(map(str, row)))

def calculateAmountOfCells(i,j, dimension):
    center = dimension // 2 #División entera
    return 1 + max(abs(center-i), abs(center-j)) # 1 + cantidad de celdas desde i,j al centro

def solveWorderSquare(n):
    dimension = 2*n-1
    result = [[(calculateAmountOfCells(i,j,dimension)) for j in range(dimension)] for i in range(dimension)] # i,j : 0 ... dimension-1
    return result


def main():
    line = stdin.readline().strip()
    while line:
        n = int(line)
        result = solveWorderSquare(n)
        printResult(result)
        line = stdin.readline().strip()


#Scripts bash, OS
if __name__ == '__main__':
    main()