import sys
import math
input = sys.stdin.readline

def normalize(a, b):
    g = math.gcd(a, b)
    a //= g
    b //= g
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return (a, b)

def reflect(px, py, dx, dy):
    # 방향 벡터 dx, dy 기준 반사
    dot = px * dx + py * dy
    norm = dx * dx + dy * dy

    if norm == 0:
        return None

    if (2 * dot * dx) % norm != 0 or (2 * dot * dy) % norm != 0:
        return None

    rx = 2 * dot * dx // norm - px
    ry = 2 * dot * dy // norm - py

    return (rx, ry)

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
S = set(points)

# 특수 케이스
if N == 1:
    x, y = points[0]
    if x == 0 and y == 0:
        print(-1)
    else:
        print(1)
    exit()

candidates = set()

# 1. 단일 점 기반 축 추가 (이게 핵심!)
for x, y in points:
    if x != 0 or y != 0:
        candidates.add(normalize(x, y))

# 2. 점 쌍 기반 축
for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]

        # 중점 방향
        mx, my = x1 + x2, y1 + y2
        if mx != 0 or my != 0:
            candidates.add(normalize(mx, my))

        # 수직 방향
        dx, dy = x2 - x1, y2 - y1
        if dx != 0 or dy != 0:
            candidates.add(normalize(-dy, dx))

# 검증
answer = 0

for dx, dy in candidates:
    ok = True
    for px, py in points:
        rp = reflect(px, py, dx, dy)
        if rp is None or rp not in S:
            ok = False
            break
    if ok:
        answer += 1

print(answer)