class Solution(object):
    def canPlaceFlowers(self, f, n):
        k=len(f)
        s=0
        if k==1 and f[0]==0:
            s=s+1
        
        for i in range(k-1):
            if i==0:
                if f[0]==0 and f[1]==0:
                    s=s+1
                    f[0]=1
            if f[i]==0 and f[i-1]==0 and f[i+1]==0:
                s=s+1
                f[i]=1
        if f[k-1]==0 and f[k-2]==0:
            s=s+1
            
        return s>=n