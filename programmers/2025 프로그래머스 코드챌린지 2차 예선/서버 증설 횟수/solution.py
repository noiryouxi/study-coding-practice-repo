def solution(players, m, k):
    add = [0] * 24
    current = 0
    answer = 0
    
    for i in range(24):
        if i >= k:
            current -= add[i - k]
        
        need = players[i] // m
        
        if current < need:
            diff = need - current
            add[i] = diff
            current += diff
            answer += diff
    
    return answer