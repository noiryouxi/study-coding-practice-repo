import sys
import math

input = sys.stdin.readline

x1, y1, z1, x2, y2, z2 = map(int, input().split())
lx, ly, lz = map(int, input().split())

# 1. 꼭짓점 생성
xs = [min(x1, x2), max(x1, x2)]
ys = [min(y1, y2), max(y1, y2)]
zs = [min(z1, z2), max(z1, z2)]

vertices = []
for x in xs:
    for y in ys:
        for z in zs:
            vertices.append((x, y, z))

# 2. 무한대 체크
for x, y, z in vertices:
    if z >= lz:
        print(-1)
        exit()

# 3. 사영
proj = []
for x, y, z in vertices:
    t = lz / (lz - z)
    px = lx + (x - lx) * t
    py = ly + (y - ly) * t
    proj.append((px, py))

# 4. Convex Hull (Monotone Chain)
def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

proj = sorted(set(proj))

if len(proj) <= 1:
    print(0)
    exit()

lower = []
for p in proj:
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in reversed(proj):
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

hull = lower[:-1] + upper[:-1]

# 5. 넓이 계산 (Shoelace)
if len(hull) < 3:
    print(0)
    exit()

area = 0
for i in range(len(hull)):
    x1, y1 = hull[i]
    x2, y2 = hull[(i+1) % len(hull)]
    area += x1*y2 - x2*y1

print(abs(area) / 2)