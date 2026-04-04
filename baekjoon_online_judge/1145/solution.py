import math
from itertools import combinations

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm3(a, b, c):
    return lcm(lcm(a, b), c)

nums = list(map(int, input().split()))

answer = float('inf')

for comb in combinations(nums, 3):
    answer = min(answer, lcm3(comb[0], comb[1], comb[2]))

print(answer)