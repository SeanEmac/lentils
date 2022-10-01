class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index in range(len(nums)):
            diff = target - nums[first_index]
            if diff in nums:
                second_index = nums.index(diff)
                # Can't use the same element
                if first_index != second_index:
                    return [first_index, second_index]

# The better solution is to keep a prevDict dict of number -> index pairs
# As you itterate the list you check if diff is in the prevDict
# If it is, return [ current, prevDict[diff] ]
