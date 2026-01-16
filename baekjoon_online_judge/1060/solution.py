import heapq
import sys

input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()
m = {}  # num -> sector count

def get_sector_count(num, part):
    if part < L and S[part] == num:
        return 0

    if part == 0:
        left = 1
        right = S[0] - 1
    elif part == L:
        return -1  # 무한대
    else:
        left = S[part - 1] + 1
        right = S[part] - 1

    return (num - left + 1) * (right - num + 1) - 1


# Python heap은 min-heap → 정렬 기준을 튜플로 변환
# (좋은구간개수, num)
# 단, -1(무한대)는 가장 뒤로 가야 하므로 큰 값으로 치환
INF = 10**30
pq = []

for i in range(L):
    if i == 0:
        left = 1
        right = S[0]
    else:
        left = S[i - 1]
        right = S[i]

    count = 0
    j = left
    while j <= right and count < n:
        if j not in m:
            val = get_sector_count(j, i)
            m[j] = val
            key = INF if val == -1 else val
            heapq.heappush(pq, (key, j))
        j += 1
        count += 1

    count = 0
    j = right
    while j >= left and count < n:
        if j not in m:
            val = get_sector_count(j, i)
            m[j] = val
            key = INF if val == -1 else val
            heapq.heappush(pq, (key, j))
        j -= 1
        count += 1

# 마지막 구간 (무한대)
for i in range(1, n + 1):
    val = S[-1] + i
    m[val] = -1
    heapq.heappush(pq, (INF, val))

# 결과 출력
ans = []
for _ in range(n):
    ans.append(heapq.heappop(pq)[1])

print(*ans)