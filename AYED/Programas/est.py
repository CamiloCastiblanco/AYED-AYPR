def funa(n):
    if n == 1:
        return 3
    else:
        return funa (n * 2 + 10)
def main():
    n = int(input())
    print(funa(n),"estampillas")
main()
