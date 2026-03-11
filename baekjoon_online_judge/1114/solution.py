import sys
input = sys.stdin.readline

L, K, C = map(int, input().split())
ks = sorted(set(map(int, input().split())))
ks.append(L)
K = len(ks)

def check(tgt):
    from_pos = L
    cut = C

    for i in range(K-1, -1, -1):
        if from_pos - ks[i] > tgt:
            if ks[i+1] - ks[i] > tgt:
                return -1
            cut -= 1
            from_pos = ks[i+1]
            if cut == 0:
                break

    if cut > 0:
        from_pos = ks[0]

    if from_pos > tgt:
        return -1
    return from_pos


lo = L // (C + 1)
hi = L

while lo < hi:
    mid = (lo + hi) // 2
    if check(mid) != -1:
        hi = mid
    else:
        lo = mid + 1

print(lo, check(lo))