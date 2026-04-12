class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        if len(nums)==2:
            return [0,1]
        else:
            complement=0
            for i,n in enumerate(nums):
                print(i,n)
                complement=target-nums[i]
                print(d)
                
                print(complement)
                if complement in d:
                    print(nums)
                    return [d[complement],i]
                
                d[n]=i       
                