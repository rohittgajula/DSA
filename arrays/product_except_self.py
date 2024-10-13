# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def product_except_self(nums):
    n = len(nums)

    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n

    for i in range(1, n):
        left_product[i] = left_product[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * nums[i+1]
    
    for i in range(n):
        result[i] = left_product[i] * right_product[i]
    
    return result

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        t = 1
        r = 1
        res = [1] * n

        for i in range(n):
            res[i] *= t
            t *= nums[i]
            res[n-i-1] *= r
            r *= nums[n-i-1]

        return res


nums = [-1,1,0,-3,3]
print(product_except_self(nums))

solution = Solution()
print(solution.productExceptSelf(nums))