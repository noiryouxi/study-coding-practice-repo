import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
pq = []

# 가장자리 먼저 넣기
for i in range(N):
    for j in range(M):
        if i==0 or i==N-1 or j==0 or j==M-1:
            heapq.heappush(pq, (board[i][j], i, j))
            visited[i][j] = True

ans = 0
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while pq:
    h,x,y = heapq.heappop(pq)

    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True

            if board[nx][ny] < h:
                ans += h - board[nx][ny]

            heapq.heappush(pq,(max(h,board[nx][ny]),nx,ny))

print(ans)