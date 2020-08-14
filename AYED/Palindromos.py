from sys import stdin
def main():
    word = str(stdin.readline().strip())
    reverse = word[::-1]
    print(reverse == word)
main()
