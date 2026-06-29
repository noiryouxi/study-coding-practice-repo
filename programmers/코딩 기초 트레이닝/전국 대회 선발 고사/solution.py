def solution(rank, attendance):
    students = sorted(range(len(rank)), key=lambda x: rank[x])

    selected = []

    for s in students:
        if attendance[s]:
            selected.append(s)
        if len(selected) == 3:
            break

    return 10000 * selected[0] + 100 * selected[1] + selected[2]