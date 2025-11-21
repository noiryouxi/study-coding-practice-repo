# 테스트 케이스 개수 입력
T = int(input())

# N 최대값 40이므로 DP 테이블 크기 41로 설정
# dp[i] = (0이 출력된 횟수, 1이 출력된 횟수)
dp = [(0, 0)] * 41

# 초기값
dp[0] = (1, 0)  # fibonacci(0): 0을 1번, 1을 0번 출력
dp[1] = (0, 1)  # fibonacci(1): 0을 0번, 1을 1번 출력

# DP 계산
for i in range(2, 41):
    zero_count = dp[i-1][0] + dp[i-2][0]  # fibonacci(i)의 0 출력 횟수
    one_count  = dp[i-1][1] + dp[i-2][1]  # fibonacci(i)의 1 출력 횟수
    dp[i] = (zero_count, one_count)

# 각 테스트 케이스 처리
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])