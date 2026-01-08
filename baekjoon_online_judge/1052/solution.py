import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 처음부터 조건을 만족하면 0
if bin(N).count('1') <= K:
    print(0)
    sys.exit()

added = 0

while True:
    # 현재 물병 개수의 popcount가 K 이하이면 종료
    if bin(N).count('1') <= K:
        print(added)
        break

    # 가장 낮은 1비트 (2^x)
    lowest_bit = N & -N

    # 해당 비트를 올림시키기 위해 추가
    added += lowest_bit
    N += lowest_bit