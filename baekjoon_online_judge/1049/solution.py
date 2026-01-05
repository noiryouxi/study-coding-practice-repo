import sys

N, M = map(int, sys.stdin.readline().split())

min_package = float('inf')
min_single = float('inf')

for _ in range(M):
    package, single = map(int, sys.stdin.readline().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

# 경우 1: 전부 낱개
cost1 = N * min_single

# 경우 2: 패키지 + 낱개
cost2 = (N // 6) * min_package + (N % 6) * min_single

# 경우 3: 패키지만
cost3 = (N // 6 + 1) * min_package

print(min(cost1, cost2, cost3))