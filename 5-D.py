testcase = int(input())
for _ in range(testcase):
    num = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    count = {}
    for i in lst:
        count[i] = count.get(i,0) + 1
    lst2 = sorted(count.items(), key= lambda x: x[1], reverse= True)
    max_lst = []
    for i in range(num[1]):
        a, _ = lst2[i]
        max_lst.append(a)
    print(" ".join(map(str, max_lst)))
