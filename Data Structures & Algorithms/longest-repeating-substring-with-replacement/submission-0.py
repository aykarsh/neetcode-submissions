class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        left=0
        max_length=0
        max_freq=0
        for right in range(len(s)):
            counts[s[right]]=counts.get(s[right],0)+1
            max_freq=max(max_freq,counts[s[right]])

            curr_wndw_size=right-left+1
            if curr_wndw_size-max_freq>k:
                counts[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
            
        