import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    j = i + 1
    print(" " * (n - j) +"*" * j)