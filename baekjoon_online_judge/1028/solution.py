import sys
input = sys.stdin.readline

R, C = map(int, input().split())
mine = [list(map(int, input().strip())) for _ in range(R)]

dl = [[0]*C for _ in range(R)]
dr = [[0]*C for _ in range(R)]
ul = [[0]*C for _ in range(R)]
ur = [[0]*C for _ in range(R)]

# down-left, down-right
for r in range(R-1, -1, -1):
    for c in range(C):
        if mine[r][c] == 1:
            dl[r][c] = 1 + (dl[r+1][c-1] if r+1 < R and c-1 >= 0 else 0)
            dr[r][c] = 1 + (dr[r+1][c+1] if r+1 < R and c+1 < C else 0)

# up-left, up-right
for r in range(R):
    for c in range(C):
        if mine[r][c] == 1:
            ul[r][c] = 1 + (ul[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0)
            ur[r][c] = 1 + (ur[r-1][c+1] if r-1 >= 0 and c+1 < C else 0)

ans = 0

for r in range(R):
    for c in range(C):
        if mine[r][c] == 1:
            max_k = min(dl[r][c], dr[r][c])
            for k in range(max_k, ans, -1):
                br = r + 2*(k-1)
                if br < R and ul[br][c] >= k and ur[br][c] >= k:
                    ans = k
                    break

print(ans)