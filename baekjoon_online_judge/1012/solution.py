import sys
sys.setrecursionlimit(10**6)

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and field[ny][nx] == 1:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                cnt += 1

    print(cnt)