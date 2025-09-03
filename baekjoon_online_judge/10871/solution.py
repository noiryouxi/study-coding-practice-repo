import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n):
    if l[i] < x :
        print(l[i])