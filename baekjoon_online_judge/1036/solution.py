import sys
input = sys.stdin.readline

N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())

# 문자 ↔ 값 변환
def char_to_val(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10

def val_to_char(v):
    if v < 10:
        return chr(v + ord('0'))
    return chr(v - 10 + ord('A'))

# 문자별 이득 계산
gain = [0] * 36

for s in nums:
    length = len(s)
    for i, c in enumerate(s):
        val = char_to_val(c)
        pos = length - i - 1
        gain[val] += (35 - val) * (36 ** pos)

# 이득이 큰 K개 선택
indices = sorted(range(36), key=lambda x: gain[x], reverse=True)
chosen = set(indices[:K])

# 바꾼 후 합 계산
total = 0
for s in nums:
    val = 0
    for c in s:
        v = char_to_val(c)
        if v in chosen:
            v = 35
        val = val * 36 + v
    total += val

# 36진수로 변환
if total == 0:
    print("0")
else:
    result = []
    while total > 0:
        result.append(val_to_char(total % 36))
        total //= 36
    print("".join(reversed(result)))