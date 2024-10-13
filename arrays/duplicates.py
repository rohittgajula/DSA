def duplicates1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return True
    return False

def duplicates2(arr):
    n = len(arr)
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
    return False

def duplicates3(arr):
    hashSet = set()
    for num in arr:
        if num in hashSet:
            return True
        hashSet.add(num)
    return False

arr = [1,2,3,1]
print(duplicates1(arr))
print(duplicates2(arr))
print(duplicates3(arr))

