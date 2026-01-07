import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

max_size = 1  # 최소 정사각형 크기는 1

for i in range(N):
    for j in range(M):
        # 가능한 정사각형 크기
        for k in range(1, min(N - i, M - j)):
            if grid[i][j] == grid[i][j + k] == grid[i + k][j] == grid[i + k][j + k]:
                max_size = max(max_size, k + 1)

# 출력은 넓이이므로 크기의 제곱
print(max_size * max_size)