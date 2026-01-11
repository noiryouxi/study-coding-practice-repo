import sys
sys.setrecursionlimit(10**7)

X0 = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
mn, mx = map(int, sys.stdin.readline().split())

dollar_cnt = S.count('$')
INF = 10**18

# ===============================
# $가 1개인 경우 (특수 케이스)
# ===============================
if dollar_cnt == 1:
    p = S.index('$')
    A = S[:p]
    B = S[p+1:]

    lenA = len(A)
    lenB = len(B)
    len0 = len(X0)

    def get_char(pos):
        # A가 N번 반복
        if pos <= lenA * N:
            return A[(pos - 1) % lenA]
        pos -= lenA * N

        # X0
        if pos <= len0:
            return X0[pos - 1]
        pos -= len0

        # B가 N번 반복
        if pos <= lenB * N:
            return B[(pos - 1) % lenB]

        return '-'

    result = []
    for i in range(mn, mx + 1):
        result.append(get_char(i))
    print("".join(result))
    sys.exit(0)

# ===============================
# 일반 케이스 ($ >= 2)
# ===============================
# 길이 계산
lengths = [len(X0)]
while len(lengths) <= N and lengths[-1] < mx:
    nxt = dollar_cnt * lengths[-1] + (len(S) - dollar_cnt)
    if nxt > INF:
        nxt = INF
    lengths.append(nxt)

useN = min(N, len(lengths) - 1)

def get_char(n, pos):
    if pos <= 0:
        return '-'
    if n == 0:
        if pos > len(X0):
            return '-'
        return X0[pos - 1]

    for c in S:
        if c != '$':
            if pos == 1:
                return c
            pos -= 1
        else:
            if pos <= lengths[n - 1]:
                return get_char(n - 1, pos)
            pos -= lengths[n - 1]
    return '-'

result = []
for i in range(mn, mx + 1):
    result.append(get_char(useN, i))

print("".join(result))