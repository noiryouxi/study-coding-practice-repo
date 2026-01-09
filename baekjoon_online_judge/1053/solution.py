def palindrome_dp(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for length in range(2, n+1):
        for l in range(n - length + 1):
            r = l + length - 1
            if s[l] == s[r]:
                dp[l][r] = dp[l+1][r-1] if l+1 <= r-1 else 0
            else:
                dp[l][r] = 1 + min(
                    dp[l+1][r],      # 삭제 or 삽입
                    dp[l][r-1],
                    dp[l+1][r-1]     # 교체
                )
    return dp[0][n-1] if n > 0 else 0


s = list(input().strip())
n = len(s)

# 1. swap 없이
answer = palindrome_dp(s)

# 2. swap 한 번 사용
for i in range(n):
    for j in range(i+1, n):
        if s[i] != s[j]:
            s[i], s[j] = s[j], s[i]
            answer = min(answer, palindrome_dp(s) + 1)
            s[i], s[j] = s[j], s[i]  # 복구

print(answer)