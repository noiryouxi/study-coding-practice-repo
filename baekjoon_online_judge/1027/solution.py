import sys

def visible_count(i, heights, N):
    count = 0
    hi = heights[i]

    # 오른쪽 빌딩
    max_num = None
    max_den = None
    for j in range(i + 1, N):
        num = heights[j] - hi
        den = j - i
        if max_num is None or num * max_den > max_num * den:
            count += 1
            max_num = num
            max_den = den

    # 왼쪽 빌딩
    max_num = None
    max_den = None
    for j in range(i - 1, -1, -1):
        num = heights[j] - hi
        den = i - j
        if max_num is None or num * max_den > max_num * den:
            count += 1
            max_num = num
            max_den = den

    return count

def main():
    input = sys.stdin.readline
    N = int(input())
    heights = list(map(int, input().split()))

    if N == 1:
        print(0)
        return

    answer = 0
    for i in range(N):
        answer = max(answer, visible_count(i, heights, N))

    print(answer)

if __name__ == "__main__":
    main()