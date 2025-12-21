from collections import Counter

N, M = map(int, input().split())
rows = [input().strip() for _ in range(N)]
K = int(input())

counter = Counter(rows)
answer = 0

for row, count in counter.items():
    zeros = row.count('0')
    if zeros <= K and (K - zeros) % 2 == 0:
        answer = max(answer, count)

print(answer)