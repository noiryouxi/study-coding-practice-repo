def solution(arr):
    return [ i / 2 if i % 2 == 0 and i >= 50 else i * 2 if i % 2 == 1 and i < 50 else i for i in arr]