count = 0

for i in range(8):
    row = input().strip()
    for j in range(8):
        if (i + j) % 2 == 0 and row[j] == 'F':
            count += 1

print(count)