
def sol(nlist):
    def merge(left, right):
        global count
        merged_list = []
        while left and right:
            if right[0] < left[0]:
                count += len(left)
                merged_list.append(right.pop(0))
            else:
                merged_list.append(left.pop(0))
        if left:
            merged_list += left
        elif right:
            merged_list += right
        return merged_list

    if len(nlist) == 1:
        return nlist

    mid = len(nlist) // 2
    left = sol(nlist[:mid])
    right = sol(nlist[mid:])
    return merge(left, right)


for _ in range(int(input())):
    num = int(input())
    nlist = list(map(int, input().split()))
    count = 0
    sol(nlist)
    print(count)