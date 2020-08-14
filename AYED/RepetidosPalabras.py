from sys import stdin
def main():
    word = str(stdin.readline().strip())
    x =[]
    count = 0
    p = 0
    for i in word:
        for j in word:
            if i == j :
                count += 1
        x.append([i, count])
        count = 0
    print(x)
main()
