def solution(emergency):
    answer = []

    for x in emergency:
        rank = 1
        for y in emergency:
            if x < y:
                rank += 1
        answer.append(rank)

    return answer