from fractions import Fraction as F

# ----------------------------
# 1. 입력 처리
# ----------------------------
N, M = map(int, input().split())
lx = ly = -1  # 광원 위치 초기화
room = []
wall_count = 0

for y in range(N):
    row = input()
    room.append(row)
    for x in range(M):
        if row[x] == '*':
            lx, ly = x, y
        elif row[x] == '#':
            wall_count += 1

# ----------------------------
# 2. 삼각형 면적 계산 함수
# ----------------------------
def get_triangle_area(x_top, x_bottom, x_target):
    """
    빛이 칸의 모서리를 넘어갈 때,
    남는 삼각형 면적을 계산하기 위한 함수
    """
    base_len = abs(x_bottom - x_target)
    height_len = abs((x_bottom - x_target) / (x_bottom - x_top)) if x_bottom != x_top else 0
    return base_len * height_len / 2

# ----------------------------
# 3. y 방향 한 줄에서 빛 영역 계산
# ----------------------------
def get_light_area_and_next(dy, curr_lights, walls):
    """
    현재 줄(curr_lights)에서 다음 줄(dy)로 빛이 전달될 때
    실제로 도달하는 면적(light_area)과
    다음 줄에서의 빛 영역(next_lights)을 계산
    """
    light_area = F(0)
    next_lights = []
    curr_light_ind = 0
    light_mult = F(dy+1, dy)  # 빛이 퍼지는 비율

    prev_block = True
    next_block = False

    for i in range(len(walls)):
        if curr_light_ind >= len(curr_lights):
            break
        if i == len(walls) - 1:
            next_block = True
        else:
            next_block = walls[i+1]

        if not walls[i]:
            x_center = F(i - len(walls)//2)
            x_left = x_center - F(1, 2)
            x_right = x_center + F(1, 2)

            for li in range(curr_light_ind, len(curr_lights)):
                light_l, light_r = curr_lights[li]

                if light_r <= x_left:
                    curr_light_ind = li + 1
                    continue
                if light_l >= x_right:
                    break

                light_l = max(light_l, x_left)
                light_r = min(light_r, x_right)
                if light_l >= light_r:
                    continue

                # 삼각형/부채꼴 면적 계산
                light_dl = light_mult * light_l
                light_dr = light_mult * light_r
                curr_area = (light_r - light_l + light_dr - light_dl) / 2

                if prev_block and light_dl < x_left:
                    curr_area -= get_triangle_area(light_l, light_dl, x_left)
                    if light_dr < x_left:
                        curr_area += get_triangle_area(light_r, light_dr, x_left)
                if next_block and light_dr > x_right:
                    curr_area -= get_triangle_area(light_r, light_dr, x_right)
                    if light_dl > x_right:
                        curr_area += get_triangle_area(light_l, light_dl, x_right)

                light_area += curr_area

                # 다음 줄의 빛 영역 갱신
                if light_dl < x_left and prev_block:
                    light_dl = x_left
                if light_dr > x_right and next_block:
                    light_dr = x_right
                if light_dl < light_dr:
                    if len(next_lights) > 0 and next_lights[-1][1] == light_dl:
                        next_lights[-1][1] = light_dr
                    else:
                        next_lights.append([light_dl, light_dr])

        prev_block = walls[i]

    return light_area, next_lights

# ----------------------------
# 4. 특정 offset의 벽 좌표 생성
# ----------------------------
def get_wall_coords(lx, ly, dx, dy, offset):
    """
    광원(lx, ly) 기준, dx/dy 방향으로 offset만큼 떨어진 줄의 벽 좌표 생성
    """
    for i in range(-offset, offset+1):
        yield (lx + dx*offset + dy*i, ly + dy*offset + dx*i)

# ----------------------------
# 5. 좌표가 벽인지 확인
# ----------------------------
def get_wall(x, y):
    if 0 <= x < M and 0 <= y < N:
        return room[y][x] == '#'
    return True  # 방 밖도 벽으로 취급

# ----------------------------
# 6. 전체 빛 영역 계산
# ----------------------------
def get_light_area(room, lx, ly):
    total = F(1)  # 광원이 있는 칸의 중심
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # 좌우상하
        curr_lights = [(F(-1,2), F(1,2))]  # 초기 빛 영역
        offset = 1
        while True:
            walls = [get_wall(x, y) for x, y in get_wall_coords(lx, ly, dx, dy, offset)]
            if all(walls):
                break
            curr_area, next_lights = get_light_area_and_next(F(2*offset-1,2), curr_lights, walls)
            total += curr_area
            offset += 1
            curr_lights = [(l, r) for l, r in next_lights if l < r]
            if not curr_lights:
                break
    return total

# ----------------------------
# 7. 최종 그림자 면적 계산
# ----------------------------
light_area = get_light_area(room, lx, ly)
shadow_area = float(N*M - wall_count - light_area)

print(f"{shadow_area:.12f}")