def solution(my_strings, parts):
    result = []

    for string, (s, e) in zip(my_strings, parts):
        result.append(string[s:e+1])

    return "".join(result)