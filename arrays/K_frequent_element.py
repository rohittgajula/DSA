# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

import heapq

def topKfrequent(nums, k):
    freq = {}

    for char in nums:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    return heapq.nlargest(k, freq.keys(), key=freq.get)

nums = [1,1,1,2,2,3]
k = 2
print(topKfrequent(nums, k))

