class Solution(object):
    def s(self, A, B):
        a = abs(A[0] - B[0])
        b = abs(A[1] - B[1])
        return max(a, b)

    def minTimeToVisitAllPoints(self, points):
        k = 0 
        for i, n in enumerate(points[:-1]):
            p = self.s(n, points[i + 1])
            k += p
        return k
            
        
        