def solution(numbers, n):
    total = 0
    
    for x in numbers:
        total += x
        if total > n:
            break
            
    return total