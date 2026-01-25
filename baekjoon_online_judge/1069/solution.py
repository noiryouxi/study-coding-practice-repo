import math

X, Y, D, T = map(int, input().split())
R = math.hypot(X, Y)

ans = R  # 전부 걷기

if R < D:
    ans = min(ans, T + (D - R), 2 * T)
else:
    k = int(R // D)
    c = math.ceil(R / D)

    ans = min(ans,
              k * T + (R - k * D),          # 점프 k번 + 걷기
              (k + 1) * T + ((k + 1) * D - R))  # 점프 k+1번 + 되돌아 걷기

    if c >= 2:
        ans = min(ans, c * T)  # 점프만 사용

print(ans)