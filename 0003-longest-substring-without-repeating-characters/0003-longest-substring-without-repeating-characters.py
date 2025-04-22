class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        k=""
        for i in s:
            if i not in k:
                k=k+i
            else:
                l=max( len(k),l)
                p=k.index(i)
                k=k[p+1:]+i
            l=max( len(k),l)   
        return l 
        