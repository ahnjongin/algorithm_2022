from collections import deque
from sys import stdin

def bfs(G, start, visited):

    queue = deque([start])
    visited[start] = True
    no_cnt = 1
    while queue:
        v = queue.popleft()
        for i in G[v]:
            if not visited[i]:
                queue.append(i)
                no_cnt += 1
                visited[i] = True
    cnt_lst.append(no_cnt)

T = int(stdin.readline())
for _ in range(T):
    cnt_lst = []
    N, E = list(map(int, stdin.readline().split()))
    edges = list(map(int, stdin.readline().split()))
    visited = [False] * (N + 1)
    G = [[] for _ in range(N)]
    for i in range(0, len(edges), 2):
        G[edges[i]].append(edges[i + 1])
        G[edges[i + 1]].append(edges[i])
    cnt = 0
    for j in range(N):
        if not visited[j]:
            bfs(G, j, visited)
            cnt += 1
    print(cnt, max(cnt_lst))

