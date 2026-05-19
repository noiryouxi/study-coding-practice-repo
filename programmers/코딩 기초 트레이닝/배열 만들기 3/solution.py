def solution(arr, intervals):
    return [
        x
        for start, end in intervals
        for x in arr[start:end+1]
    ]