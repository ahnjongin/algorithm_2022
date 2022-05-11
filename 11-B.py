from copy import deepcopy


def howSum(m, nums, memo):
    if m < 0: return None
    if m == 0: return []
    if m in memo: return memo[m]
    for x in nums:
        li = howSum(m - x, nums, memo)
        if li is not None:
            ne = deepcopy(li)
            ne.append(x)
            memo[m] = ne
            return ne
    memo[m] = None
    return None


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n = list(map(int, input().split()))
        num = list(map(int, input().split()))
        memo = dict()
        res = howSum(m, num, memo)
        if res is not None:
            print(len(res), end=" ")
            print(" ".join(str(x) for x in res))
        else:
            print(-1)
