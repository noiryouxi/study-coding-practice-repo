import sys
input = sys.stdin.readline

mn, mx = map(int, input().split())

size = mx - mn + 1
chk = [False] * size

i = 2
while i * i <= mx:
    sq = i * i
    
    # sq의 첫 배수 구하기
    start = ((mn + sq - 1) // sq) * sq
    
    for j in range(start, mx + 1, sq):
        chk[j - mn] = True
    
    i += 1

print(chk.count(False))