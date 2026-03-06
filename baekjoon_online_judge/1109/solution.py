from collections import Counter
import sys

input = sys.stdin.readline

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]


def init():
    global N,M,map_list
    N,M=map(int,input().split())
    map_list=[input().strip() for _ in range(N)]


def full_dfs(x,y,idx,visited):

    stack=[(x,y)]
    visited[y][x]=idx

    while stack:

        x,y=stack.pop()

        for k in range(8):

            ax=x+dx[k]
            ay=y+dy[k]

            if 0<=ax<M and 0<=ay<N:
                if map_list[ay][ax]=='x' and visited[ay][ax]==-1:
                    visited[ay][ax]=idx
                    stack.append((ax,ay))


def inside_dfs(x,y,idx):

    is_outside=False
    contact_set=set()

    stack=[(x,y)]

    local=[[False]*M for _ in range(N)]
    local[y][x]=True

    while stack:

        x,y=stack.pop()

        for k in range(4):

            ax=x+dx[k]
            ay=y+dy[k]

            if 0<=ax<M and 0<=ay<N:

                if visited[ay][ax]==-1 and not local[ay][ax]:
                    local[ay][ax]=True
                    stack.append((ax,ay))

                elif visited[ay][ax]!=-1 and visited[ay][ax]!=idx:
                    contact_set.add(visited[ay][ax])

            else:
                is_outside=True

    return is_outside,contact_set


def full_search():

    global visited,target_node

    visited=[[-1]*M for _ in range(N)]
    target_node=[]

    idx=0

    for i in range(N):
        for j in range(M):

            if map_list[i][j]=='x' and visited[i][j]==-1:

                full_dfs(j,i,idx,visited)
                target_node.append((j,i))
                idx+=1


def bfs(node,contact_dict,score_list,visited,memo):

    if memo[node]!=-1:
        return memo[node]

    nxt_list=[]

    for nxt in contact_dict[node]:

        if not visited[nxt]:
            visited[nxt]=True
            nxt_list.append(nxt)

    result=0

    for nxt in nxt_list:
        result=max(result,bfs(nxt,contact_dict,score_list,visited,memo)+1)

    score_list[node]=result
    memo[node]=result

    return result


def inside_search():

    contact_dict={}
    outside_list=[]

    for idx,(x,y) in enumerate(target_node):

        is_outside,contact_set=inside_dfs(x,y,idx)

        if is_outside:
            outside_list.append(idx)

        contact_dict[idx]=contact_set

    for i in range(len(target_node)):
        for j in contact_dict[i]:
            contact_dict[j].add(i)

    inside_visited=[False]*len(target_node)

    for x in outside_list:
        inside_visited[x]=True

    score_list=[0]*len(target_node)
    memo=[-1]*len(target_node)

    for node in outside_list:
        bfs(node,contact_dict,score_list,inside_visited,memo)

    maxval=max(score_list)

    counter=Counter(score_list)

    result=[0]*(maxval+1)

    for k,v in counter.items():
        result[k]=v

    print(*result)


def solve():

    init()
    full_search()

    if not target_node:
        print(-1)
        return

    inside_search()


solve()