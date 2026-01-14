n = int(input())
friends = [input().strip() for _ in range(n)]

answer = 0

for i in range(n):
    two_friends = set()

    for j in range(n):
        if i == j:
            continue

        # 직접 친구인 경우
        if friends[i][j] == 'Y':
            two_friends.add(j)
        else:
            # 공통 친구가 있는 경우
            for k in range(n):
                if friends[i][k] == 'Y' and friends[k][j] == 'Y':
                    two_friends.add(j)
                    break

    answer = max(answer, len(two_friends))

print(answer)