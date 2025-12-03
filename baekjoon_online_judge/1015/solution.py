N = int(input())
A = list(map(int, input().split()))

# (값, 원래 인덱스)
arr = [(A[i], i) for i in range(N)]
arr.sort()  # 값 ↑, 같으면 원래 인덱스 ↑ → 사전순 최소 보장

P = [0] * N

# 정렬된 순서대로 0,1,2,... 할당
for pos, (_, idx) in enumerate(arr):
    P[idx] = pos

print(*P)