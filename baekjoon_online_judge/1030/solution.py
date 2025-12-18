def is_black(s, N, K, r, c):
    start = (N - K) // 2
    end = start + K

    for _ in range(s):
        if start <= r % N < end and start <= c % N < end:
            return 1
        r //= N
        c //= N

    return 0


def main():
    s, N, K, R1, R2, C1, C2 = map(int, input().split())

    for r in range(R1, R2 + 1):
        line = []
        for c in range(C1, C2 + 1):
            line.append(str(is_black(s, N, K, r, c)))
        print("".join(line))


if __name__ == "__main__":
    main()