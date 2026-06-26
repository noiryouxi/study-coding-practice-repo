def solution(strArr):
    count = {}
    answer = 0

    for s in strArr:
        length = len(s)
        count[length] = count.get(length, 0) + 1
        answer = max(answer, count[length])

    return answer