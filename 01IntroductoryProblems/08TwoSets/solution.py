import sys
input = sys.stdin.readline

def two_sets(n):

    sum1 = 0
    set1 = []
    sum2 = 0
    set2 = []

    for i in range(n, 0, -1):
        if sum1 < sum2:
            sum1 += i
            set1.append(i)
        else:
            sum2 += i
            set2.append(i)

    set1.reverse()
    set2.reverse()
    
    if sum1 == sum2:
        return "YES", set1, set2
    return "NO", None, None






def main():
    n = int(input())
    result, set1, set2 = two_sets(n)
    print(result)

    if result == "YES":
        print(len(set1))
        print(" ".join(map(str, set1)))
        print(len(set2))
        print(" ".join(map(str, set2)))
    






if __name__ == '__main__':
    main()