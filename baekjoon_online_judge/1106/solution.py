import sys

input = sys.stdin.readline

C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

# 최대 고객 수 여유분
max_customer = C + 100

# dp[i] = i명의 고객을 얻기 위한 최소 비용
dp = [float('inf')] * (max_customer + 1)
dp[0] = 0

for cost, customer in cities:
    for i in range(customer, max_customer + 1):
        dp[i] = min(dp[i], dp[i - customer] + cost)

# C명 이상 중 최소 비용
answer = min(dp[C:])
print(answer)