def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 1:
            if i % 2 == 0:
                arr[i] += n
        else:
            if i % 2 == 1:
                arr[i] += n
    return arr