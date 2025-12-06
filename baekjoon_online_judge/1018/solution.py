N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

def count_repaint(x, y):
    # 패턴1: (x,y)이 W로 시작
    repaint_w = 0
    # 패턴2: (x,y)이 B로 시작
    repaint_b = 0

    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            # (i+j)%2 == 0 → 시작색
            if (i + j) % 2 == 0:
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
    return min(repaint_w, repaint_b)

result = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, count_repaint(i, j))

print(result)