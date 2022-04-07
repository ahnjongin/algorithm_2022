testcase = int(input())
for _ in range(testcase):
    num = int(input())
    lst = [0]*(num-1)
    lst2 = []
    lst2 = map(int, input().split())
    lst.extend(lst2)
    ch_lst = []
    for i in range(num-1):
        if (lst[-(2*i+1)] > lst[-(2*i+2)]):
            lst[num-2-i] = lst[-(2*i+1)]
            ch_lst.append(lst[-(2*i+2)])
        else:
            lst[num-2-i] = lst[-(2*i+2)]
            ch_lst.append(lst[-(2 * i + 1)])
    print(max(ch_lst))

