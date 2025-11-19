import sys
input = sys.stdin.readline
import heapq

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

# 줄 ID 부여
# 0 ~ N-1: 행
# N ~ 2N-1: 열
# 2N: diag ↘
# 2N+1: anti-diag ↙
ROW = 0
COL = N
DIA = 2 * N
ADI = 2 * N + 1

total_lines = 2 * N + 2

# 각 줄별 남은 비용(초기)
remain = [0] * total_lines

# 행
for i in range(N):
    remain[ROW + i] = sum(A[i])
# 열
for j in range(N):
    s = 0
    for i in range(N):
        s += A[i][j]
    remain[COL + j] = s
# diag ↘ (i == j)
s = 0
for i in range(N):
    s += A[i][i]
remain[DIA] = s
# anti-diag ↙ (i + j == N-1)
s = 0
for i in range(N):
    s += A[i][N - 1 - i]
remain[ADI] = s

# 각 줄의 타입/번호 (tie-breaking용)
# type order: row -> col -> diag -> anti
def line_order(lineid):
    if lineid < COL:
        return (0, lineid)   # row
    elif lineid < DIA:
        return (1, lineid - COL)  # col
    elif lineid == DIA:
        return (2, 0)        # diag
    else:
        return (3, 0)        # anti

# min-heap: (remain_cost, type, idx, lineid)
# type, idx는 tie-breaking을 위해 저장
heap = []
for lid in range(total_lines):
    typ, num = line_order(lid)
    heapq.heappush(heap, (remain[lid], typ, num, lid))

# 줄이 끝났는지
done = [False] * total_lines

# 결과 저장: k빙고 달성 시간
answer = [0] * (total_lines + 1)

cur_bingo = 0
time = 0

# 각 칸이 속한 줄 리스트를 미리 만들어두기
# 최대 4개의 줄(row, col, diag, anti)
belongs = [[None] * N for _ in range(N)]  # 칸 당 (row, col, diag?, anti?)
for i in range(N):
    for j in range(N):
        lst = []
        lst.append(ROW + i)
        lst.append(COL + j)
        if i == j:
            lst.append(DIA)
        if i + j == N - 1:
            lst.append(ADI)
        belongs[i][j] = lst

# 메인 루프: 2N+2 줄이 모두 끝날 때까지
finished_count = 0
while finished_count < total_lines:
    rc, typ, num, lid = heapq.heappop(heap)
    
    # lazy check
    if done[lid]:
        continue
    if rc != remain[lid]:
        continue

    # 이 줄을 끝냄
    done[lid] = True
    finished_count += 1

    time += rc
    cur_bingo += 1
    answer[cur_bingo] = time

    # lid 줄의 모든 칸을 순회하며 업데이트
    if lid < COL:
        # row lid: row = lid
        i = lid
        for j in range(N):
            if A[i][j] != 0:
                val = A[i][j]
                # 이 칸은 이제 사용됨 → 0으로 바꿈
                A[i][j] = 0
                # 이 칸이 속한 다른 줄들 업데이트
                for other in belongs[i][j]:
                    if not done[other]:
                        remain[other] -= val
                        otyp, onum = line_order(other)
                        heapq.heappush(heap, (remain[other], otyp, onum, other))

    elif lid < DIA:
        # col lid-N
        j = lid - COL
        for i in range(N):
            if A[i][j] != 0:
                val = A[i][j]
                A[i][j] = 0
                for other in belongs[i][j]:
                    if not done[other]:
                        remain[other] -= val
                        otyp, onum = line_order(other)
                        heapq.heappush(heap, (remain[other], otyp, onum, other))

    elif lid == DIA:
        # diag ↘, i==j
        for i in range(N):
            j = i
            if A[i][j] != 0:
                val = A[i][j]
                A[i][j] = 0
                for other in belongs[i][j]:
                    if not done[other]:
                        remain[other] -= val
                        otyp, onum = line_order(other)
                        heapq.heappush(heap, (remain[other], otyp, onum, other))

    else:
        # anti ↙, i+j==N-1
        for i in range(N):
            j = N - 1 - i
            if A[i][j] != 0:
                val = A[i][j]
                A[i][j] = 0
                for other in belongs[i][j]:
                    if not done[other]:
                        remain[other] -= val
                        otyp, onum = line_order(other)
                        heapq.heappush(heap, (remain[other], otyp, onum, other))

# 출력
out = []
for k in range(1, total_lines + 1):
    out.append(str(answer[k]))

print("\n".join(out))