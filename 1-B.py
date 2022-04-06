testcase = int(input())
for i in range(testcase):
    count = 0
    a = input()
    for j in range(len(a)-2):
        if len(set(a[j:j+3])) == 3:
            count += 1
    print(count)