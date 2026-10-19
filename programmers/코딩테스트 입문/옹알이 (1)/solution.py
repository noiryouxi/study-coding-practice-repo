def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for word in words:
            b = b.replace(word, " ")

        if b.strip() == "":
            answer += 1

    return answer