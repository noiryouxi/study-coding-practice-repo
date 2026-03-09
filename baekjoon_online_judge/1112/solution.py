import sys

x, b = map(int, sys.stdin.readline().split())

if x == 0:
    print(0)
    exit()

res = []

if b > 0:
    sign = ""
    if x < 0:
        sign = "-"
        x = -x
    
    while x > 0:
        res.append(str(x % b))
        x //= b
    
    print(sign + ''.join(res[::-1]))

else:
    while x != 0:
        r = x % b
        x //= b
        
        if r < 0:
            r += abs(b)
            x += 1
        
        res.append(str(r))
    
    print(''.join(res[::-1]))