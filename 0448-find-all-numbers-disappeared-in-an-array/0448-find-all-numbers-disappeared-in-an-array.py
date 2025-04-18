class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])  # mark as visited

        # Collect indexes that were not marked
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
