def solution(n):
    factorial = 1
    i = 1

    while factorial * (i + 1) <= n:
        i += 1
        factorial *= i

    return i