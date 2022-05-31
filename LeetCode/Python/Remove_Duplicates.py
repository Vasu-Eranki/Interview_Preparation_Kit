class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictionary = {}
        length = 0
        indices = 0
        for i in range(0,len(nums)):
            if(nums[i] not in dictionary):
                dictionary[nums[i]] = i
                length = length+1
                nums[indices] = nums[i]
                indices+=1
            else:
                #nums[i]= nums[indices]
                continue
        return length 
        
