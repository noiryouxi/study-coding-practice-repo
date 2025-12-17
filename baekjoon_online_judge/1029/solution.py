import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    price = [list(map(int, input().strip())) for _ in range(N)]

    INF = 10
    SIZE = 1 << N

    # dp[mask][i] = mask 상태에서 마지막 소유자가 i일 때의 최소 구매 가격
    dp = [[INF] * N for _ in range(SIZE)]

    # 시작 상태: 1번 예술가(0번 인덱스)가 가격 0에 소유
    dp[1][0] = 0

    for mask in range(SIZE):
        for i in range(N):
            if dp[mask][i] == INF:
                continue
            current_price = dp[mask][i]
            for j in range(N):
                if mask & (1 << j):
                    continue
                if price[i][j] >= current_price:
                    new_mask = mask | (1 << j)
                    dp[new_mask][j] = min(dp[new_mask][j], price[i][j])

    answer = 0
    for mask in range(SIZE):
        for i in range(N):
            if dp[mask][i] != INF:
                answer = max(answer, bin(mask).count('1'))

    print(answer)

if __name__ == "__main__":
    main()