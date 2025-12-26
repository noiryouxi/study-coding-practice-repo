def solve():
    N, K = input().split()
    K = int(K)
    n_str = N
    n_len = len(n_str)

    # 서로 다른 숫자 개수 세기
    def bitcount(x):
        return bin(x).count("1")

    answer = None

    # 자릿수 L에 대해 가장 작은 수 찾기
    def dfs(pos, L, tight, used_mask, path):
        nonlocal answer

        if answer is not None:
            return

        used_cnt = bitcount(used_mask)
        remain = L - pos

        # 가지치기
        if used_cnt > K:
            return
        if used_cnt + remain < K:
            return

        if pos == L:
            if used_cnt == K:
                answer = "".join(path)
            return

        # 선택 가능한 숫자 범위
        if tight:
            start = int(n_str[pos])
        else:
            start = 0

        for d in range(start, 10):
            if pos == 0 and d == 0:
                continue  # leading zero 금지

            new_mask = used_mask | (1 << d)
            new_used = bitcount(new_mask)

            if new_used > K:
                continue

            path.append(str(d))
            dfs(
                pos + 1,
                L,
                tight and (d == start),
                new_mask,
                path
            )
            path.pop()

            if answer is not None:
                return

    # 자릿수 증가시키며 탐색
    max_L = n_len + K
    for L in range(max(n_len, K), max_L + 1):
        answer = None
        if L == n_len:
            dfs(0, L, True, 0, [])
        else:
            dfs(0, L, False, 0, [])
        if answer is not None:
            print(answer)
            return


solve()