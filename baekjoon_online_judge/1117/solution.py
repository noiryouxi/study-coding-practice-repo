import sys
input = sys.stdin.readline

W,H,f,c,x1,y1,x2,y2 = map(int,input().split())

overlap = min(f, W-f)

width = x2-x1
height = y2-y1

doubleWidth = max(0, min(x2, overlap) - x1)
singleWidth = width - doubleWidth

painted = height * (c+1) * (singleWidth + 2*doubleWidth)

print(W*H - painted)