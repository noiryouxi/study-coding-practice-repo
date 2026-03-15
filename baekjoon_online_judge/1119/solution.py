import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(0)
    exit()

g = [input().strip() for _ in range(N)]
visited = [False] * N

edges = sum(row.count('Y') for row in g) // 2

components = []
for i in range(N):
    if visited[i]:
        continue

    stack = [i]
    visited[i] = True
    size = 0

    while stack:
        cur = stack.pop()
        size += 1
        for nxt in range(N):
            if g[cur][nxt] == 'Y' and not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

    if size == 1:
        print(-1)
        exit()

    components.append(size)

needed_edges = sum(s - 1 for s in components)

extra_edges = edges - needed_edges

if len(components) - 1 <= extra_edges:
    print(len(components) - 1)
else:
    print(-1)