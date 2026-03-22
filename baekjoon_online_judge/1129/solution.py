n = int(input())
b = [0] + list(map(int, input().split()))  # 1-based index

b.sort()

cost = 0

# 앞쪽 (1 → n, +2)
s = 1
while True:
    ps = s
    if s == n:
        break
    s += 2
    if s > n:
        s = n
    cost = max(cost, abs(b[s] - b[ps]))

# 끝 연결
if n % 2 == 1:
    s = n - 1
else:
    s = n - 2

cost = max(cost, abs(b[s] - b[n]))

# 뒤쪽 (n → 1, -2)
while True:
    ps = s
    if s == 2:
        break
    s -= 2
    cost = max(cost, abs(b[s] - b[ps]))

cost = max(cost, abs(b[s] - b[1]))

# 출력 구성
c = [0] * (n + 1)

print(b[1], b[2], end=' ')
c[1] = c[2] = 1

x, y = 2, 1

for i in range(3, n + 1):
    # C++ 코드 그대로 재현 (인덱스 안전 처리 포함)
    if i + 1 <= n and b[i + 1] - b[y] > cost:
        y = i
    else:
        print(b[i], end=' ')
        x = i
        c[i] = 1

for i in range(n, 0, -1):
    if c[i] == 0:
        print(b[i], end=' ')