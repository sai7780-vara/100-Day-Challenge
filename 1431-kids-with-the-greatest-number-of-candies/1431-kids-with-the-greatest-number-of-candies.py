class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
         maximum = max(candies)
         k=[]
         for i in range (len(candies)):
            if candies[i]+ extraCandies >= maximum : 
                k.append(True)
            else :
                k.append(False)
         return k
