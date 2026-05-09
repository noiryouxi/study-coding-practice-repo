def solution(code):
    mode = 0
    ret = []

    for idx in range(len(code)):
        if code[idx] == "1":
            mode = 1 - mode   # mode 변경
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(code[idx])
            elif mode == 1 and idx % 2 == 1:
                ret.append(code[idx])

    answer = ''.join(ret)

    return answer if answer else "EMPTY"