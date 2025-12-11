import math

N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]

ans = -1

for r in range(N):
    for c in range(M):
        for dr in range(-N+1, N):
            for dc in range(-M+1, M):

                # dr = 0, dc = 0 → 한 칸만 사용 가능
                if dr == 0 and dc == 0:
                    num = int(A[r][c])
                    s = int(math.isqrt(num))
                    if s*s == num:
                        ans = max(ans, num)
                    continue

                x, y = r, c
                num_str = ""

                while 0 <= x < N and 0 <= y < M:
                    num_str += A[x][y]
                    num = int(num_str)

                    s = int(math.isqrt(num))
                    if s*s == num:
                        ans = max(ans, num)

                    x += dr
                    y += dc

print(ans)