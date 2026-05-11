def solution(a, d, included):
    answer = 0
    value = a
    
    for flag in included:
        if flag:
            answer += value
        value += d
        
    return answer