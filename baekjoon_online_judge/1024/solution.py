import sys

def main():
    N, L = map(int, sys.stdin.readline().split())

    for length in range(L, 101):
        S = N - length * (length - 1) // 2
        if S < 0:
            continue
        if S % length == 0:
            x = S // length
            if x >= 0:
                print(" ".join(str(x + i) for i in range(length)))
                return

    print(-1)

if __name__ == "__main__":
    main()