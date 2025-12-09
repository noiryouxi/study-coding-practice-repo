import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

def get_value(r, c):
    m = max(abs(r), abs(c))
    if m == 0:
        return 1

    maxv = (2*m + 1)**2

    if r == m:
        return maxv - (m - c)

    maxv -= 2*m
    if c == -m:
        return maxv - (m - r)

    maxv -= 2*m
    if r == -m:
        return maxv - (c + m)

    maxv -= 2*m
    return maxv - (r + m)

# generate output
table = []
max_len = 0

for r in range(r1, r2 + 1):
    row = []
    for c in range(c1, c2 + 1):
        v = get_value(r, c)
        row.append(v)
        max_len = max(max_len, len(str(v)))
    table.append(row)

for row in table:
    print(" ".join(str(v).rjust(max_len) for v in row))