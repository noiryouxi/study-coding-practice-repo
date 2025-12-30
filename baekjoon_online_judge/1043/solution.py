import sys
input = sys.stdin.readline

# Union-Find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

truth_info = list(map(int, input().split()))
truth_count = truth_info[0]
truth_people = truth_info[1:]

parties = []

# 파티 정보 입력 + union
for _ in range(M):
    data = list(map(int, input().split()))
    people = data[1:]
    parties.append(people)
    for i in range(len(people) - 1):
        union(people[i], people[i + 1])

# 진실을 아는 사람들의 root 집합
truth_roots = set(find(p) for p in truth_people)

# 과장 가능한 파티 세기
answer = 0
for party in parties:
    can_lie = True
    for person in party:
        if find(person) in truth_roots:
            can_lie = False
            break
    if can_lie:
        answer += 1

print(answer)