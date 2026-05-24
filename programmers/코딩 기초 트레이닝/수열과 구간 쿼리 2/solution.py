def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        value = float('inf')

        for i in range(s, e + 1):
            if arr[i] > k:
                value = min(value, arr[i])

        if value == float('inf'):
            answer.append(-1)
        else:
            answer.append(value)

    return answer