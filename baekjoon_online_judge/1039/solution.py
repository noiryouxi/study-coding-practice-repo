from collections import deque

N, K = input().split()
K = int(K)

# 자리수가 1이면 swap 불가
if len(N) == 1:
    print(-1)
    exit()

q = deque()
q.append(N)

# visited[depth] = set of numbers
visited = [set() for _ in range(K + 1)]
visited[0].add(N)

for depth in range(K):
    for _ in range(len(q)):
        cur = q.popleft()
        cur_list = list(cur)
        M = len(cur_list)

        for i in range(M):
            for j in range(i + 1, M):
                nxt = cur_list[:]
                nxt[i], nxt[j] = nxt[j], nxt[i]

                # 앞자리가 0이면 무효
                if nxt[0] == '0':
                    continue

                nxt_str = ''.join(nxt)

                if nxt_str not in visited[depth + 1]:
                    visited[depth + 1].add(nxt_str)
                    q.append(nxt_str)

# K번 정확히 수행한 결과가 없으면 -1
if not visited[K]:
    print(-1)
else:
    print(max(visited[K]))