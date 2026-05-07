def solution(n):
    board = [[0] * n for _ in range(n)]
    
    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    dir = 0  # 방향 인덱스
    
    for num in range(1, n * n + 1):
        board[x][y] = num
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        # 범위 밖이거나 이미 채워졌으면 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        
        x, y = nx, ny
    
    return board