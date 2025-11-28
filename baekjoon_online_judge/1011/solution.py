import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x

    k = int(d ** 0.5)

    if d == k * k:
        print(2 * k - 1)
    elif d <= k * k + k:
        print(2 * k)
    else:
        print(2 * k + 1)