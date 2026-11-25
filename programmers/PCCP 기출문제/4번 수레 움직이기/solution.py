from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    red_start = blue_start = None
    red_end = blue_end = None
    walls = set()

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)
            elif maze[i][j] == 5:
                walls.add((i, j))

    # 상태: 빨간 위치, 파란 위치, 빨간 방문 칸, 파란 방문 칸
    start = (
        red_start,
        blue_start,
        frozenset([red_start]),
        frozenset([blue_start])
    )

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, count = queue.popleft()

        red, blue, red_visited, blue_visited = state

        # 두 수레 모두 도착했다면 종료
        if red == red_end and blue == blue_end:
            return count

        # 빨간 수레의 다음 이동 후보
        if red == red_end:
            red_next = [red]
        else:
            red_next = []
            for dx, dy in directions:
                nx, ny = red[0] + dx, red[1] + dy
                pos = (nx, ny)

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if pos in walls or pos in red_visited:
                    continue

                red_next.append(pos)

        # 파란 수레의 다음 이동 후보
        if blue == blue_end:
            blue_next = [blue]
        else:
            blue_next = []
            for dx, dy in directions:
                nx, ny = blue[0] + dx, blue[1] + dy
                pos = (nx, ny)

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if pos in walls or pos in blue_visited:
                    continue

                blue_next.append(pos)

        # 두 수레의 이동 조합 확인
        for nr in red_next:
            for nb in blue_next:

                # 같은 칸에 위치할 수 없음
                if nr == nb:
                    continue

                # 서로 자리를 바꾸는 이동 불가능
                if nr == blue and nb == red:
                    continue

                new_state = (
                    nr,
                    nb,
                    red_visited | {nr},
                    blue_visited | {nb}
                )

                if new_state in visited:
                    continue

                visited.add(new_state)
                queue.append((new_state, count + 1))

    return 0