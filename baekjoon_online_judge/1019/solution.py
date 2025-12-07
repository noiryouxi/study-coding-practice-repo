N = int(input())

count = [0] * 10
x = 1

while x <= N:
    left = N // (x * 10)
    cur = (N // x) % 10
    right = N % x

    for d in range(10):
        count[d] += left * x
        if cur > d:
            count[d] += x
        elif cur == d:
            count[d] += right + 1

    # leading zero 보정
    count[0] -= x

    x *= 10

print(*count)