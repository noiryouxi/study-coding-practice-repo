def solve():
    N = int(input())
    files = [input().strip() for _ in range(N)]

    length = len(files[0])
    result = []

    for i in range(length):
        ch = files[0][i]
        for j in range(1, N):
            if files[j][i] != ch:
                ch = '?'
                break
        result.append(ch)

    print("".join(result))


if __name__ == "__main__":
    solve()