import sys
input = sys.stdin.readline

INF = 10**9

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t, level):
        from collections import deque
        q = deque([s])
        level[:] = [-1] * self.n
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def dfs(self, u, t, f, level, work):
        if u == t:
            return f
        for i in range(work[u], len(self.graph[u])):
            work[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                ret = self.dfs(v, t, min(f, cap), level, work)
                if ret:
                    self.graph[u][i][1] -= ret
                    self.graph[v][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        while self.bfs(s, t, level):
            work = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, work)
                if not f:
                    break
                flow += f
        return flow


# 입력
N = int(input())
A = [input().strip() for _ in range(N)]

K = int(input())

have = []
for _ in range(N):
    data = list(map(int, input().split()))
    have.append(data[1:])

office = []
for _ in range(N):
    data = list(map(int, input().split()))
    office.append(data[1:])

answer = 0

# 회사별로 처리
for c in range(K):
    S = N
    T = N + 1
    mf = Dinic(N + 2)

    has = [False] * N
    can = [False] * N

    for i in range(N):
        if c in have[i]:
            has[i] = True
        if c in office[i]:
            can[i] = True

    for i in range(N):
        if has[i]:
            mf.add_edge(S, i, INF)
        elif not can[i]:
            mf.add_edge(i, T, INF)

    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] == '1':
                mf.add_edge(i, j, 1)
                mf.add_edge(j, i, 1)

    answer += mf.max_flow(S, T)

print(answer)