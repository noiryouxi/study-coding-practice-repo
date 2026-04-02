import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
cost = list(map(float, input().split()))

adj = [[] for _ in range(N)]
for i in range(N):
    s = input().strip()
    for j in range(N):
        if s[j] == 'Y':
            adj[i].append(j)

# Tarjan
visitedOrder = [-1]*N
sccnum = [-1]*N
indegree = [0]*N

stack = []
order = 0
sccCnt = 0
SCC = []

def dfs(now):
    global order, sccCnt
    order += 1
    visitedOrder[now] = order
    parent = order
    stack.append(now)

    for nxt in adj[now]:
        if visitedOrder[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif sccnum[nxt] == -1:
            parent = min(parent, visitedOrder[nxt])
        else:
            indegree[sccnum[nxt]] += 1

    if parent == visitedOrder[now]:
        scc = []
        while True:
            x = stack.pop()
            sccnum[x] = sccCnt
            scc.append(x)
            if x == now:
                break
        SCC.append(scc)

        if stack:  # C++의 if(!s.empty())
            indegree[sccCnt] += 1

        sccCnt += 1

    return parent

for i in range(N):
    if visitedOrder[i] == -1:
        dfs(i)

# SCC 내 최소 비용 찾기
def minValue_withNode(scc):
    mn = 1e9
    node = -1
    for x in scc:
        if cost[x] < mn:
            mn = cost[x]
            node = x
    return node, mn

pCnt = 0.0
pSum = 0.0

# 필수 SCC 처리 (indegree == 0)
for i in range(sccCnt):
    if indegree[i] == 0:
        node, val = minValue_withNode(SCC[i])
        pCnt += 1
        pSum += val
        cost[node] = -1  # 이미 사용

# 나머지 중에서 평균 낮추는 것만 추가
cost.sort()

for c in cost:
    if c == -1:
        continue
    if (pSum + c) / (pCnt + 1) < (pSum / pCnt):
        pSum += c
        pCnt += 1

print(pSum / pCnt)