class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dnums=set(nums)
        if len(Dnums)!=len(nums):
            return True
        else:
            return False