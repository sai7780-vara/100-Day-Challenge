class Solution(object):
    def reverseWords(self, m):
        k=""
        s=[]
        for i in m:
            if i!=" ":
                k=k+i 
            else:
                if len(k)!=0:
                    s.append(k)
                k=""
        if len(k)!=0:
            s.append(k)
        return(' '.join(reversed(s)))    