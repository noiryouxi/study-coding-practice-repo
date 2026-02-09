import sys
input = sys.stdin.readline

n = int(input())
ch = [0] * 15
tmp = [0] * 15

# n == 1
if n == 1:
    p0 = int(input())
    k = int(input())
    if p0 > k:
        print(0)
        print()
        print()
    else:
        print(1)
        print(0)
        print(0)
    sys.exit(0)

# 가격 입력 (한 줄!)
co = list(map(int, input().split()))
k = int(input())

# (cost, digit)
a = []
for i in range(n):
    a.append((co[i], i))

# cost ↑, digit ↓
a.sort(key=lambda x: (x[0], -x[1]))

# === printLen ===
pl = 0

if k < a[0][0]:
    print(0)
    print()
    print()
    sys.exit(0)

if a[0][1] == 0:
    if k < a[1][0]:
        print(1)
        print(0)
        print(0)
        sys.exit(0)
    k -= a[1][0]
    pl = 1

ch[a[0][1]] = k // a[0][0]
ch[a[1][1]] = pl
length = ch[a[0][1]] + pl
print(length)
k %= a[0][0]

# 첫 자리 업그레이드
if pl:
    for i in range(n - 1, a[1][1], -1):
        diff = co[i] - a[1][0]
        if k >= diff:
            k -= diff
            ch[a[1][1]] -= 1
            ch[i] += 1
            break

# === Solve ===
for i in range(n - 1, a[0][1], -1):
    diff = co[i] - a[0][0]
    if diff <= 0:
        continue
    change = min(ch[a[0][1]], k // diff)
    ch[i] += change
    ch[a[0][1]] -= change
    k %= diff

# 앞 50자리
tmp[:] = ch[:]
cnt = 0
for i in range(n - 1, -1, -1):
    while cnt < 50 and ch[i] > 0:
        print(i, end='')
        ch[i] -= 1
        cnt += 1
print()

# 뒤 50자리
ch[:] = tmp[:]
ans = []
cnt = 0
for i in range(n):
    while cnt < 50 and ch[i] > 0:
        ans.append(i)
        ch[i] -= 1
        cnt += 1

ans.reverse()
print("".join(map(str, ans)))