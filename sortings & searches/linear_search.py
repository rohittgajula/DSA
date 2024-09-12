# LINEAR SEARCH

# start a loop and compare each element with target.

# time complexity : O(n) - where n is num of elements in list
# space complexity : O(1)
# this is prefered for small and unsorted sets of list

def linear_search(arr, target):
  count = 0
  while count < len(arr):
    if arr[count] == target:
      return True, f'at index : {count}'
    count += 1

  # for i in range(len(arr)):
  #   if arr[i] == target:
  #     return True, f'at index : {i}'
  # return False


arr = [5,8,4,6,9,2]
target = 9
print(linear_search(arr, target))
