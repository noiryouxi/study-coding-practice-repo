MOD = 1000000

N = int(input())

if N == 1:
    print(1)
    exit()

dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]

# 초기값 (길이 2)
dp[2][1][0] = 1  # 감소
dp[2][2][1] = 1  # 증가

for i in range(3, N+1):
    prefix_inc = [0]*(N+2)
    prefix_dec = [0]*(N+2)
    
    for j in range(1, i):
        prefix_inc[j] = (prefix_inc[j-1] + dp[i-1][j][1]) % MOD
        prefix_dec[j] = (prefix_dec[j-1] + dp[i-1][j][0]) % MOD

    for j in range(1, i+1):
        dp[i][j][1] = prefix_dec[j-1] % MOD
        dp[i][j][0] = (prefix_inc[i-1] - prefix_inc[j-1]) % MOD

answer = 0
for j in range(1, N+1):
    answer = (answer + dp[N][j][0] + dp[N][j][1]) % MOD

print(answer)