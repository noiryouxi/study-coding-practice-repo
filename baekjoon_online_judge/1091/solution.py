import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

# 현재 카드 위치
pos = list(range(N))

def check():
    for i in range(N):
        if pos[i] % 3 != P[i]:
            return False
    return True

visited = set()
count = 0

while True:
    # 조건 만족 확인
    if check():
        print(count)
        break
    
    # 상태를 튜플로 저장해서 중복 검사
    state = tuple(pos)
    if state in visited:
        print(-1)
        break
    
    visited.add(state)
    
    # 한 번 섞기
    new_pos = [0] * N
    for i in range(N):
        new_pos[i] = S[pos[i]]
    
    pos = new_pos
    count += 1