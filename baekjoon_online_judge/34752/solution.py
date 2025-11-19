import sys
input = sys.stdin.readline

N = int(input())

# 1. 에라토스테네스 (10만 이하)
MAXV = 100000
is_prime = [True] * (MAXV + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXV**0.5) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        for j in range(start, MAXV + 1, step):
            is_prime[j] = False

# prefix sum of primes
prefix = [0] * (MAXV + 1)
for i in range(1, MAXV + 1):
    prefix[i] = prefix[i - 1] + (1 if is_prime[i] else 0)

# 2. 참가자 처리
best_score = -1
best_name = None

worst_score = 10**9
worst_name = None

for _ in range(N):
    name, num = input().split()
    X = int(num[:5])
    Y = int(num[5:])

    lo = min(X, Y)
    hi = max(X, Y)

    score = prefix[hi] - (prefix[lo - 1] if lo > 1 else 0)

    # 행운상 (최대 점수)
    if score > best_score or (score == best_score and name < best_name):
        best_score = score
        best_name = name

    # 불운상 (최소 점수)
    if score < worst_score or (score == worst_score and name < worst_name):
        worst_score = score
        worst_name = name

# 출력
print(best_name)
print(worst_name)