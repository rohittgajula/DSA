

def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n-1):
            if arr[i] + arr[j] == target:
                return [i, j]
    return "not possible"

def two_sum2(arr, target):
    prevMap = {}

    for i, n in enumerate(arr):
        diff = target - n
        print(prevMap)
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return



arr = [2,7,11,15]
target = 17
print(two_sum(arr, target))
print(two_sum2(arr, target))

