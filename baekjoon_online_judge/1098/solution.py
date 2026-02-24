import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
p, d = map(int, input().split())

edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        if dist >= d:
            edges.append((dist, i, j))

edges.sort()

max_possible = n * p // 2

dp = {(0,)*n: 0}

max_edges = 0

for dist, u, v in edges:
    new_dp = dp.copy()
    
    for state, cost in dp.items():
        if state[u] < p and state[v] < p:
            new_state = list(state)
            new_state[u] += 1
            new_state[v] += 1
            new_state = tuple(new_state)
            
            new_cost = cost + dist
            
            if new_state not in new_dp or new_dp[new_state] > new_cost:
                new_dp[new_state] = new_cost
    
    # pruning 시작
    
    items = []
    for state, cost in new_dp.items():
        total_deg = sum(state)
        edges_cnt = total_deg // 2
        
        remain_capacity = sum(p - x for x in state) // 2
        
        # 가지치기 1
        if edges_cnt + remain_capacity < max_edges:
            continue
        
        items.append((edges_cnt, cost, state))
    
    # 정렬: 간선 많이, 비용 적게
    items.sort(key=lambda x: (-x[0], x[1]))
    
    # 상위 5000개만 유지
    LIMIT = 5000
    dp = {}
    
    for i in range(min(len(items), LIMIT)):
        edges_cnt, cost, state = items[i]
        dp[state] = cost
        max_edges = max(max_edges, edges_cnt)

# 최종 계산
answer_edges = 0
answer_cost = float('inf')

for state, cost in dp.items():
    total_deg = sum(state)
    if total_deg % 2:
        continue
    
    edges_cnt = total_deg // 2
    
    if edges_cnt > answer_edges:
        answer_edges = edges_cnt
        answer_cost = cost
    elif edges_cnt == answer_edges:
        answer_cost = min(answer_cost, cost)

print(answer_edges, answer_cost)