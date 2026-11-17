def solution(mats, park):
    rows = len(park)
    cols = len(park[0])

    # 큰 돗자리부터 검사
    mats.sort(reverse=True)

    for size in mats:
        # 돗자리가 공원 크기보다 크면 건너뛰기
        if size > rows or size > cols:
            continue

        # 모든 시작 위치 확인
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):

                # size x size 영역이 모두 비어 있는지 확인
                possible = True

                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":
                            possible = False
                            break
                    if not possible:
                        break

                if possible:
                    return size

    return -1