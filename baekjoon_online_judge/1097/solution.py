import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
words = [input().strip() for _ in range(N)]
K = int(input().strip())

def get_min_period(s):
    L = len(s)
    for p in range(1, L + 1):
        if L % p != 0:
            continue
        block = s[:p]
        if block * (L // p) == s:
            return p
    return L

answer = 0

for perm in permutations(words):
    T = ''.join(perm)
    L = len(T)
    
    p = get_min_period(T)
    
    if L // p == K:
        answer += 1

print(answer)