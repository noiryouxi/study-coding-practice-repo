L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

# n이 S에 있으면 좋은 구간은 0개
if n in S:
    print(0)
else:
    left = 0
    right = 0

    for x in S:
        if x < n:
            left = x
        elif x > n:
            right = x
            break

    # 좋은 구간 개수 계산
    result = (n - left) * (right - n) - 1
    print(result)