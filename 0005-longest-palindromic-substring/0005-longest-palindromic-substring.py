class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # the last valid palindrome
        
        res = ""
        for i in range(len(s)):
            # Odd-length palindromes (center at i)
            p1 = expand(i, i)
            # Even-length palindromes (center between i and i+1)
            p2 = expand(i, i+1)
            # Choose the longer one
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        return res
