class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        l=[]
        for i,a in enumerate(heights):
            #print("left:",left,"right:",right)
            length=abs(left-right)
            #print("length:",length)
            height=min(heights[left],heights[right])
            #print("height:",height)
            area=length*height
            l.append(area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            #print(l)
        return max(l)
