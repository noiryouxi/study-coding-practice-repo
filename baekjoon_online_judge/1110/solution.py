import sys
n = int(sys.stdin.readline().rstrip())
e = n
a = 0 
while True:
    b = n // 10
    c = n % 10
    d = c + b
    f = d % 10
    n = f + (c * 10)
    a = a + 1
    if(n == e):
        break
print(a)