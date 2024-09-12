# Given an array, arr. The task is to find the largest element in it.

# Input: arr = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.


def largest_element(arr):

  largest_ele = 0
  
  for element in arr:
    if element > largest_ele:
      largest_ele = element
  return largest_ele


arr = [1, 8, 7, 56, 90]
print(largest_element(arr))

# time complixity : O(n) (loop is running n number of times)