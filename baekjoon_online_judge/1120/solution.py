A, B = input().split()

lenA = len(A)
lenB = len(B)

answer = float('inf')

for i in range(lenB - lenA + 1):
    diff = 0
    for j in range(lenA):
        if A[j] != B[i + j]:
            diff += 1
    answer = min(answer, diff)

print(answer)