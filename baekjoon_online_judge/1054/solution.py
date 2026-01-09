import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
s = [input().strip() for _ in range(N)]
rs = [x[::-1] for x in s]
L = [len(x) for x in s]


def checkin(i, k, j, left):
    if L[k] > j:
        return False
    if left:
        return s[i][j-L[k]:j][::-1] == s[k]
    else:
        return s[i][L[i]-j:L[i]-j+L[k]][::-1] == s[k]


def checkextend(i, k, j, left):
    if L[k] <= j:
        return False
    if left:
        return s[i][:j][::-1] == s[k][:j]
    else:
        return s[i][L[i]-j:][::-1] == s[k][L[k]-j:]


@lru_cache(None)
def dp(taken, i, j, left):
    if j == 0:
        res = 1
        for k in range(N):
            if not (taken >> k) & 1:
                res += dp(taken | (1 << k), k, L[k], 0)
        return res

    res = 0
    for k in range(N):
        if (taken >> k) & 1:
            continue
        if checkin(i, k, j, left):
            res += dp(taken | (1 << k), i, j - L[k], left)
        if checkextend(i, k, j, left):
            res += dp(taken | (1 << k), k, L[k] - j, left ^ 1)
    return res


ans = 0

for i in range(N):
    n = L[i]

    # odd
    for c in range(n):
        l = r = c
        used = -1
        ok = True
        while l >= 0 and r < n:
            if s[i][l] != s[i][r]:
                ok = False
                break
            used += 2
            l -= 1
            r += 1
        if ok:
            ans += dp(1 << i, i, n - used, 1 if l >= 0 else 0)

    # even
    for c in range(n):
        l = c - 1
        r = c
        used = 0
        ok = True
        while l >= 0 and r < n:
            if s[i][l] != s[i][r]:
                ok = False
                break
            used += 2
            l -= 1
            r += 1
        if ok:
            ans += dp(1 << i, i, n - used, 1 if l >= 0 else 0)

print(ans)