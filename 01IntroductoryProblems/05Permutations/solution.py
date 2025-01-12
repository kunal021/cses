import sys
input = sys.stdin.readline

def permutation(n):
    if n == 2 or n == 3:
        return "NO SOLUTION"
    odd = []
    even = []
    
    for i in range(1, n+1, 2):
        odd.append(str(i))
    for i in range(2, n+1, 2):
        even.append(str((i)))

    return " ".join(even + odd)



def main():
    n = int(input())
    result = permutation(n)
    print(result)


if __name__ == '__main__':
    main()