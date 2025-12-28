N = int(input())
A, B, C, D, E, F = map(int, input().split())

if N == 1:
    print(A + B + C + D + E + F - max(A, B, C, D, E, F))
    exit()

one = min(A, B, C, D, E, F)

two = min(
    A + min(B, C, D, E),
    F + min(B, C, D, E),
    B + min(A, C, D, F),
    E + min(A, C, D, F),
    C + min(A, B, E, F),
    D + min(A, B, E, F)
)

three = min(
    A+B+C, A+B+D, A+E+C, A+E+D,
    F+B+C, F+B+D, F+E+C, F+E+D
)

answer = (
    4 * three +
    (8*N - 12) * two +
    (5*N*N - 16*N + 12) * one
)

print(answer)