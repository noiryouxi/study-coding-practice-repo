import sys
input = sys.stdin.readline

sentence = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

L = len(sentence)
INF = float('inf')

# dp[i] = sentence[:i]까지 해석하는 최소 비용
dp = [INF] * (L + 1)
dp[0] = 0

from collections import Counter

# 단어별 문자 카운트 미리 계산
word_counters = [Counter(w) for w in words]

for i in range(L):
    if dp[i] == INF:
        continue
    
    for idx, w in enumerate(words):
        length = len(w)
        
        if i + length > L:
            continue
        
        sub = sentence[i:i+length]
        
        # 아나그램 체크
        if Counter(sub) != word_counters[idx]:
            continue
        
        # 비용 계산 (위치가 다른 문자 수)
        cost = sum(1 for a, b in zip(sub, w) if a != b)
        
        dp[i+length] = min(dp[i+length], dp[i] + cost)

print(dp[L] if dp[L] != INF else -1)