import sys
input = sys.stdin.readline

def bit_strings(n):
    MOD = 10**9 + 7
    return 2**n % MOD






def main():
    n = int(input())
    result = bit_strings(n)
    print(result)






if __name__ == '__main__':
    main()