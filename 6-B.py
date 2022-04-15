from sys import stdin
def detectCycle(G, visited, v, visiting):
    visiting.add(v)
    for w in G[v]:
        if visited[w]: continue
        if w in visiting: return True
        if detectCycle(G, visited, w, visiting): return True
    visited[v] = True
    return False
def solve(G):
    visited = [False] * len(G)
    for v in range(len(G)):
        if not visited[v] and detectCycle(G, visited, v, set()):
            return True
    return False

T = int(stdin.readline())
for _ in range(T):
    N, E = list(map(int, stdin.readline().split()))
    edges = list(map(int, stdin.readline().split()))
    G = [[] for _ in range(N)]
    for i in range(0, len(edges), 2):
        G[edges[i]].append(edges[i+1])
    print('true' if solve(G) else 'false')
