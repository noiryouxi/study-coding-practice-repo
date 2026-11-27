def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    def f(t):
        m = (t * 59) // 3600
        h = (t * 719) // 43200

        # 12시 정각 중복 제거
        return m + h - (t // 43200)

    answer = f(end) - f(start)

    # 시작 시간이 정각이면 해당 알람 포함
    if start % 43200 == 0:
        answer += 1

    return answer