import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 노드의 개수
parent_info = list(map(int, input().split()))  # 부모 정보
Removed = int(input())  # 삭제할 노드

# 각 부모당 자식의 정보들 -> 자식의 개수가 0인 node가 leaf node
tree = [[] for _ in range(N)]
alive = [True for _ in range(N)]  # 생존 여부
root = 0  # 루트 노드 인덱스

# 트리 구조 만들기
for i in range(N):
    if parent_info[i] != -1:
        tree[parent_info[i]].append(i)  # 자식 추가
    else:
        root = i  # 루트 노드 찾기

# BFS로 삭제된 노드 처리
def BFS(p):
    queue = deque([p])
    visited = [False for _ in range(N)]
    visited[p] = True
    alive[p] = False

    while queue:
        p = queue.popleft()
        for c in tree[p]:
            if not visited[c]:
                queue.append(c)
                visited[c] = True
                alive[c] = False

# 삭제된 노드를 처리하는 함수
def solve(removed_node):
    cnt = 0
    alive[removed_node] = False  # 삭제된 노드는 생존하지 않음

    # root 노드를 삭제하는 경우
    if removed_node == root:
        return 0
    
    # 리프 노드를 삭제하는 경우
    elif len(tree[removed_node]) == 0:
        # 삭제하려는 노드의 부모 인덱스 구하기
        parent_index = 0
        for i, parent in enumerate(tree):
            for child in parent:
                if child == removed_node:
                    parent_index = i
        # 부모에서 삭제된 노드 제거
        tree[parent_index].remove(removed_node)
    # internal 노드를 삭제하는 경우
    else:
        for child in tree[removed_node]:
            BFS(child)

    # 리프 노드 세기
    for i in range(N):
        if alive[i] and len(tree[i]) == 0:
            cnt += 1
    return cnt

# 결과 출력
print(solve(Removed))