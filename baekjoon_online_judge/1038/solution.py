from itertools import combinations

N = int(input())

decreasing_numbers = []

# 1자리부터 10자리까지 모든 조합 생성
for length in range(1, 11):
    for comb in combinations(range(10), length):
        # 내림차순 정렬
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        decreasing_numbers.append(num)

# 오름차순 정렬
decreasing_numbers.sort()

# N번째 감소하는 수 출력
if N < len(decreasing_numbers):
    print(decreasing_numbers[N])
else:
    print(-1)