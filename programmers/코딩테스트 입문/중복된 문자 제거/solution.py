def solution(my_string):
    answer = ""
    seen = set()

    for ch in my_string:
        if ch not in seen:
            answer += ch
            seen.add(ch)

    return answer