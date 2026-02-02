import sys
input = sys.stdin.readline

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def inside(a, b, p):
    # p가 선분 a->b의 왼쪽(또는 위)에 있으면 내부
    return cross(a, b, p) >= 0

def intersection(a, b, c, d):
    # 직선 ab 와 cd 의 교점
    A1 = b[1] - a[1]
    B1 = a[0] - b[0]
    C1 = A1 * a[0] + B1 * a[1]

    A2 = d[1] - c[1]
    B2 = c[0] - d[0]
    C2 = A2 * c[0] + B2 * c[1]

    det = A1 * B2 - A2 * B1
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    return (x, y)

def clip(poly, a, b):
    res = []
    n = len(poly)

    for i in range(n):
        cur = poly[i]
        prev = poly[i - 1]

        cur_in = inside(a, b, cur)
        prev_in = inside(a, b, prev)

        if cur_in:
            if not prev_in:
                res.append(intersection(prev, cur, a, b))
            res.append(cur)
        elif prev_in:
            res.append(intersection(prev, cur, a, b))

    return res

def area(poly):
    if len(poly) < 3:
        return 0.0
    s = 0.0
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0

# ---------- 입력 ----------
N, M = map(int, input().split())
A = [tuple(map(float, input().split())) for _ in range(N)]
B = [tuple(map(float, input().split())) for _ in range(M)]

# ---------- 클리핑 ----------
poly = A
for i in range(M):
    poly = clip(poly, B[i], B[(i + 1) % M])
    if not poly:
        break

# ---------- 출력 ----------
print(f"{area(poly):.12f}")