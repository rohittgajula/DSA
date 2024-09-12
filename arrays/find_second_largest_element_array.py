# Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

# Input: arr = [12, 35, 1, 10, 34, 1, 100]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.


def find_second_largest(arr):
  
  largest = arr[0]
  second_largest = arr[0]
  # largest
  for element in arr:
    if element > largest:
      largest = element
  # second largest
  for element in arr:
    if element != largest and element > second_largest:
      second_largest = element
  return second_largest


def find_second_largest2(arr):
  largest = arr[0]                  
  second_largest = arr[0]          

  for i in range(len(arr)):
    if arr[i] > largest:
      second_largest = largest 
      largest = arr[i]              
    elif (arr[i] != largest and arr[i] > second_largest):
      second_largest = arr[i]

  return largest, second_largest
  
arr = [12, 35, 1, 10, 34, 1, 100]
print(find_second_largest(arr))
print(find_second_largest2(arr))

