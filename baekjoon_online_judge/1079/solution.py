import sys
input = sys.stdin.readline

N = int(input())
guilt_init = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
mafia = int(input())

ans = 0
FULL = (1 << N) - 1

def dfs(alive_mask, guilt, night):
    global ans

    # 마피아 죽음
    if not (alive_mask & (1 << mafia)):
        ans = max(ans, night)
        return

    alive_cnt = alive_mask.bit_count()

    # 시민 전멸
    if alive_cnt == 1:
        ans = max(ans, night)
        return

    # ⭐ 올바른 가지치기
    max_future_nights = alive_cnt // 2
    if night + max_future_nights <= ans:
        return

    # 🌙 밤
    if alive_cnt % 2 == 0:
        for i in range(N):
            if i == mafia:
                continue
            if alive_mask & (1 << i):
                new_guilt = guilt[:]
                for j in range(N):
                    if alive_mask & (1 << j):
                        new_guilt[j] += R[i][j]
                dfs(alive_mask & ~(1 << i), new_guilt, night + 1)

    # ☀️ 낮
    else:
        max_g = -10**9
        target = -1
        for i in range(N):
            if alive_mask & (1 << i):
                if guilt[i] > max_g:
                    max_g = guilt[i]
                    target = i
        dfs(alive_mask & ~(1 << target), guilt, night)

dfs(FULL, guilt_init, 0)
print(ans)