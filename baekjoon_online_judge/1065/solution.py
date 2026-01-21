N = int(input())

count = 0

for i in range(1, N + 1):
    digits = list(map(int, str(i)))
    
    if len(digits) <= 2:
        count += 1
    else:
        diff = digits[1] - digits[0]
        is_hansu = True
        
        for j in range(2, len(digits)):
            if digits[j] - digits[j - 1] != diff:
                is_hansu = False
                break
        
        if is_hansu:
            count += 1

print(count)