import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 가장 무거운 박스를 못 들면 불가능
if boxes[0] > cranes[0]:
    print(-1)
    exit()

positions = [0] * N      # 각 크레인이 현재 보고 있는 박스 인덱스
visited = [False] * M    # 박스 사용 여부

count = 0
time = 0

while count < M:
    time += 1
    for i in range(N):
        # 이미 모든 박스를 다 확인했다면 패스
        while positions[i] < M:
            if not visited[positions[i]] and cranes[i] >= boxes[positions[i]]:
                visited[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1

print(time)