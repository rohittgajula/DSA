# There is an integer array nums sorted in ascending order (with distinct values).

# time complexity : O(n)
def search_array(nums, target):
  for i in range(len(nums)):
    if nums[i] == target:
      return i
  return -1

# time complexity : O(log n)
def search_rotated_array(nums, target):
  l, r = 0, len(nums)-1

  while l <= r:
    mid = (l + r) // 2

    # check middle value is the target
    if target == nums[mid]:
      return f'target is at {mid}'
    
    if nums[l] <= nums[mid]:
      if target > nums[mid] or target < nums[l]:
        l = mid + 1
      else:
        r = mid - 1
    else:
      if target < nums[mid] or target > nums[r]:
        r = mid - 1
      else:
        l = mid + 1
  return f'Target not found.'



nums = [4,5,6,7,0,1,2]
target = 4
# print(search_array(nums, target))
print(search_rotated_array(nums, target))

