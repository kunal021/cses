import sys
input = sys.stdin.readline

def wierdAlgorithm(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        n //= 2
    elif n % 2 != 0:
        n = n * 3 + 1
    return wierdAlgorithm(n)
    


def main():
    n = int(input())
    wierdAlgorithm(n)

if __name__ == '__main__':
    main()