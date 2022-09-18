class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = binary_search(nums,target)
        return index
        
def binary_search(array,target):
    index = 0
    length = len(array)
    if(length==1) and (array[0]!=target):
        return -1
    mid_length = length//2
    actual_value = array[mid_length]
    if(actual_value==target):
        return mid_length
    elif(actual_value>target):
        index = binary_search(array[:mid_length],target)
    else:
        index =  binary_search(array[mid_length:],target)
        if(index!=-1): index = index +mid_length
    return index
