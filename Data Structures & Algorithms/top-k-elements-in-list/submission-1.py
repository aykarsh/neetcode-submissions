class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(list)
        numdict={}
        for i,n in enumerate(nums):
            numdict[n]=0
        for i in nums:
            numdict[i]+=1
        print(numdict)
        a=len(nums)+1
        l=[[] for _ in range(a)]
        for i,num in numdict.items():
            l[num].append(i)
        print(l)
        res=[]
        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                res.append(n)
                if len(res)==k:
                    return res