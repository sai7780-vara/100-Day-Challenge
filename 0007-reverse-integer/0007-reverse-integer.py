class Solution:
    def reverse(self, x: int) -> int:
        m= 2**31 -1
        sign = -1 if x<0 else 1
        x = abs(x)
        f=0
        while x!=0:
            k= x%10
            x=x//10
            f = f*10 + k
            if f > m:
                return 0 
        return sign * f
