def solution(array):
    max_num = 0
    max_count = 0
    answer = -1

    for num in set(array):
        count = array.count(num)

        if count > max_count:
            max_count = count
            answer = num
        elif count == max_count:
            answer = -1

    return answer