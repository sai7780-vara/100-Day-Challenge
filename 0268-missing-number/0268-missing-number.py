class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        n=len(nums)
        n=n*(n+1)//2
        for i in nums:
            k=k+i
        
        return n-k
        