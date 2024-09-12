# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

def remove_elements(nums):
  st = set()
  for i in range(len(nums)):
    st.add(nums[i])
  k = len(st)
  j = 0
  for x in st:
    nums[j] = x
    j += 1
  return k, nums

# time comp : O(n)
def remove_duplicates2(nums):
  j = 0
  for i in range(1, len(nums)):
    if nums[i] != nums[j]:
      j += 1
      nums[j] = nums[i]
  return j + 1

def remove_duplicate3(nums):
  noduplist = []
  for element in nums:
    if element not in noduplist:
      noduplist.append(element)

  return len(noduplist), noduplist 


nums = [0,0,1,1,1,2,2,3,3,4]
# print(remove_elements(nums))
print(remove_duplicates2(nums)) # this is the most efficent way
# print(remove_duplicate3(nums))
