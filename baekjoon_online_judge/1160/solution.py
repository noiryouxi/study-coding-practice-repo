def mat_mul(A, B, mod):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
    ]

def mat_pow(mat, n, mod):
    result = [[1, 0], [0, 1]]  # identity
    while n:
        if n % 2:
            result = mat_mul(result, mat, mod)
        mat = mat_mul(mat, mat, mod)
        n //= 2
    return result

m, a, c, X0, n, g = map(int, input().split())

M = [[a, c], [0, 1]]
Mn = mat_pow(M, n, m)

Xn = (Mn[0][0] * X0 + Mn[0][1]) % m

print(Xn % g)