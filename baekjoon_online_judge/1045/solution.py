import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[b] = a
        return True

N, M = map(int, input().split())
adj = [input().strip() for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i+1, N):
        if adj[i][j] == 'Y':
            edges.append((i, j))

if len(edges) < M:
    print(-1)
    sys.exit()

edges.sort()

dsu = DSU(N)
tree = []
extra = []

# 1. 사전순 최대 스패닝 트리
for u, v in edges:
    if dsu.union(u, v):
        tree.append((u, v))
    else:
        extra.append((u, v))

if len(tree) != N - 1:
    print(-1)
    sys.exit()

# 2. 추가 간선 채우기
need = M - (N - 1)
tree.extend(extra[:need])

# 차수 계산
deg = [0] * N
for u, v in tree:
    deg[u] += 1
    deg[v] += 1

print(*deg)