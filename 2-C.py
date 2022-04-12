from sys import stdin

def solve(m,nums):
    if m<0: return None
    if m==0: return []
    for x in nums:
        ret=solve(m-x, nums)
        if ret is not None:
            ret.append(x)
            return ret
    return None
T=int(stdin.readline())
for _ in range(T):
    m,n=list(map(int, input().split()))
    nums=list(map(int, input().split()))
    sol=solve(m,nums)
    if sol is None: print("-1")
    else: print(len(sol), " ".join(str(i) for i in sol))
