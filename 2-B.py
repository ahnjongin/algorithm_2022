from sys import stdin

def solve(m,nums):
    if m<0: return False
    if m==0: return True
    for x in nums:
        if solve(m-x, nums): return True
    return False
T=int(stdin.readline())
for _ in range(T):
    m,n=list(map(int, input().split()))
    nums=list(map(int, input().split()))
    sol=solve(m,nums)
    if solve(m, nums):
        print('true')
    else: print('false')
