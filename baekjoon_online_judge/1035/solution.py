from itertools import combinations, permutations
from collections import deque

# 입력
board = [list(input().strip()) for _ in range(5)]
stars = [(i, j) for i in range(5) for j in range(5) if board[i][j] == '*']
k = len(stars)

# 연결 여부 확인
def is_connected(cells):
    q = deque([cells[0]])
    visited = {cells[0]}
    cell_set = set(cells)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if (nx, ny) in cell_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return len(visited) == len(cells)

# 맨해튼 거리
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

cells = [(i, j) for i in range(5) for j in range(5)]
answer = float('inf')

# 모든 k칸 조합 탐색
for comb in combinations(cells, k):
    if not is_connected(comb):
        continue

    # 조각 배치 최소 비용
    best = float('inf')
    for perm in permutations(comb):
        cost = sum(dist(stars[i], perm[i]) for i in range(k))
        best = min(best, cost)

    answer = min(answer, best)

print(answer)