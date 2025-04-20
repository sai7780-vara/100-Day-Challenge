class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        k= sorted(nums)
        s ={}
        for i,n in enumerate(k):
            if n not in s:
                s[n]=i
        r = []
        for i in nums:
            r.append(s[i])
        return r
            
            
        
        