# Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

# using set
# time complexity : O(n1 + n2)
def union_array(nums1, nums2):
  s = set()
  union = []

  for item in nums1:
    s.add(item)
  for item in nums2:
    s.add(item)
  for num in s:
    union.append(num)
  return union

# using pointers
# time complexity : O(m + n)
# space complexity : O(m + n) {if space of union is considered else O(1)}
def union_array_pointers(nums1, nums2):
  i = 0
  j = 0
  union = []

  while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
      if len(union) == 0 or union[-1] != nums1[i]:
        union.append(nums1[i])
      i += 1
    else:
      if len(union) == 0 or union[-1] != nums2[j]:
        union.append(nums2[j])
      j += 1

  # for any element left in nums1
  while i < len(nums1):
    if union[-1] != nums1[i]:
      union.append(nums1[i])
    i += 1
  # for any element left in nums2
  while j < len(nums2):
    if union[-1] != nums2[j]:
      union.append(nums2[j])
    j += 1

  return union

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 6, 7]
print(union_array(nums1, nums2))
print(union_array_pointers(nums1, nums2))