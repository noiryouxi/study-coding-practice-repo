def solution(arr, k):
    answer = []
    visited = set()

    for x in arr:
        if x not in visited:
            answer.append(x)
            visited.add(x)

        if len(answer) == k:
            break

    while len(answer) < k:
        answer.append(-1)

    return answer