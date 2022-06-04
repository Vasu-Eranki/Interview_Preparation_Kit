class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer_2 = 0
        for i in range(0,len(nums)):
            if(nums[i]==val):
                continue
            nums[pointer_2] = nums[i]
            pointer_2 = pointer_2+1
        return pointer_2
