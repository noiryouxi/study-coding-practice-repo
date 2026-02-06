def digit_sum_upto(n):
    if n < 0:
        return 0

    result = 0
    factor = 1

    while factor <= n:
        higher = n // (factor * 10)
        current = (n // factor) % 10
        lower = n % factor

        # higher 부분
        result += higher * 45 * factor

        # current 부분
        result += (current * (current - 1) // 2) * factor
        result += current * (lower + 1)

        factor *= 10

    return result


L, U = map(int, input().split())
print(digit_sum_upto(U) - digit_sum_upto(L - 1))