import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())

    # 위상정렬 준비
    q = deque()
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = D[i]
        if indegree[i] == 0:
            q.append(i)

    # 위상정렬 진행
    while q:
        now = q.popleft()

        for nxt in graph[now]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[now] + D[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[W])