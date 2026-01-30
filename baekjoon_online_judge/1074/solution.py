import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

answer = 0

while N > 0:
    half = 1 << (N - 1)
    size = half * half

    if r < half and c < half:          # 1사분면
        pass
    elif r < half and c >= half:       # 2사분면
        answer += size
        c -= half
    elif r >= half and c < half:       # 3사분면
        answer += size * 2
        r -= half
    else:                              # 4사분면
        answer += size * 3
        r -= half
        c -= half

    N -= 1

print(answer)