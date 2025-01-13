import sys
input = sys.stdin.readline

def trailing_zeros(n):
    count = 0
    while n >=5:
        n //= 5
        count += n
    return count







def main():
    n = int(input())
    result = trailing_zeros(n)
    print(result)






if __name__ == '__main__':
    main()