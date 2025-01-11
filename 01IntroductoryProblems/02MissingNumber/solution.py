import sys
input = sys.stdin.readline

def missingNumber(n, number):
    res = set(number)

    for i in range(1, n+1):
        if i not in res:
            return i
        
    return -1



def main():
    n = int(input())
    number = list(map(int, input().split()))
    result = missingNumber(n, number)
    print(result)


if __name__ == '__main__':
    main()