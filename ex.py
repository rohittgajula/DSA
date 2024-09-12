

#          i
arr = [12, 35, 1, 10, 34, 1, 100]
#      l
#      s

def solution(arr):
  largest = 0

  for i in range(len(arr)):
    if arr[i] > largest:
      largest = arr[i]
  return largest


print(solution(arr))

