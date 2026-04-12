class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1={}
        w2={}
        
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                w1[s[i]]=1 + w1.get(s[i],0)
                w2[t[i]]=1 + w2.get(t[i],0)
            return w1==w2