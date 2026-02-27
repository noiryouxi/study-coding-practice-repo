import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

answer = N - 1

for joker in range(N):
    used = [False] * M
    moves = 0

    for i in range(N):
        if i == joker:
            continue

        color_count = 0
        color_idx = -1

        for j in range(M):
            if boxes[i][j] != 0:
                color_count += 1
                color_idx = j

        if color_count == 0:
            continue
        elif color_count == 1:
            if used[color_idx]:
                moves += 1
            else:
                used[color_idx] = True
        else:
            moves += 1

    answer = min(answer, moves)

print(answer)