def solution(arr):
    x = len(arr)          # 행 개수
    y = len(arr[0])       # 열 개수

    length = max(x, y)

    answer = [[0] * length for _ in range(length)]

    for i in range(x):
        for j in range(y):
            answer[i][j] = arr[i][j]

    return answer