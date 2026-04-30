def solution(binomial):
    answer = 0
    arr = binomial.split()
    if arr[1] == "+":
        answer = int(arr[0]) + int(arr[2])
    elif arr[1] == "-":
        answer = int(arr[0]) - int(arr[2])
    else :
        answer = int(arr[0]) * int(arr[2])
    return answer