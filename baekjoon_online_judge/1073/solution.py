import sys

def double_factorial(n):
    """n!! 계산 (n은 홀수이거나 -1)"""
    res = 1
    i = n
    while i > 0:
        res *= i
        i -= 2
    return res

def main():
    input = sys.stdin.readline

    N = int(input())
    deg = [0] * 10

    for _ in range(N):
        s = input().strip()
        a = int(s[0])
        b = int(s[1])
        deg[a] += 1
        deg[b] += 1

    ans = 1
    for d in deg:
        # 홀수 차수면 사이클 콜렉션 불가능
        if d % 2 == 1:
            print(0)
            return
        # d = 2k → (2k-1)!!
        if d >= 2:
            ans *= double_factorial(d - 1)

    print(ans)

if __name__ == "__main__":
    main()