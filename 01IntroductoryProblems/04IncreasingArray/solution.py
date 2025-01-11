import sys
input = sys.stdin.readline

def increasingArray(n, number):
    res = 0

    for i in range(1,n):
        if number[i] < number[i-1]:
            diff = number[i-1] - number[i]
            res += diff
            number[i] = number[i-1]
    return res



def main():
    n = int(input())
    number = list(map(int, input().split()))
    result = increasingArray(n, number)
    print(result)


if __name__ == '__main__':
    main()