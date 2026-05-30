from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    count = Counter(dice)

    if len(count) == 1:  # 4개 모두 같음
        p = dice[0]
        return 1111 * p

    elif len(count) == 2:
        nums = list(count.items())

        # 3개 + 1개
        if 3 in count.values():
            for num, cnt in nums:
                if cnt == 3:
                    p = num
                else:
                    q = num
            return (10 * p + q) ** 2

        # 2개 + 2개
        else:
            p, q = count.keys()
            return (p + q) * abs(p - q)

    elif len(count) == 3:
        # 2개 + 1개 + 1개
        qr = []
        for num, cnt in count.items():
            if cnt == 1:
                qr.append(num)
        return qr[0] * qr[1]

    else:  # len(count) == 4
        return min(dice)