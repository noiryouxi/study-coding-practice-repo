import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
values = list(map(int, input().split()))
K = int(input())
M = int(input())

owned = set()
if M > 0:
    owned = set(map(int, input().split()))

# 현재 보유 스티커 가격 합
current_price_sum = sum(prices[i] for i in owned)

# 반으로 나누기
mid = N // 2

left = []
right = []

# 왼쪽 부분집합
for mask in range(1 << mid):
    total_price = 0
    total_value = 0
    for i in range(mid):
        if mask & (1 << i):
            total_price += prices[i]
            total_value += values[i]
    left.append((total_value, total_price))

# 오른쪽 부분집합
for mask in range(1 << (N - mid)):
    total_price = 0
    total_value = 0
    for i in range(N - mid):
        if mask & (1 << i):
            total_price += prices[mid + i]
            total_value += values[mid + i]
    right.append((total_value, total_price))

# 오른쪽을 가치 기준 정렬
right.sort()

# 오른쪽에서 가치가 증가할 때 가격 최소만 남기기
filtered = []
min_price = float('inf')
for v, p in reversed(right):
    min_price = min(min_price, p)
    filtered.append((v, min_price))

filtered.reverse()

import bisect

answer = float('inf')

for lv, lp in left:
    need = K - lv
    if need <= 0:
        answer = min(answer, lp)
        continue
    
    idx = bisect.bisect_left(filtered, (need, -1))
    if idx < len(filtered):
        rv, rp = filtered[idx]
        answer = min(answer, lp + rp)

if answer == float('inf'):
    print(-1)
else:
    print(max(0, answer - current_price_sum))