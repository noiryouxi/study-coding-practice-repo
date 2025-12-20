import sys
sys.setrecursionlimit(10**7)
from math import gcd

def dfs(cur):
    for nxt, p, q in graph[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        # cur / nxt = p / q  → nxt = cur * q / p
        num[nxt] = num[cur] * q
        den[nxt] = den[cur] * p
        dfs(nxt)

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N = int(sys.stdin.readline())
    global graph, visited, num, den
    
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, p, q = map(int, sys.stdin.readline().split())
        graph[a].append((b, p, q))
        graph[b].append((a, q, p))
    
    visited = [False] * N
    num = [0] * N
    den = [0] * N
    
    # 0번 재료 기준
    num[0] = 1
    den[0] = 1
    visited[0] = True
    
    dfs(0)
    
    # 모든 분모의 LCM
    L = 1
    for d in den:
        L = lcm(L, d)
    
    # 정수 질량으로 변환
    mass = [num[i] * (L // den[i]) for i in range(N)]
    
    # 최소화 (전체 GCD로 나누기)
    g = mass[0]
    for m in mass:
        g = gcd(g, m)
    
    mass = [m // g for m in mass]
    print(*mass)

if __name__ == "__main__":
    main()