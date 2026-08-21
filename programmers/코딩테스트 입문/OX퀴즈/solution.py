def solution(quiz):
    answer = []

    for q in quiz:
        x, op, y, equal, z = q.split()

        x = int(x)
        y = int(y)
        z = int(z)

        if op == "+":
            result = x + y
        else:
            result = x - y

        answer.append("O" if result == z else "X")

    return answer