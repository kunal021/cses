import sys
input = sys.stdin.readline

def find_number(y,x):
    
    if y >= x:
        if y % 2 == 0:
            return y**2 - x + 1
        else:
            return (y-1)**2 + x
    else:
        if x % 2 == 0:
            return (x-1)**2 + y
        else:
            return x**2 - y + 1





def main():
    n = int(input())
    result = []
    for _ in range(n):
        y ,x = map(int, input().split())
        result.append(find_number(y,x))

    sys.stdout.write("\n".join(map(str, result)) + "\n")





if __name__ == '__main__':
    main()