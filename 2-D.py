from sys import stdin


def solve(m, nums):
    if m < 0: return 0
    if m == 0: return 1
    count = 0
    for x in nums:
        count += solve(m - x, nums)
    return count


T = int(stdin.readline())
for _ in range(T):
    m, n = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    sol = solve(m, nums)
    print(sol)