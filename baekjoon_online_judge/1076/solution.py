colors = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

first = input().strip()
second = input().strip()
third = input().strip()

# 앞 두 색으로 기본 값 만들기
value = colors[first][0] * 10 + colors[second][0]

# 세 번째 색의 곱 적용
result = value * colors[third][1]

print(result)