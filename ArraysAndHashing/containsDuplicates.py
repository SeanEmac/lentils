# Easy
# Arrays & Hashing

# Input: nums = [1,2,3,1]
# Output: true
    
# Input: nums = [1,2,3,4]
# Output: false
    
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# This question will only work when using a set,
# Using an array will exceed the timeout
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # uniqueList = []
        hashset = set()

        for number in nums:
            if number in hashset:
                # We have already encountered this number so it's a duplicate
                return True
            # Add it to the set of unique numbers
            hashset.add(n)
        # Have itterated through the numbers and found no duplicates
        return False