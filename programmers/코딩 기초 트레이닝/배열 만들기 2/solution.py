def solution(l, r):
    result = []
    
    for i in range(l, r + 1):
        # 모든 자리가 0 또는 5인지 확인
        if all(ch in ['0', '5'] for ch in str(i)):
            result.append(i)
    
    return result if result else [-1]