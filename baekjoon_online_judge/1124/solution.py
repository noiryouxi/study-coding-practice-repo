A, B = map(int, input().split())

# 1. 소수 판별
is_prime = [True] * (B+100)  # 여유분
is_prime[0] = is_prime[1] = False
for i in range(2, int((B+100)**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, B+100, i):
            is_prime[j] = False

# 2. 소인수 개수 계산 (dp 방식)
factor_count = [0] * (B+1)  # factor_count[n] = n의 소인수 개수

for i in range(2, B+1):
    if factor_count[i] == 0:  # 소수이면
        # i는 소수 → factor_count[i] = 1
        for j in range(i, B+1, i):
            n = j
            while n % i == 0:
                factor_count[j] += 1
                n //= i

# 3. 언더프라임 개수 세기
result = 0
for n in range(A, B+1):
    if is_prime[factor_count[n]]:
        result += 1

print(result)