def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            print(j)
            if j == "7":
                answer += 1
    return answer