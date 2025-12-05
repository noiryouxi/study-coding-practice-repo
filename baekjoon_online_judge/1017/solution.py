import sys
input = sys.stdin.readline

MAX = 2000
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False

N = int(input())
arr = list(map(int, input().split()))
first = arr[0]

odd, even = [], []
for x in arr:
    (odd if x % 2 else even).append(x)

# first가 홀수면 A=odd, B=even
if first % 2:
    A = odd
    B = even
else:
    A = even
    B = odd

if len(A) != len(B):
    print(-1)
    exit()

n = len(A)
m = len(B)

Ai = A[:]  # 값
Bi = B[:]

# 인덱스 기반 그래프
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if prime[Ai[i] + Bi[j]]:
            graph[i].append(j)

first_idx = Ai.index(first)

def dfs(a, visited):
    for b in graph[a]:
        if visited[b]:
            continue
        visited[b] = True
        if match[b] == -1 or dfs(match[b], visited):
            match[b] = a
            return True
    return False

answers = []

for cand in graph[first_idx]:
    match = [-1] * m
    match[cand] = first_idx  # 고정 매칭

    ok = True
    for a in range(n):
        if a == first_idx:
            continue
        visited = [False] * m

        # 🔴 critical fix: 강제 매칭된 cand 를 DFS에서 절대 사용하지 못하게 막기
        visited[cand] = True

        if not dfs(a, visited):
            ok = False
            break

    if ok:
        answers.append(Bi[cand])

if answers:
    print(*sorted(answers))
else:
    print(-1)