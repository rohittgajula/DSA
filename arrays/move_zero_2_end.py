# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


# space complixity : O(n^2)
def move_zeros(nums):
  nonzero = []
  zeroele = []
  for i in nums:
    if i != 0:
      nonzero.append(i)
    else:
      zeroele.append(i)
  return nonzero + zeroele

# using L, R pointers
# space complexity : O(1)
def move_zeros_pointers(nums):
  l = 0
  for r in range(len(nums)):
    if nums[r]:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
  return nums


nums = [0,1,0,3,12]
print(move_zeros(nums))
print(move_zeros_pointers(nums))