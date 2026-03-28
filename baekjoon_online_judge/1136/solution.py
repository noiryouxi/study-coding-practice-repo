import sys
input = sys.stdin.readline

INF = 10**9 + 7

n, m = map(int, input().split())
v = list(map(int, input().split()))

v.sort()
v.append(INF)

# suffix min
suffix_min = [0] * (m + 1)
suffix_min[m] = INF
for i in range(m - 1, -1, -1):
    suffix_min[i] = min(v[i], suffix_min[i + 1])

DP = [[-1] * (n + 1) for _ in range(m + 1)]
DP[0][0] = v[0]

for c in range(m):
    val = v[c]
    mn = suffix_min[c + 1]
    
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if DP[i][j] == -1:
                continue
            if j + val > n:
                continue
            
            if i == c:
                DP[i + 1][j + val] = mn
            else:
                DP[i + 1][j + val] = max(DP[i + 1][j + val], DP[i][j])

ans = m

for i in range(m):
    for j in range(n + 1):
        if DP[i][j] == -1:
            continue
        if (n - j) < DP[i][j] * (i + 1):
            ans = min(ans, i)

print(ans)