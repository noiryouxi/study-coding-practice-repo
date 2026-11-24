from collections import defaultdict

def solution(points, routes):
    answer = 0

    # 각 로봇의 시간별 위치를 저장
    positions = []

    for route in routes:
        path = []

        # 첫 번째 포인트에서 시작
        r, c = points[route[0] - 1]
        path.append((r, c))

        # 나머지 포인트 순서대로 이동
        for i in range(1, len(route)):
            nr, nc = points[route[i] - 1]

            # r 좌표를 먼저 이동
            while r != nr:
                r += 1 if nr > r else -1
                path.append((r, c))

            # 그 다음 c 좌표 이동
            while c != nc:
                c += 1 if nc > c else -1
                path.append((r, c))

        positions.append(path)

    # 시간별로 로봇의 위치를 확인
    max_time = max(len(path) for path in positions)

    for t in range(max_time):
        count = defaultdict(int)

        for path in positions:
            # 운송이 끝난 로봇은 제외
            if t < len(path):
                count[path[t]] += 1

        # 같은 좌표에 2대 이상의 로봇이 있으면 위험 상황
        for robot_count in count.values():
            if robot_count >= 2:
                answer += 1

    return answer