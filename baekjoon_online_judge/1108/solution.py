import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)     # u -> v
pred = defaultdict(list)      # v <- u
sites = set()

for _ in range(N):
    data = input().split()
    v = data[0]
    k = int(data[1])
    sites.add(v)

    for u in data[2:]:
        sites.add(u)
        graph[u].append(v)
        pred[v].append(u)

target = input().strip()

# 모든 사이트 초기화
for s in sites:
    graph[s]
    pred[s]

# ---------- 경로 존재 확인 ----------
def reachable(start, goal):
    stack = [start]
    visited = set()

    while stack:
        x = stack.pop()
        if x == goal:
            return True
        for nx in graph[x]:
            if nx not in visited:
                visited.add(nx)
                stack.append(nx)
    return False

# ---------- 허용된 간선 ----------
allowed_pred = defaultdict(list)

for v in sites:
    for u in pred[v]:
        # u -> v edge
        if not reachable(v, u):   # v -> ... -> u 없으면 허용
            allowed_pred[v].append(u)

# ---------- 점수 계산 ----------
memo = {}

def score(v):
    if v in memo:
        return memo[v]

    s = 1
    for u in allowed_pred[v]:
        s += score(u)

    memo[v] = s
    return s

print(score(target))