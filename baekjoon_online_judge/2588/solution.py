a = int(input())
b = int(input())
c = b//100
d = b//10 - c*10
f = b - c*100 - d*10
print(a*f)
print(a*d)
print(a*c)
print(a*b)