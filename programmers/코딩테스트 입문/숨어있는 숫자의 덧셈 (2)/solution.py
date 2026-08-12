def solution(my_string):
    answer = 0
    num = ""

    for char in my_string:
        if char.isdigit():
            num += char
        else:
            if num:
                answer += int(num)
                num = ""

    # 문자열이 숫자로 끝나는 경우
    if num:
        answer += int(num)

    return answer