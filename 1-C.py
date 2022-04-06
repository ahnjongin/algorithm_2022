def merge_sort(arr, desc=False):
    if len(arr) <= 1: return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half], desc)
    right = merge_sort(arr[half:], desc)
    mer = []

    while len(left) > 0 and len(right) > 0:
        if (left[0] > right[0] and not desc) or (left[0] < right[0] and desc):
            mer.append(right[0]);
            right.pop(0)
        else:
            mer.append(left[0]);
            left.pop(0)

    if len(left) > 0: mer += left
    if len(right) > 0: mer += right
    return mer

testcase = int(input())
for i in range(testcase):
    a = int(input())
    num = list(map(int, input().split()))
    num2=merge_sort(num)
    print(" ".join(map(str, num2)))
