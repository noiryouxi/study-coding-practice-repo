import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

# 기본적으로 필요한 글자
base_letters = {'a', 'n', 't', 'i', 'c'}

# K가 5보다 작으면 어떤 단어도 읽을 수 없음
if K < 5:
    print(0)
    sys.exit()

# 각 단어를 비트마스크로 변환
def word_to_bitmask(word):
    mask = 0
    for ch in word:
        mask |= 1 << (ord(ch) - ord('a'))
    return mask

word_masks = []
for word in words:
    # "anta"와 "tica" 제거
    core = word[4:-4]
    word_masks.append(word_to_bitmask(core))

# 기본 글자 비트마스크
base_mask = 0
for ch in base_letters:
    base_mask |= 1 << (ord(ch) - ord('a'))

# 추가로 배울 수 있는 글자들
candidates = set()
for mask in word_masks:
    for i in range(26):
        if mask & (1 << i):
            if not (base_mask & (1 << i)):
                candidates.add(i)

candidates = list(candidates)

answer = 0

# 가능한 조합 탐색
for comb in combinations(candidates, min(K - 5, len(candidates))):
    learn_mask = base_mask
    for c in comb:
        learn_mask |= 1 << c

    count = 0
    for word_mask in word_masks:
        if word_mask & ~learn_mask == 0:
            count += 1

    answer = max(answer, count)

print(answer)