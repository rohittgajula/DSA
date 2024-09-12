# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


def rotate_array(nums, k):
  k = k % len(nums)
  l, r = 0, len(nums) - 1
  while l < r:                      # reverse the array
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l+1, r-1

  # reverce the first k elements
  l, r = 0, k - 1
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l+1, r-1

  # reverse elements after k
  l , r = k, len(nums) - 1
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l+1, r-1

  return nums

def rotate_array_fun(nums, k):
  n = len(nums)
  k = k % n

  def reverse(l, r):
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l+1, r-1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

  return nums

nums = [0,1,2,4,5,6,7]
k = 3
print(rotate_array(nums, k))
print(rotate_array_fun(nums, k))