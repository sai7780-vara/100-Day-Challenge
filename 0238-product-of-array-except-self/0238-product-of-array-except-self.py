class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Left pass: accumulate product of elements to the left of current index
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
        
        # Right pass: accumulate product of elements to the right and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res
