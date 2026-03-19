import sys
input = sys.stdin.readline

N = int(input())
blocks = list(map(int, input().split()))

MAX = sum(blocks)
dp = [-1] * (MAX + 1)
dp[0] = 0

for h in blocks:
    prev = dp[:] 
    
    for diff in range(MAX - h + 1):
        if prev[diff] == -1:
            continue
        
        # 높은 쪽
        if dp[diff + h] < prev[diff]:
            dp[diff + h] = prev[diff]
        
        # 낮은 쪽
        if diff >= h:
            if dp[diff - h] < prev[diff] + h:
                dp[diff - h] = prev[diff] + h
        else:
            if dp[h - diff] < prev[diff] + diff:
                dp[h - diff] = prev[diff] + diff

print(dp[0] if dp[0] > 0 else -1)