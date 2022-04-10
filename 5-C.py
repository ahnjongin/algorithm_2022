def quick_sort(lst, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and lst[left] <= lst[pivot]):
            left += 1
        while(right > start and lst[right] >= lst[pivot]):
            right -= 1
        if(left > right):
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            lst[left], lst[right] = lst[right], lst[left]
    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)


testcase = int(input())
for _ in range(testcase):
    num = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)
    print(lst[(num[1]-1)])