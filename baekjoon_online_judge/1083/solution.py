N = int(input())
A = list(map(int, input().split()))
S = int(input())

for i in range(N):
    if S == 0:
        break

    # S번 이내로 이동 가능한 범위
    max_pos = i
    for j in range(i + 1, min(N, i + S + 1)):
        if A[j] > A[max_pos]:
            max_pos = j

    # max_pos의 값을 i까지 끌어오기
    for j in range(max_pos, i, -1):
        A[j], A[j - 1] = A[j - 1], A[j]
        S -= 1

print(*A)