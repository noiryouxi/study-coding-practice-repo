def solution(names):
    answer = []
    for num in range(len(names)):
        if num % 5 == 0 :
            answer.append(names[num])
    return answer