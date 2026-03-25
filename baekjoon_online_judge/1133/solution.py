import sys
sys.setrecursionlimit(10**7)

K, N, A = map(int, input().split())

result = None

def is_valid(s):
    length = len(s)
    for l in range(1, length // K + 1):
        ok = True
        last = s[length - l:length]
        for i in range(2, K + 1):
            if s[length - i*l:length - (i-1)*l] != last:
                ok = False
                break
        if ok:
            return False
    return True

def dfs(s):
    global result
    if result is not None:
        return

    if len(s) == N:
        result = s
        return

    for i in range(A):
        c = chr(ord('A') + i)
        ns = s + c
        if is_valid(ns):
            dfs(ns)

dfs("")

print(result if result else -1)