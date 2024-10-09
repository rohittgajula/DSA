# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.



# this is for normal sorted array
def check_array(nums):
  for i in range(len(nums)):
    if nums[i] > nums[i+1]:
      return False
  return True

# this is for sorted and rotated array.
def check_rotated_array(nums):
  count = 0
  n = len(nums)
  for i in range(n):
    print(i, (i + 1) // n)
    if nums[i] > nums[(i + 1) % n]:
      count += 1
    if count > 1:
      return False
  return True

nums = [3,4,5,1,2,9]
print(check_array(nums))
print(check_rotated_array(nums))

