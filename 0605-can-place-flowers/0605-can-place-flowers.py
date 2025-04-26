class Solution(object):
    def canPlaceFlowers(self, f, n):
        k = len(f)
        s = 0
        for i in range(k):
            if f[i] == 0:
                empty_left = (i == 0) or (f[i-1] == 0)
                empty_right = (i == k-1) or (f[i+1] == 0)
                if empty_left and empty_right:
                    f[i] = 1
                    s += 1
        return s >= n
