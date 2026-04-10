import sys
input = sys.stdin.readline

N = int(input())
adj = [[False] * (N + 1) for _ in range(N + 1)]

# 자기 자신은 제외
for i in range(1, N + 1):
    adj[i][i] = True

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a][b] = True
    adj[b][a] = True

# 보완 그래프에서 색칠
color = [-1] * (N + 1)

from collections import deque

def bfs(start):
    q = deque([start])
    color[start] = 0
    
    while q:
        u = q.popleft()
        for v in range(1, N + 1):
            if u == v:
                continue
            
            # 원래 그래프에서 연결 안 되어 있으면 보완 그래프 간선
            if not adj[u][v]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True

# 모든 정점 검사
for i in range(1, N + 1):
    if color[i] == -1:
        if not bfs(i):
            print(-1)
            exit()

# 결과 출력
teamA = []
teamB = []

for i in range(1, N + 1):
    if color[i] == 0:
        teamA.append(i)
    else:
        teamB.append(i)

# 1번 학생이 포함된 팀 먼저 출력
if 1 in teamB:
    teamA, teamB = teamB, teamA

print(1)
print(*sorted(teamA), -1)
print(*sorted(teamB), -1)