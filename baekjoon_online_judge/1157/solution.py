import sys

word = sys.stdin.readline().strip().upper()

count = [0] * 26

for ch in word:
    count[ord(ch) - ord('A')] += 1

max_count = max(count)

# 최대값이 여러 개면 ?
if count.count(max_count) > 1:
    print("?")
else:
    print(chr(count.index(max_count) + ord('A')))