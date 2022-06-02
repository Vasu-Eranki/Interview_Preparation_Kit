class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            target_number = target-nums[i]
            if(target_number in nums):
                for j in range(0,len(nums)):
                    if(nums[j]==target_number) and (i!=j):
                        return [i,j]
            else:
                continue
