from collections import Counter
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
cnt = Counter(nums)
unique = sorted(cnt.keys())

answer = []
found = False

def dfs(prev, depth):
    global found
    if found:
        return
    if depth == N:
        print(*answer)
        found = True
        return

    for x in unique:
        if cnt[x] == 0:
            continue
        if prev is not None and prev + 1 == x:
            continue

        cnt[x] -= 1
        answer.append(x)

        dfs(x, depth + 1)

        answer.pop()
        cnt[x] += 1

        if found:
            return

dfs(None, 0)