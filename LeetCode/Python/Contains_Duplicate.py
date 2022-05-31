class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        return True if (len(sets)!=len(nums)) else False
        
