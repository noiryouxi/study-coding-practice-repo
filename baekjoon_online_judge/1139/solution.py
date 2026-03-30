import math
from functools import lru_cache

N = int(input())
arr = list(map(int, input().split()))

# 삼각형 넓이
def area(a, b, c):
    if a + b <= c:
        return 0
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

@lru_cache(None)
def dfs(mask):
    # 모두 사용했으면 끝
    if mask == (1 << N) - 1:
        return 0.0
    
    # 가장 작은 미사용 인덱스 찾기
    for i in range(N):
        if not (mask >> i) & 1:
            break
    
    res = 0.0
    
    # i를 사용하지 않는 경우
    res = dfs(mask | (1 << i))
    
    # i를 포함해서 삼각형 만들기
    for j in range(i + 1, N):
        if (mask >> j) & 1:
            continue
        for k in range(j + 1, N):
            if (mask >> k) & 1:
                continue
            
            a, b, c = sorted([arr[i], arr[j], arr[k]])
            if a + b <= c:
                continue
            
            ar = area(a, b, c)
            new_mask = mask | (1 << i) | (1 << j) | (1 << k)
            res = max(res, dfs(new_mask) + ar)
    
    return res

print(dfs(0))