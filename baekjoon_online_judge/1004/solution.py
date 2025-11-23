import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        # 출발점과 도착점이 원 내부에 있는지 판정
        d1 = (x1 - cx)**2 + (y1 - cy)**2 < r*r
        d2 = (x2 - cx)**2 + (y2 - cy)**2 < r*r
        
        # 하나만 내부에 있으면 경계 1번 통과
        if d1 != d2:
            count += 1
    
    print(count)