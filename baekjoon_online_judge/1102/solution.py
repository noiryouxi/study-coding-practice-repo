import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
status = input().strip()
P = int(input())

INF = float('inf')

# 초기 상태 비트마스크 만들기
start = 0
for i in range(N):
    if status[i] == 'Y':
        start |= (1 << i)

# 이미 조건 만족
if bin(start).count('1') >= P:
    print(0)
    exit()

# 아무 발전소도 켜져있지 않으면 불가능
if start == 0:
    print(-1)
    exit()

dp = [INF] * (1 << N)
dp[start] = 0

for mask in range(1 << N):
    if dp[mask] == INF:
        continue
    
    # 현재 켜진 발전소 개수
    if bin(mask).count('1') >= P:
        continue
    
    for i in range(N):
        if mask & (1 << i):  # i가 켜져있다면
            for j in range(N):
                if not (mask & (1 << j)):  # j가 꺼져있다면
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(
                        dp[new_mask],
                        dp[mask] + cost[i][j]
                    )

# 정답 찾기
answer = INF
for mask in range(1 << N):
    if bin(mask).count('1') >= P:
        answer = min(answer, dp[mask])

print(answer if answer != INF else -1)