def solution(array, n):
    array.sort(key=lambda x: (abs(x - n), x))
    return array[0]