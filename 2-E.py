from sys import stdin

def solve(m,nums):
    if m<0: return None
    if m==0: return []
    best = None
    for x in nums:
        ret=solve(m-x, nums)
        if ret is not None:
            if best is None or len(best)>len(ret)+1:
                ret.append(x)
                best = ret
    return best
T=int(stdin.readline())
for _ in range(T):
    m,n=list(map(int, input().split()))
    nums=list(map(int, input().split()))
    sol=solve(m,nums)
    if sol is None: print("-1")
    else: print(len(sol), " ".join(str(i) for i in sol))
