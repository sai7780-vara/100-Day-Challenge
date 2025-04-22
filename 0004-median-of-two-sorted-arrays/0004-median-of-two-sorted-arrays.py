class Solution(object):
    def findMedianSortedArrays(self, n1, n2):
        i = 0
        j = 0
        k = len(n1) + len(n2)
        s = []

        while len(s) <= k // 2:
            if i < len(n1) and (j >= len(n2) or n1[i] <= n2[j]):
                s.append(n1[i])
                i += 1
            else:
                s.append(n2[j])
                j += 1

        if k % 2 == 0:
            return (s[k//2] + s[k//2 - 1]) / 2.0
        else:
            return s[k//2]
