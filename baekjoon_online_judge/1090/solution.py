import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

xs = [p[0] for p in points]
ys = [p[1] for p in points]

INF = 10**18
answer = [INF] * (N + 1)

for tx in xs:
    for ty in ys:
        dist = []
        for x, y in points:
            dist.append(abs(x - tx) + abs(y - ty))
        dist.sort()
        
        s = 0
        for k in range(N):
            s += dist[k]
            answer[k + 1] = min(answer[k + 1], s)

print(*answer[1:])