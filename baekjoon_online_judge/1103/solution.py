import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 범위 벗어나거나 구멍이면 종료
    if x < 0 or x >= N or y < 0 or y >= M or board[x][y] == 'H':
        return 0

    # 사이클 발견
    if visited[x][y]:
        print(-1)
        sys.exit(0)

    # 이미 계산된 값이면 반환
    if dp[x][y] != 0:
        return dp[x][y]

    visited[x][y] = True

    move = int(board[x][y])
    max_move = 0

    for i in range(4):
        nx = x + dx[i] * move
        ny = y + dy[i] * move
        max_move = max(max_move, dfs(nx, ny) + 1)

    visited[x][y] = False
    dp[x][y] = max_move
    return dp[x][y]

print(dfs(0, 0))