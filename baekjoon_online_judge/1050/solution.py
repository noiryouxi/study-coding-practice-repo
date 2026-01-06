import sys

LIMIT = 1_000_000_000

n, m = map(int, sys.stdin.readline().split())

# cost[name] = 최소 비용, -1이면 아직 불가능
cost = {}

# 레시피 저장: (결과물, [(개수, 재료), ...])
recipes = []

# 시장 재료 입력
for _ in range(n):
    name, c = sys.stdin.readline().split()
    cost[name] = int(c)

# 레시피 입력
for _ in range(m):
    tmp = sys.stdin.readline().strip()

    left, right = tmp.split('=')
    parts = right.split('+')

    req = []
    for p in parts:
        cnt = int(p[0])
        name = p[1:]
        if name not in cost:
            cost[name] = -1
        req.append((cnt, name))

    if left not in cost:
        cost[left] = -1

    recipes.append((left, req))

# 반복 완화
updated = True
while updated:
    updated = False
    for name, req in recipes:
        total = 0
        valid = True
        for cnt, ing in req:
            if cost[ing] != -1:
                total += cnt * cost[ing]
                if total > LIMIT:
                    total = LIMIT + 1
            else:
                valid = False
                break

        if valid and total > 0:
            if cost[name] == -1 or cost[name] > total:
                cost[name] = total
                updated = True

# 결과 출력
if "LOVE" not in cost or cost["LOVE"] == -1:
    print(-1)
else:
    print(cost["LOVE"])