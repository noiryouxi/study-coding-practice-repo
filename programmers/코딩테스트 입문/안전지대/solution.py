def solution(board):
    n = len(board)
    danger = [[False] * n for _ in range(n)]

    # 주변 8방향
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger[i][j] = True

                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = True

    # 위험지역이 아닌 칸의 개수
    answer = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                answer += 1

    return answer