def solution(arr):
    n = 1

    while n < len(arr):
        n *= 2

    return arr + [0] * (n - len(arr))