import math

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

# 입력
xA, yA, xB, yB, xC, yC = map(int, input().split())
A = (xA, yA)
B = (xB, yB)
C = (xC, yC)

# 외적으로 일직선 판별
cross = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
if cross == 0:
    print(-1.0)
    exit()

# 세 가지 경우의 둘레
perimeters = [
    2 * (dist(A, B) + dist(A, C)),
    2 * (dist(B, A) + dist(B, C)),
    2 * (dist(C, A) + dist(C, B))
]

# 결과
print(max(perimeters) - min(perimeters))