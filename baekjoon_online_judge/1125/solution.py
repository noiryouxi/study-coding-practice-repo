import sys
input = sys.stdin.readline

def f(x1, y1, x2, y2):
    ret = [0] * 6
    if x1 > x2 or y1 > y2:
        return ret
    if x2 - x1 > 5 and y2 - y1 > 5:
        return ret
    if ((x1 // 5 + y1 // 5) % 2):
        ret[y2 - y1] += x2 - x1
    else:
        ret[x2 - x1] += y2 - y1
    return ret


x1, y1, x2, y2 = map(int, input().split())

r = [0] * 6

xx1 = x1 + (5 - x1 % 5) % 5
yy1 = y1 + (5 - y1 % 5) % 5
xx2 = (x2 // 5) * 5
yy2 = (y2 // 5) * 5

def add(t):
    for j in range(1, 6):
        r[j] += t[j]


if xx1 > xx2 and yy1 > yy2:
    add(f(x1, y1, x2, y2))

elif xx1 > xx2:
    if y1 % 5:
        t = f(x1, y1, x2, (y1 // 5 + 1) * 5)
        add(t)
        y1 = (y1 // 5 + 1) * 5

    if y2 % 5:
        t = f(x1, (y2 // 5) * 5, x2, y2)
        add(t)
        y2 = (y2 // 5) * 5

    i = y1
    while i < y2:
        t = f(x1, i, x2, i + 5)
        add(t)
        i += 5

elif yy1 > yy2:
    if x1 % 5:
        t = f(x1, y1, (x1 // 5 + 1) * 5, y2)
        add(t)
        x1 = (x1 // 5 + 1) * 5

    if x2 % 5:
        t = f((x2 // 5) * 5, y1, x2, y2)
        add(t)
        x2 = (x2 // 5) * 5

    i = x1
    while i < x2:
        t = f(i, y1, i + 5, y2)
        add(t)
        i += 5

else:
    r[5] += ((xx2 - xx1) // 5) * ((yy2 - yy1) // 5) * 5

    if x1 < xx1 and y1 < yy1:
        add(f(x1, y1, xx1, yy1))

    if xx1 < xx2 and y1 < yy1:
        r[5] += ((xx2 - xx1) // 10) * (yy1 - y1)
        r[yy1 - y1] += ((xx2 - xx1) // 10) * 5
        if (xx2 - xx1) % 10 == 5:
            add(f(xx1, y1, xx1 + 5, yy1))

    if xx2 < x2 and y1 < yy1:
        add(f(xx2, y1, x2, yy1))

    if x1 < xx1 and yy1 < yy2:
        r[5] += ((yy2 - yy1) // 10) * (xx1 - x1)
        r[xx1 - x1] += ((yy2 - yy1) // 10) * 5
        if (yy2 - yy1) % 10 == 5:
            add(f(x1, yy1, xx1, yy1 + 5))

    if xx2 < x2 and yy1 < yy2:
        r[5] += ((yy2 - yy1) // 10) * (x2 - xx2)
        r[x2 - xx2] += ((yy2 - yy1) // 10) * 5
        if (yy2 - yy1) % 10 == 5:
            add(f(xx2, yy1, x2, yy1 + 5))

    if x1 < xx1 and yy2 < y2:
        add(f(x1, yy2, xx1, y2))

    if xx1 < xx2 and yy2 < y2:
        r[5] += ((xx2 - xx1) // 10) * (y2 - yy2)
        r[y2 - yy2] += ((xx2 - xx1) // 10) * 5
        if (xx2 - xx1) % 10 == 5:
            add(f(xx1, yy2, xx1 + 5, y2))

    if xx2 < x2 and yy2 < y2:
        add(f(xx2, yy2, x2, y2))


res = 0

res += r[5]
r[5] = 0

k = min(r[4], r[1])
res += k
r[4] -= k
r[1] -= k

k = min(r[3], r[2])
res += k
r[3] -= k
r[2] -= k

k = min(r[3], r[1] // 2)
res += k
r[3] -= k
r[1] -= k * 2

k = min(r[2] // 2, r[1])
res += k
r[2] -= k * 2
r[1] -= k

k = min(r[2], r[1] // 3)
res += k
r[2] -= k
r[1] -= k * 3

res += r[1] // 5
r[1] %= 5

res += r[4]
r[4] = 0

k = min(r[3], r[1])
res += k
r[3] -= k
r[1] -= k

res += r[2] // 2
r[2] %= 2

k = min(r[2], r[1] // 2)
res += k
r[2] -= k
r[1] -= k * 2

res += r[1] // 4
r[1] %= 4

res += r[3]
r[3] = 0

k = min(r[2], r[1])
res += k
r[2] -= k
r[1] -= k

res += r[1] // 3
r[1] %= 3

res += r[2]
r[2] = 0

res += r[1] // 2
r[1] %= 2

res += r[1]

print(res)