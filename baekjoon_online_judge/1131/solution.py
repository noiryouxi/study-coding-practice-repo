import sys
input = sys.stdin.readline

A, B, K = map(int, input().split())

# 자리수 K제곱 합
def next_num(x):
    res = 0
    while x > 0:
        d = x % 10
        res += d ** K
        x //= 10
    return res

MAX = 4000000
dp = [0] * (MAX + 1)
visited = [0] * (MAX + 1)

def solve(start):
    stack = []
    cur = start
    
    while True:
        if dp[cur] != 0:
            result = dp[cur]
            break
        
        if visited[cur]:
            # 사이클 발견
            cycle_min = cur
            idx = len(stack) - 1
            while stack[idx] != cur:
                cycle_min = min(cycle_min, stack[idx])
                idx -= 1
            result = cycle_min
            break
        
        visited[cur] = 1
        stack.append(cur)
        cur = next_num(cur)
    
    # 경로 역으로 채우기
    for x in reversed(stack):
        result = min(result, x)
        dp[x] = result
        visited[x] = 0  # 초기화
    
    return dp[start]

# 전체 계산
answer = 0
for i in range(A, B + 1):
    answer += solve(i)

print(answer)