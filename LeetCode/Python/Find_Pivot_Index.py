class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        for i in range(0,len(nums)):
            left_sum = sum(nums[:i])
            if(total_sum-nums[i]-left_sum)==left_sum:
                return i
        return -1
