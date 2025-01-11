import sys
input = sys.stdin.readline

def repetitions(char):
    n = len(char)
    if len(char) == 0:
        return 0

    curr_length = 1
    max_length = 1

    for i in range(1, n):
        if char[i] == char[i-1]:
            curr_length += 1
            max_length = max(curr_length, max_length)
        else:
            curr_length = 1

    return max_length


def main():
    char = str(input())
    result = repetitions(char)
    print(result)


if __name__ == '__main__':
    main()