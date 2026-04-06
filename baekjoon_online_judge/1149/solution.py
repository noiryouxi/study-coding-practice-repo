import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# dp[i][color] : i번째 집을 color로 칠했을 때 최소 비용
dp = [[0]*3 for _ in range(N)]

# 첫 집 초기화
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# DP 진행
for i in range(1, N):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

# 결과 출력
print(min(dp[N-1]))