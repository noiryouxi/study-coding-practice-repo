def solution(info, n, m):
    INF = float('inf')
    
    # dp[b] = B 흔적이 b일 때 A 흔적 최소값
    dp = [INF] * m
    dp[0] = 0
    
    for a, b in info:
        new_dp = [INF] * m
        
        for b_sum in range(m):
            if dp[b_sum] == INF:
                continue
            
            # 1. A가 훔침
            if dp[b_sum] + a < n:
                new_dp[b_sum] = min(new_dp[b_sum], dp[b_sum] + a)
            
            # 2. B가 훔침
            if b_sum + b < m:
                new_dp[b_sum + b] = min(new_dp[b_sum + b], dp[b_sum])
        
        dp = new_dp
    
    answer = min(dp)
    return answer if answer != INF else -1