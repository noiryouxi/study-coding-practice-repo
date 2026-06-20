def solution(arr):
    stk = []

    for num in arr:
        if stk and stk[-1] == num:
            stk.pop()
        else:
            stk.append(num)

    return stk or [-1]