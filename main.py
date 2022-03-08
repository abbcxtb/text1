def min(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr =[64, 29, 57, 16, 98, 18, 67, 32, 57, 60, 16, 27, 98, 17, 23, 51, 19, 73, 47, 21]

min(arr)

print("排序后的数组:")
print("%d" % arr[12])