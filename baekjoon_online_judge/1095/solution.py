import sys
input = sys.stdin.readline

def cal(p, n):
    cnt = 0
    while n:
        n //= p
        cnt += n
    return cnt

s, f, m = map(int, input().split())

# 1️ 소수는 m까지만 구하면 충분
limit = m
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit+1, i):
            is_prime[j] = False

primes = [i for i in range(2, limit+1) if is_prime[i]]

# 2️ 조합에서 각 소수의 지수 미리 계산
comb_exp = {}
for p in primes:
    e = cal(p, s+f) - cal(p, s) - cal(p, f)
    if e > 0:
        comb_exp[p] = e

# 3️ m부터 내려가면서 검사
for i in range(m, 0, -1):
    tmp = i
    possible = True
    
    # √i까지만 소인수분해
    for p in primes:
        if p*p > tmp:
            break
        if tmp % p == 0:
            cnt = 0
            while tmp % p == 0:
                tmp //= p
                cnt += 1
            if comb_exp.get(p, 0) < cnt:
                possible = False
                break
    
    # 남은 수가 소수일 경우
    if possible and tmp > 1:
        if comb_exp.get(tmp, 0) < 1:
            possible = False
    
    if possible:
        print(i)
        break