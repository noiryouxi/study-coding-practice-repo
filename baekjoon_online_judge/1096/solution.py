import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s1 = set()
s2 = set()

now = [[0] * 12 for _ in range(12)]

def f(d, n, type_):
    if type_ == 0:
        for i in range(n):
            s1.add(now[d][i])
    else:
        for i in range(n):
            s2.add(now[d][i])

    for i in range(1, n):
        for j in range(n):
            now[d + 1][j] = 0

        for j in range(i, n):
            now[d + 1][j - i] |= now[d][j]

        for j in range(i - 1, -1, -1):
            now[d + 1][i - 1 - j] |= now[d][j]

        f(d + 1, max(i, n - i), type_)


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 행 경우 생성
    for i in range(n):
        now[0][i] = 1 << i
    f(0, n, 0)

    # 열 경우 생성
    for i in range(m):
        now[0][i] = 1 << i
    f(0, m, 1)

    # 마스크 → 인덱스 리스트 변환
    row_groups = []
    for a in s1:
        rows = []
        for i in range(n):
            if a & (1 << i):
                rows.append(i)
        row_groups.append(rows)

    col_groups = []
    for b in s2:
        cols = []
        for i in range(m):
            if b & (1 << i):
                cols.append(i)
        col_groups.append(cols)

    ans = -10**9

    # 완전 탐색 (비트 연산 없음)
    for rows in row_groups:
        num = [0] * m

        # 필요한 행만 더함
        for r in rows:
            row = board[r]
            for j in range(m):
                num[j] += row[j]

        # 필요한 열만 더함
        for cols in col_groups:
            s = 0
            for c in cols:
                s += num[c]
            if s > ans:
                ans = s

    print(ans)


if __name__ == "__main__":
    solve()