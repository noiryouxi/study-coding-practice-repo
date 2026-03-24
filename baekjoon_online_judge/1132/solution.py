import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

weight = [0] * 10
is_leading = [False] * 10

# 가중치 계산
for word in words:
    is_leading[ord(word[0]) - ord('A')] = True
    length = len(word)
    for i in range(length):
        idx = ord(word[i]) - ord('A')
        weight[idx] += 10 ** (length - i - 1)

# (알파벳 index, 가중치) 리스트
letters = [(i, weight[i]) for i in range(10)]
letters.sort(key=lambda x: -x[1])

# 숫자 배정
digit = 9
assign = [-1] * 10

# 0 배정할 문자 찾기
for i in range(9, -1, -1):
    idx = letters[i][0]
    if not is_leading[idx]:
        assign[idx] = 0
        letters.pop(i)
        break

# 나머지 9부터 배정
for idx, _ in letters:
    if assign[idx] == -1:
        assign[idx] = digit
        digit -= 1

# 결과 계산
result = 0
for word in words:
    num = 0
    for ch in word:
        num = num * 10 + assign[ord(ch) - ord('A')]
    result += num

print(result)