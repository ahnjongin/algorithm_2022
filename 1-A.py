testcase = int(input())
card = []
l = []
for i in range(testcase):
    a = int(input())
    card = list(map(int, input().split()))
    l = set(card)
    if len(card) == len(l):
        print("false")
    else:
        print("true")