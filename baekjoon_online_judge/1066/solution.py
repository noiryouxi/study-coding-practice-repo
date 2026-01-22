import sys
from collections import defaultdict

MOD = 10**9 + 7
input = sys.stdin.readline

N, A = map(int, input().split())

# N = 1 처리
if N == 1:
    print(9 if A == 1 else 0)
    sys.exit(0)

# dp[diff][bef][cnt]
# diff: 0~8, 9는 "아직 공차 없음"
dp = defaultdict(int)

# 초기 두 자리
for i in range(1, 10):
    for j in range(i, 10):
        dp[(j - i, j, 1)] += 1

# 3번째 자리부터 N번째 자리까지
for _ in range(3, N + 1):
    ndp = defaultdict(int)
    for (diff, bef, cnt), val in dp.items():
        for i in range(bef, 10):
            if diff == 9:
                # 새 그룹 시작
                ndp[(i - bef, i, cnt)] = (ndp[(i - bef, i, cnt)] + val) % MOD
            else:
                if i - bef == diff:
                    # 같은 그룹 유지
                    ndp[(diff, i, cnt)] = (ndp[(diff, i, cnt)] + val) % MOD
                else:
                    # 반드시 뒤에서 끊음
                    if cnt + 1 <= A:
                        ndp[(9, i, cnt + 1)] = (ndp[(9, i, cnt + 1)] + val) % MOD
    dp = ndp

# 정답 합산
ans = 0
for (diff, bef, cnt), val in dp.items():
    if cnt == A:
        ans = (ans + val) % MOD

print(ans)