class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #bubblesorting
        n=len(nums)
        res=[]
        for i in range(len(nums)):
            for j in range(0,n-i-1):
                #print("==============")
                #print("nums[j]:",nums[j],"nums[j+1]:",nums[j+1])
                #print("==============")
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    #print(nums)
        
        for i in range(len(nums)):
            a=nums[i]
            if a>0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threesum=a+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
'''
        tup=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        tmp=[nums[i],nums[j],nums[k]]
                        tup.add(tuple(tmp))
        
        return [list(i) for i in tup]
'''
        
