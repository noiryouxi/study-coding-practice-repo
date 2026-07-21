def solution(A, B):
    if A == B:
        return 0

    s = A

    for i in range(1, len(A) + 1):
        s = s[-1] + s[:-1]  # 오른쪽으로 한 칸 회전
        if s == B:
            return i

    return -1