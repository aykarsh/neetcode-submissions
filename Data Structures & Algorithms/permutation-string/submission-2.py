class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashsets1={}
        hashsets2={}
        k=len(s1)

        if len(s1)>len(s2):
            return False
        for i in s1:
            if i not in hashsets1:
                hashsets1[i]=1
            else:
                hashsets1[i]+=1
        
        for j in range(k):
            char=s2[j]
            if char not in hashsets2:
                hashsets2[char]=1
            else:
                hashsets2[char]+=1
        
        if hashsets1==hashsets2:
            return True 
    
        for r in range(k,len(s2)):
            newchar=s2[r]
            oldchar=s2[r-k]
            if newchar not in hashsets2:
                hashsets2[newchar]=1
            else:
                hashsets2[newchar]+=1

            hashsets2[oldchar]-=1
            if hashsets2[oldchar]==0:
                del hashsets2[oldchar]
            if hashsets2==hashsets1:
                return True       
        return False
        