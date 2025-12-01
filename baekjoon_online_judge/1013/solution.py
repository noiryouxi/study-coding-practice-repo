import re
import sys
input = sys.stdin.readline

pattern = re.compile(r'^(100+1+|01)+$')

T = int(input())
for _ in range(T):
    s = input().strip()
    if pattern.match(s):
        print("YES")
    else:
        print("NO")