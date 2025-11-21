import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    d_sq = dx*dx + dy*dy
    d = math.sqrt(d_sq)
    
    if d == 0 and r1 == r2:
        print(-1)
    elif d > r1 + r2 or d < abs(r1 - r2):
        print(0)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    else:
        print(2)