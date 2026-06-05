class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProfit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit
'''
        n=len(prices)
        a=0
        while(n>0):
            for i in range(len(prices)-1):
                print(i)
                if (prices[i+1]<prices[i]):
                    print("prices[i]:",prices[i],"prices[i+1]:",prices[i+1])
                    a=0
                    n-=1
                    if (prices[i+1]>prices[i]):
                        break
            return a
'''