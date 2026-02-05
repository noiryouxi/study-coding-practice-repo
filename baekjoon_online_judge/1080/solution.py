import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] ^= 1  # 0->1, 1->0

# 3×3 연산이 불가능한 경우
if N < 3 or M < 3:
    if A == B:
        print(0)
    else:
        print(-1)
    sys.exit()

count = 0

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            count += 1

# 최종 비교
if A == B:
    print(count)
else:
    print(-1)