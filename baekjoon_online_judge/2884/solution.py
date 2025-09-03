a, b = map(int, input().split())
if b >= 45 :
    print(a, b - 45)
elif a >= 1 :
    print(a - 1, 15 + b)
else :
    print(23 , 15 + b)