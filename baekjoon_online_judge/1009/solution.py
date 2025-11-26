import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    a, b = map(int, input().split())
    r = pow(a, b, 10)    # a^b mod 10
    print(10 if r == 0 else r)