# BINARY SEARCH

# slice the array into half and compare it with target value. if not fount shift left or right pointers accordingly to the middle pointer. (array shourd be sorted)



# All the values should be sorted
def binary_search(nums, target):
  left_pointer = 0
  right_pointer = len(nums) - 1

  while left_pointer <= right_pointer:
    middle_index = (left_pointer + right_pointer) // 2

    # check middel index
    if nums[middle_index] == target:
      return f'target fount at : {middle_index}'
    # check left sorted position
    elif nums[middle_index] < target:
      left_pointer = middle_index + 1
    # check right sorted position
    else:
      right_pointer = middle_index - 1

  return f'targte not found'


nums = [2, 4, 5, 6, 8, 9]
target = 4
print(binary_search(nums, target))

