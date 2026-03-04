import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

broken = set()
if M > 0:
    broken = set(input().split())

# 기본값: 100에서 +,-만 눌러 이동
answer = abs(N - 100)

# 숫자를 만들 수 있는지 확인 함수
def can_make(num):
    for ch in str(num):
        if ch in broken:
            return False
    return True

# N 기준으로 위아래 탐색
for diff in range(1000001):
    
    # 아래쪽
    lower = N - diff
    if lower >= 0 and can_make(lower):
        answer = min(answer, len(str(lower)) + diff)
        break
    
    # 위쪽
    upper = N + diff
    if can_make(upper):
        answer = min(answer, len(str(upper)) + diff)
        break

print(answer)