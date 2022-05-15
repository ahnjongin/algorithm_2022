def countSum(m, nums):
    table = [0] * (m + 1)
    table[0] = 1
    for i in range(m):
        if table[i] != 0:
            for x in nums:
                if i + x <= m:
                    table[i + x] += table[i]
    return table[m]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n = list(map(int, input().split()))
        num = list(map(int, input().split()))
        print(countSum(m, num))