testcase = int(input())
for _ in range(testcase):
    num = int(input())
    lst = list(map(int, input().split()))
    max = 0
    min = 0
    if lst[0] < lst[1]:
        max = lst[1]
        min = lst[0]
    else:
        max = lst[0]
        min = lst[1]
    i = 2
    while i < len(lst)-1:
        if lst[i] < lst[i+1]:
            if lst[i] < min: min = lst[i]
            if lst[i+1] > max: max = lst[i+1]
        else:
            if lst[i+1] < min: min = lst[i+1]
            if lst[i] > max: max = lst[i]
        i += 2
    if i == len(lst)-1:
        if lst[i] < min: min = lst[i]
        elif lst[i] > max: max = lst[i]

    print(max, min)
