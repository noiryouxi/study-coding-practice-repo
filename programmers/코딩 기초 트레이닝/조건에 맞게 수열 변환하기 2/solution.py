def solution(arr):
    answer = 0

    for num in arr:
        cnt = 0
        x = num

        while True:
            if x >= 50 and x % 2 == 0:
                x //= 2
                cnt += 1
            elif x < 50 and x % 2 == 1:
                x = x * 2 + 1
                cnt += 1
            else:
                break

        answer = max(answer, cnt)

    return answer