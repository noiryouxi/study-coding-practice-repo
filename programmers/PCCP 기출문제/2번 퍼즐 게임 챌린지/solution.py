def solution(diffs, times, limit):
    n = len(diffs)

    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for i in range(n):
            if diffs[i] <= mid:
                total += times[i]
            else:
                fail = diffs[i] - mid
                total += fail * (times[i] + times[i - 1]) + times[i]

            if total > limit:
                break

        if total <= limit:
            right = mid - 1
        else:
            left = mid + 1

    return left