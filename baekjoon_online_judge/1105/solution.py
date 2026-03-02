L, R = input().split()

# 자릿수가 다르면 무조건 0
if len(L) != len(R):
    print(0)
else:
    count = 0
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                count += 1
        else:
            break
    print(count)