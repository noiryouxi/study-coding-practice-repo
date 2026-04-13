n = int(input())
count = [0] * 26  # a~z

for _ in range(n):
    name = input().strip()
    first = ord(name[0]) - ord('a')
    count[first] += 1

result = []

for i in range(26):
    if count[i] >= 5:
        result.append(chr(i + ord('a')))

if result:
    print(''.join(result))
else:
    print("PREDAJA")