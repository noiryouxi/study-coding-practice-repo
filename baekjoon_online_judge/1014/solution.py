import sys
input = sys.stdin.readline

def solve():
    C = int(input())
    for _ in range(C):
        N, M = map(int, input().split())
        seat = [input().strip() for _ in range(N)]
        
        # 각 행에서 가능한 자리 mask 생성
        avail = []
        for r in range(N):
            mask = 0
            for c in range(M):
                if seat[r][c] == '.':
                    mask |= (1 << c)
            avail.append(mask)

        # 가능한 모든 state 미리 생성
        states = []
        for s in range(1 << M):
            # 같은 행에서 좌우 충돌 체크
            if (s & (s << 1)) == 0:
                states.append(s)

        # DP 테이블
        dp = [dict() for _ in range(N)]
        
        # 첫 행 초기화
        for s in states:
            if (s & avail[0]) == s:
                dp[0][s] = bin(s).count("1")

        # 나머지 행 DP
        for r in range(1, N):
            for s in states:
                if (s & avail[r]) != s:
                    continue  # 놓을 수 없는 자리 포함됨
                    
                cnt = bin(s).count("1")
                for ps in dp[r-1]:
                    # 위 행과 대각선 충돌 체크
                    if (ps & (s << 1)) == 0 and (ps & (s >> 1)) == 0:
                        val = dp[r-1][ps] + cnt
                        if s not in dp[r] or dp[r][s] < val:
                            dp[r][s] = val

        # 마지막 행에서 최대값이 정답
        print(max(dp[N-1].values()))

solve()