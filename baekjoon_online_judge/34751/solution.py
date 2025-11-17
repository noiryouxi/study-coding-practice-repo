import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 총 구간 수
total = N * (N + 1) // 2

cnt1only = 0  # mex = 0
cnt0only = 0  # mex = 1

# 연속된 1 구간 계산
i = 0
while i < N:
    if A[i] == 1:
        j = i
        while j < N and A[j] == 1:
            j += 1
        L = j - i
        cnt1only += L * (L + 1) // 2
        i = j
    else:
        i += 1

# 연속된 0 구간 계산
i = 0
while i < N:
    if A[i] == 0:
        j = i
        while j < N and A[j] == 0:
            j += 1
        L = j - i
        cnt0only += L * (L + 1) // 2
        i = j
    else:
        i += 1

# 나머지 구간은 0과 1이 모두 포함된 구간 → mex = 2
cntboth = total - (cnt1only + cnt0only)

answer = cnt0only * 1 + cntboth * 2  # cnt1only * 0 은 필요 없음

print(answer)