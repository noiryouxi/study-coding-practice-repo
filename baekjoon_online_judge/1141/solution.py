n = int(input())
words = [input().strip() for _ in range(n)]

words.sort()

count = 0

for i in range(n):
    if i == n - 1:
        count += 1
    else:
        if not words[i+1].startswith(words[i]):
            count += 1

print(count)