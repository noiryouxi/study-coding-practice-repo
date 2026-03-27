import sys
sys.setrecursionlimit(10**6)

N = int(input())
parent = list(map(int, input().split()))

tree = [[] for _ in range(N)]

# 트리 구성
for i in range(1, N):
    tree[parent[i]].append(i)

def dfs(node):
    # 리프 노드
    if not tree[node]:
        return 0
    
    times = []
    
    # 자식들 DFS
    for child in tree[node]:
        times.append(dfs(child))
    
    # 오래 걸리는 순으로 정렬
    times.sort(reverse=True)
    
    max_time = 0
    
    for i in range(len(times)):
        # i번째로 전화 → i+1분 후 시작
        max_time = max(max_time, times[i] + i + 1)
    
    return max_time

print(dfs(0))