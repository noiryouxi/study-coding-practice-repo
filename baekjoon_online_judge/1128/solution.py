import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
items = [tuple(map(int, input().split())) for _ in range(N)]

# 무게 기준 정렬
items.sort()

# prefix sum
psw = [0] * N
psc = [0] * N

psw[0] = items[0][0]
psc[0] = items[0][1]

for i in range(1, N):
    psw[i] = psw[i-1] + items[i][0]
    psc[i] = psc[i-1] + items[i][1]

C = int(input())

# 메모이제이션
from functools import lru_cache

@lru_cache(None)
def rec(p, C, usedBig):
    if p < 0:
        return 0
    
    # 전부 담기 가능
    if psw[p] <= C:
        return psc[p]
    
    w, v = items[p]
    
    # 선택 불가능
    if w > C:
        return rec(p-1, C, False)
    
    # 같은 무게 중복 방지
    if not (usedBig or (p == N-1 or items[p+1][0] != w)):
        return rec(p-1, C, False)
    
    # 분기 순서: 선택 먼저
    take = rec(p-1, C - w, True) + v
    skip = rec(p-1, C, False)
    
    return take if take > skip else skip

print(rec(N-1, C, True))