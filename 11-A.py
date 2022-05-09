def canSum(m, nums, memo):
    if m<0: return False
    if m==0: return True
    if m in memo: return memo[m]
    for i in nums:
        if canSum(m-i, nums, memo):
            memo[m] = True
            return True
    memo[m] = False
    return False


if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        m,n = list(map(int, input().split()))
        num = list(map(int, input().split()))
        memo = dict()
        canSum(m, num, memo)
        if memo[m] == True:
            print("true")
        else:
            print("false")


