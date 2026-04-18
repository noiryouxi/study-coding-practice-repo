import bisect

def solution(n, bans):
    
    def get_index(s):
        res = 0
        for l in range(1, len(s)):
            res += 26 ** l
        for i, ch in enumerate(s):
            res += (ord(ch) - ord('a')) * (26 ** (len(s) - i - 1))
        return res + 1
    
    def get_string(k):
        length = 1
        while k > 26 ** length:
            k -= 26 ** length
            length += 1
        
        res = []
        for i in range(length):
            base = 26 ** (length - i - 1)
            idx = (k - 1) // base
            res.append(chr(ord('a') + idx))
            k -= idx * base
        
        return ''.join(res)
    
    ban_idx = sorted(get_index(b) for b in bans)
    
    left, right = n, n + len(bans)
    
    while left <= right:
        mid = (left + right) // 2
        removed = bisect.bisect_right(ban_idx, mid)
        
        if mid - removed >= n:
            right = mid - 1
        else:
            left = mid + 1
    
    return get_string(left)