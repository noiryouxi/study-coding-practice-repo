from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil = [0] * m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):

            if land[i][j] == 1 and not visited[i][j]:

                q = deque([(i, j)])
                visited[i][j] = True

                size = 0
                columns = set()

                while q:
                    x, y = q.popleft()

                    size += 1
                    columns.add(y)

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if (0 <= nx < n and
                            0 <= ny < m and
                            land[nx][ny] == 1 and
                            not visited[nx][ny]):

                            visited[nx][ny] = True
                            q.append((nx, ny))

                # 해당 덩어리가 포함된 모든 열에 크기 누적
                for col in columns:
                    oil[col] += size

    return max(oil)