def solution(score):
    sums = [sum(s) for s in score]
    return [sum(x > s for x in sums) + 1 for s in sums]