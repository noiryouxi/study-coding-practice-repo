def solution(arr, query):
    for i, j in enumerate(query):
        if i % 2 == 0 :
            arr = arr[:j+1]
        else :
            arr = arr[j:]
    return arr