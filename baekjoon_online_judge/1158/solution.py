from collections import deque

N, K = map(int, input().split())

dq = deque(range(1, N + 1))
result = []

while dq:
    dq.rotate(-(K - 1))  # K번째 사람을 앞으로
    result.append(dq.popleft())  # 제거

print("<" + ", ".join(map(str, result)) + ">")