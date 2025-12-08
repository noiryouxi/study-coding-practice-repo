from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
dq = deque(range(1, N+1))

answer = 0

for target in targets:
    idx = dq.index(target)  # 현재 target이 있는 위치 (0-based)
    
    # 왼쪽 회전이 빠른 경우
    if idx <= len(dq) // 2:
        answer += idx
        dq.rotate(-idx)
    # 오른쪽 회전이 빠른 경우
    else:
        answer += len(dq) - idx
        dq.rotate(len(dq) - idx)
    
    dq.popleft()  # 1번 연산 (비용 없음)

print(answer)