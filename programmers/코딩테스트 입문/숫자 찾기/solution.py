def solution(num, k):
    index = str(num).find(str(k))
    return index + 1 if index != -1 else -1