def solution(n, w, num):
    # 현재 박스의 위치
    row = (num - 1) // w
    if row % 2 == 0:
        col = (num - 1) % w
    else:
        col = w - 1 - ((num - 1) % w)
    
    answer = 1  # 자기 자신 포함
    
    # 전체 층 수
    max_row = (n - 1) // w
    
    for r in range(row + 1, max_row + 1):
        # 해당 층의 시작 번호
        start = r * w + 1
        end = min(n, (r + 1) * w)
        
        if r % 2 == 0:
            target = start + col
        else:
            target = start + (w - 1 - col)
        
        if target <= end:
            answer += 1
    
    return answer