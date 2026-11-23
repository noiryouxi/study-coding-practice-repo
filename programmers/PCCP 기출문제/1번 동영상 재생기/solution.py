def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s

    def to_time(seconds):
        return f"{seconds // 60:02d}:{seconds % 60:02d}"

    video = to_seconds(video_len)
    pos = to_seconds(pos)
    start = to_seconds(op_start)
    end = to_seconds(op_end)

    # 시작 위치가 오프닝 구간이면 건너뛰기
    if start <= pos <= end:
        pos = end

    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        elif command == "next":
            pos = min(video, pos + 10)

        # 명령 수행 후 오프닝 구간 확인
        if start <= pos <= end:
            pos = end

    return to_time(pos)