import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

Z = (100 * Y) // X

# 승률이 절대 변하지 않는 경우
if Z >= 99:
    print(-1)
    sys.exit()

left, right = 1, 10**9
answer = -1

while left <= right:
    mid = (left + right) // 2
    new_Z = (100 * (Y + mid)) // (X + mid)
    
    if new_Z > Z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)