import sys
from itertools import product

input = sys.stdin.readline

N = int(input())
board = [input().rstrip() for _ in range(5)]

# 숫자 패턴 정의
digits = [
    ["###",
     "#.#",
     "#.#",
     "#.#",
     "###"],

    ["..#",
     "..#",
     "..#",
     "..#",
     "..#"],

    ["###",
     "..#",
     "###",
     "#..",
     "###"],

    ["###",
     "..#",
     "###",
     "..#",
     "###"],

    ["#.#",
     "#.#",
     "###",
     "..#",
     "..#"],

    ["###",
     "#..",
     "###",
     "..#",
     "###"],

    ["###",
     "#..",
     "###",
     "#.#",
     "###"],

    ["###",
     "..#",
     "..#",
     "..#",
     "..#"],

    ["###",
     "#.#",
     "###",
     "#.#",
     "###"],

    ["###",
     "#.#",
     "###",
     "..#",
     "###"]
]

possible = []

# 각 자리마다 가능한 숫자 찾기
for pos in range(N):
    candidates = []
    start_col = pos * 4
    
    for d in range(10):
        ok = True
        for r in range(5):
            for c in range(3):
                if board[r][start_col + c] == '#' and digits[d][r][c] == '.':
                    ok = False
                    break
            if not ok:
                break
        if ok:
            candidates.append(d)
    
    if not candidates:
        print(-1)
        sys.exit()
    
    possible.append(candidates)

# 전체 경우의 수
total_cases = 1
for p in possible:
    total_cases *= len(p)

# 평균 계산
average = 0
for i in range(N):
    weight = 10 ** (N - 1 - i)
    digit_avg = sum(possible[i]) / len(possible[i])
    average += digit_avg * weight

print(average)