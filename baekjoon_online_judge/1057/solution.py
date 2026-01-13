N, a, b = map(int, input().split())

round_num = 0

while a != b:
    a = (a + 1) // 2
    b = (b + 1) // 2
    round_num += 1

    if a == 0 or b == 0:
        print(-1)
        break
else:
    print(round_num)