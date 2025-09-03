import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    c = a + b
    d = i + 1
    print(f"Case #{d}: {a} + {b} = {c}")