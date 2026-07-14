def solution(s1, s2):
    answer = 0

    for word in s1:
        if word in s2:
            answer += 1

    return answer