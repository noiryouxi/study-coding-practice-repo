def solution(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    answer = []

    while i >= 0 or j >= 0 or carry:
        x = ord(a[i]) - ord('0') if i >= 0 else 0
        y = ord(b[j]) - ord('0') if j >= 0 else 0

        s = x + y + carry
        answer.append(chr(s % 10 + ord('0')))
        carry = s // 10

        i -= 1
        j -= 1

    return ''.join(reversed(answer))