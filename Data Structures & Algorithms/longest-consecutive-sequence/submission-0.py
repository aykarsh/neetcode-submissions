class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
        numSet=set(nums)
        longest=0
        for i in nums:
            if(i-1) not in numSet:
                length=0
                while i+length in numSet:
                    length+=1
                longest=max(length,longest)
        return longest