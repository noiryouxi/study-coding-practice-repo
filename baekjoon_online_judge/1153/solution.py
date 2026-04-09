import sys
input = sys.stdin.readline

N = int(input())

# 1. 예외 처리
if N < 8:
    print(-1)
    exit()

# 2. 소수 구하기 (에라토스테네스의 체)
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 3. 기본 두 수 먼저 선택
if N % 2 == 0:
    a, b = 2, 2
    remainder = N - 4
else:
    a, b = 2, 3
    remainder = N - 5

# 4. 나머지를 두 소수의 합으로
for i in range(2, remainder):
    if is_prime[i] and is_prime[remainder - i]:
        print(a, b, i, remainder - i)
        break