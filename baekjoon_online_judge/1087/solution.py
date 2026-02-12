import sys
input = sys.stdin.readline

N = int(input())
rats = [tuple(map(int, input().split())) for _ in range(N)]

def F(t):
    xs = []
    ys = []
    for px, py, vx, vy in rats:
        xs.append(px + vx * t)
        ys.append(py + vy * t)
    return max(max(xs) - min(xs), max(ys) - min(ys))

# 삼분 탐색
lo = 0.0
hi = 10000.0

for _ in range(200):  # 충분한 반복 (1e-9 정밀도 확보)
    m1 = (2*lo + hi) / 3
    m2 = (lo + 2*hi) / 3
    
    if F(m1) < F(m2):
        hi = m2
    else:
        lo = m1

answer = F((lo + hi) / 2)
print("{:.15f}".format(answer))