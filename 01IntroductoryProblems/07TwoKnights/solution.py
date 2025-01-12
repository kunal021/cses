import sys
input = sys.stdin.readline

def moves(k):
    if k == 1:
        return 0
    
    totl_placements = ((k*k) * (k*k - 1)) // 2
    if k >= 3:
        attacking_placementd = 4 * (k-1) * (k-2)
    else:
        attacking_placementd = 0

    return totl_placements - attacking_placementd






def main():
    n = int(input())
    result = []
    for i in range(1,n+1):
        result.append(moves(i))

    sys.stdout.write("\n".join(map(str, result)) + "\n")





if __name__ == '__main__':
    main()