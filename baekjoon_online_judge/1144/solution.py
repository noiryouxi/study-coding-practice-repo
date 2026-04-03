import sys
input = sys.stdin.readline

INF = 10**9 + 7

n, m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]

cache = [[dict() for _ in range(m)] for _ in range(n)]

def Norm(s):
    check = [0] * 10
    t = 1
    for c in s:
        if c == '0' or check[ord(c) & 15]:
            continue
        check[ord(c) & 15] = chr(t + 48)
        t += 1

    ret = ['0'] * len(s)
    for i, c in enumerate(s):
        if c == '0':
            continue
        ret[i] = check[ord(c) & 15]
    return ''.join(ret)

def Merge(s):
    ret = s[1:]
    if s[0] == '0' and s[-1] == '0':
        ret += '9'
    elif s[0] == '0':
        ret += s[-1]
    elif s[-1] == '0' or s[0] == s[-1]:
        ret += s[0]
    else:
        ret += s[0]
        ret = list(ret)
        for i in range(len(ret)):
            if ret[i] == s[-1]:
                ret[i] = s[0]
        ret = ''.join(ret)
    return Norm(ret)

def Merge2(s):
    ret = s[1:]
    if s[0] == '0':
        ret += '9'
    else:
        ret += s[0]
    return Norm(ret)

def CheckPass(s):
    if s[0] == '0':
        return True
    for i in range(1, len(s)):
        if s[i] == s[0]:
            return True
    return False

def CheckValid(s):
    check = [0] * 10
    for c in s:
        check[ord(c) & 15] = 1
    cnt = sum(check[1:])
    return cnt <= 1

def DFS(x, y, cur):
    if x == n:
        return 0 if CheckValid(cur) else INF

    cur = Norm(cur)

    if cur in cache[x][y]:
        return cache[x][y][cur]

    nx, ny = x, y + 1
    if ny >= m:
        nx += 1
        ny = 0

    ret = INF

    # 선택 안 함
    if CheckPass(cur):
        nxt = cur[1:] + '0'
        ret = min(ret, DFS(nx, ny, nxt))

    # 선택 함
    if y != 0:
        nxt = Merge(cur)
    else:
        nxt = Merge2(cur)

    ret = min(ret, DFS(nx, ny, nxt) + v[x][y])

    # 이미 하나의 연결 요소만 남았으면 종료 가능
    if CheckValid(cur):
        ret = min(ret, 0)

    cache[x][y][cur] = ret
    return ret

print(DFS(0, 0, '0' * m))