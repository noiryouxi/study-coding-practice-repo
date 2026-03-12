import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

visited = [False] * N
cycles = 0

for i in range(N):
    if not visited[i]:
        cycles += 1
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cur = P[cur]

if cycles == 1:
    print(0)
else:
    print(cycles)